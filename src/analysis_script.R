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
data <- readRDS(url('https://github.com/kim3-sudo/nfl_analysis_data/blob/main/nflfastr_pbp_2010_to_2020.rds?raw=true'))

##########################################################################
# Do some EDA of the main effects
favstats(data$kick_distance~data$game_stadium) # nothing exceptional, but mean distance not what was expected
favstats(data$air_yards~data$game_stadium) # nothing special
favstats(data$kick_distance~data$home_team) # nothing special, SDs are astonishingly similar
favstats(data$kick_distance~data$away_team)
favstats(data$air_yards~data$home_team)
favstats(data$air_yards~data$away_team) # teams pass roughly the same distance regardless of whether they're home or away
favstats(data$kick_distance~data$temp) # if it sucks to kick in the cold, it's a minute effect in EDA
favstats(data$air_yards~data$temp) # ditto for passing
  # a few outliers, but nothing seemingly out of the ordinary - all are exceptional in the same way
  # the really low bar is for Mile High game_stadium (home: DEN), curious!

boxplot(data$air_yards~data$game_stadium, las = 3)
  # most passes are not long (see favstats), but of course, there are hail marys and longer passes
  # most passes are under 10 yards
boxplot(data$kick_distance~data$home_team, las = 2)
  # little difference between bars is what we want to see, good!
boxplot(data$kick_distance~data$away_team, las = 2)
  # ditto
boxplot(data$air_yards~data$home_team, las = 2)
  # 4all teams play at roughly similar level
boxplot(data$air_yards~data$away_team, las = 2)
  # ditto
boxplot(data$kick_distance~data$temp)
  # much more variance at lower temperatures, but past freezing, it stabilizes quite a bit - a mental block? Probably more games are played at higher temps, so more data
boxplot(data$air_yards~data$temp)
  # the variance below freezing is still present, but not nearly to the same degree (pun not intended)

##########################################################################
# Do some EDA of possible interactions
# run a cross-tab
n_ij = xtabs(~data$temp+data$game_stadium)
xtabs(data$kick_distance~data$temp+data$game_stadium)/n_ij
xtabs(data$air_yards~data$temp+data$game_stadium)/n_ij
  # there are interactions to be aware of - let's investigate

# kick distance dotplot attempt
plot(data$kick_distance~as.numeric(data$temp), cex = 1.5, pch = 16, xaxt = "n", xlab = "Temperature", ylab = "Kick Distance")
axis(1, at=c(1, 2, 3), labels = levels(data$temp))
legend("topleft", title = "Kick Distance to Temperature", c(data$game_stadium),  pch = 16)

# air yards dotplot attempt
plot(data$air_yards~as.numeric(data$temp), cex = 1.5, pch = 16, xaxt = "n", xlab = "Temperature", ylab = "Air Yards")
axis(1, at=c(1, 2, 3), labels = levels(data$temp))
legend("topleft", title = "Air Yards to Temperature", c(data$game_stadium),  pch = 16)

##########################################################################
# Construct 2-way ANOVA model table
kickModel = aov(data$kick_distance~data$temp*data$stadium)
passModel = aov(data$air_yards~data$temp*data$stadium)
summary(kickModel)
summary(passModel)
