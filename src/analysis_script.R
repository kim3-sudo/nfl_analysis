### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

# Declare global variables for datasets

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

# Load in nflfastR
data <- readRDS(url('https://github.com/'))

# Data analysis
