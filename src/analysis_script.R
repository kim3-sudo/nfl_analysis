### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

# Declare global variables for datasets
nfldata2018 = null
nfldata2019 = null
nfldata2020 = null

# Load libraries
message("####################################################################")
message("Do not proceed or halt until you see 'ALL LIBRARIES LOADED' show up.")
message("####################################################################")
# Attempt to load mosaic
mosaicResult = tryCatch({
  message("Try to load 'mosaic'")
  library(mosaic)
  message("Library load success: mosaic")
}, warning = function(w) {
  warning("Possible issue trying load library mosaic")
  mosaicResult = tryCatch({
    message("Trying to load 'mosaicCore'")
    library(mosaicCore)
  }, warning = function(w) {
    warning(w)
  }, error = function(e) {
    warning(e)
  })
}, error = function(e) {
  warning(e)
}, finally = {
  message("Finished library family load attempt: mosaic")
})
# Attempt to load ggplot2
ggplot2Result = tryCatch({
  message("Try to load 'ggplot2'")
  library(ggplot2)
  message("Library load success: ggplot2")
}, warning = function(w) {
  warning("Possible issue trying to load library ggplot2")
}, finally = {
  message("Finished single library load attempt: ggplot2")
})
# Attempt to load nflfastR
nflfastrResult = tryCatch({
  message("Try to load local 2018 dataset into var `nfldata2018`")
  nfldata2018 <- readRDS('../data/play_by_play_2018.rds')
  message("Try to load local 2019 dataset into var `nfldata2019`")
  nfldata2019 <- readRDS('../data/play_by_play_2019.rds')
  message("Try to load local 2020 dataset into var `nfldata2020`")
  nfldata2020 <- readRDS('../data/play_by_play_2020.rds')
}, warning = function(w) {
  warning("Possible issue trying load local data nflfastr")
  mosaicResult = tryCatch({
    message("Attempting to load 2018 data by remote RDS method")
    nfldata2018 <- readRDS(url('https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/data/play_by_play_2018.rds'))
    message("Attempting to load 2019 data by remote RDS method")
    nfldata2019 <- readRDS(url('https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/data/play_by_play_2019.rds'))
    message("Attempting to load 2020 data by remote RDS method")
    nfldata2020 <- readRDS(url('https://raw.githubusercontent.com/guga31bb/nflfastR-data/master/data/play_by_play_2020.rds'))
  }, warning = function(w) {
    warning(w)
  }, error = function(e) {
    warning(e)
  })
}, error = function(e) {
  warning(e)
}, finally = {
  message("Finished library family load attempt: nfldataR")
})
message("####################")
message("ALL LIBRARIES LOADED")
message("####################")

head(nfldata2018)
