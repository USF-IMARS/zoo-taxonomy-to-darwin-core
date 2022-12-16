# ---- load libraries ----
library("tidyverse")
library("fs")
library("magrittr")
library("cli")
library("stringr")
library("glue")
library("readxl")
library("lubridate")

# two files needed:
# compiled_zoo_taxonomy_Jaimie_31JAN2018 (1).xlsx
# sample-details.csv


# location of files
# look for 
# compiled_zoo_taxonomy_Jaimie_31JAN2018 (1).xlsx
file_location <- file.choose()

# look for sample-details.csv
meta_samples_file <- file.choose()

file_location
meta_samples_file

# - or - type it in yourself 
# ex
# file_location <- "~/<folder>/compiled_zoo_taxonomy_Jaimie_31JAN2018 (1).xlsx"

# read all sheet names and filter for ones with WS and LK
# WS = Western Sambo
# LK = Looe Key
sheets <-
    readxl::excel_sheets(file_location) %>%
    
    # turn into tibbles (DON'T worry about what it is)
    tibble(sheets = .) %>%
    
    # filter(str_detect(sheets, "^(WS|LK)")) %>%
    filter(!str_detect(sheets, "Samples|PL")) %>%
    mutate(
        sheet = if_else(str_detect(sheets, "MR116500"), "MR0116500", sheets),
        sheet = if_else(str_detect(sheets, "WS0117640"), "WS011764", sheet),
        stn   = str_sub(sheet, 1, 2),
        month = str_sub(sheet, 3, 4),
        year  = str_sub(sheet, 5, 6),
        mesh  = str_sub(sheet, 7, 10)  %>% str_remove(., "2$"),
        dup   = if_else(str_detect(sheet, "2$"), "duplicate", "")
    )  %>%
    select(-sheet) %>%
    arrange(year, month, stn, mesh)

# if you want to reorder the xlsx file
# temp <- sheets %>% 
#     mutate(
#         # metadata
#         data = map(sheets, 
#                    ~ readxl::read_xlsx(file_location, sheet = .,
#                    )))
# map2(.x = tests$data, .y = tests$sheets, 
#      ~ xlsx::write.xlsx(.x, 
#                         paste0(dirname(file_location), "/zoo_fix.xlsx"), 
#                         sheetName = .y,
#                         append = TRUE,
#                         showNA = FALSE))
# rm(temp)

# read each sheet for data and metadata
species <- 
    sheets %>%
    
    # add 2 columns and loop through each file to load
    # 1. meta data (inludes date and location)
    # 2. data (includes species info)
    mutate(
        # metadata
        meta = map(sheets, 
                   ~ readxl::read_xlsx(file_location, sheet = .,
                                       n_max = 7, col_names = FALSE,
                                       .name_repair = janitor::make_clean_names)),
        # species data
        data = map(sheets, 
                   ~ readxl::read_xlsx(file_location, sheet = ., skip = 7,
                                       .name_repair = janitor::make_clean_names,
                                       na = c("", "#VALUE!")))
    )

# extract the data within the list
species <- species %>%
    unnest(data) 

# find columns of list that have na's
num_na <- species %>%
    filter(is.na(n_ind_m3)) %>%
    count(sheets)

# determine if na for individuals per cubic meter are because:
# 1. there was no volume recorded
# 2. the specie didn't exist
species <- species %>%
    mutate(
        no_vol = if_else(
            sheets %in% num_na$sheets[num_na$n > 1],
            "no volume recorded", ""
        )
    )

# load metadata and fix
meta_samples <- 
    meta_samples_file %>%
    read_csv() %>%
    mutate(
        month   = format(Date, "%m"),
        year    = format(Date, "%y"),
        day     = format(Date, "%d"),
        .before = Date
    ) %>%
    mutate(
        stn = case_when(
                    str_detect(Station, "Mol") ~ "MR",
                    str_detect(Station, "West") ~ "WS",
                    str_detect(Station, "Loo") ~ "LK",
        ),
        mesh_size_um = strsplit(as.character(`mesh size (um)`), "/"),
        .before = `mesh size (um)`
    ) %>%
    unnest(mesh_size_um) %>%
    mutate(mesh_size_um = str_trim(mesh_size_um)) %>%
    distinct(stn, Date, mesh_size_um, .keep_all = TRUE)
 
write_csv(species,
          file = paste0(dirname(file_location), 
                        "/zoo_compiled.csv"),
          na = "")

# merge metadata with zoo data
# this combines month, year, station and mesh 
species1 <- 
    species %>%
    left_join(
        meta_samples,
        by = c("year" = "year",
               "month" = "month",
               "stn" = "stn",
               "mesh" = "mesh_size_um")
    ) %>%
    select(
        -c(`Tow time (min)`:Comment, `flowmeter in`, ...1,
           `mesh size (um)`, Station)
    ) %>%
    relocate(
        year, month, day, Date, `Local time (EST)`, `LON in`, `LAT in`, 
        .before = month
    ) %>%
    relocate(dup, meta, .after = no_vol) %>%
    relocate(n_ind_m3, .after = clasification)

write_csv(species1,
          file = paste0(dirname(file_location), 
                        "/zoo_compiled_with_meta.csv"),
          na = "")


