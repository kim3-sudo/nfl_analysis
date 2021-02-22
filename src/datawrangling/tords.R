### NFL Data Analysis
### Josh Katz & Sejin Kim
### STAT 306 S21 @ Kenyon College

data <- read.csv2("/home/kim3/nfl_analysis/src/datawrangling/nflfastr_2010_2020_kicks_passes.csv")

saveRDS(data, file = "/home/kim3/nfl_analysis_data/nflfastr_2010_2020_kicks_passes.rds")