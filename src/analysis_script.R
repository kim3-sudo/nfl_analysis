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
library(pwr)
library(agricolae)
library(multcomp)
library(car)
library(tidyr)

# Load in nflfastR
data <- readRDS(url('https://github.com/kim3-sudo/nfl_analysis_data/blob/main/nflfastr_pbp_2010_to_2020.rds?raw=true'))

##########################################################################
# Do some EDA of the main effects
favstats(data$kick_distance~data$game_stadium) # nothing exceptional, but mean distance not what was expected
summary(favstats(data$kick_distance~data$game_stadium))
favstats(data$air_yards~data$game_stadium) # nothing special
summary(favstats(data$air_yards~data$game_stadium))
favstats(data$kick_distance~data$home_team) # nothing special, SDs are astonishingly similar
favstats(data$kick_distance~data$away_team)
## Confirm that home and away kicking distance differences are not statistically significant
homeawayModel = aov(data$kick_distance ~ data$home_team * data$away_team)
summary(homeawayModel)
favstats(data$air_yards~data$home_team)
favstats(data$air_yards~data$away_team) # teams pass roughly the same distance regardless of whether they're home or away
homeawayPassModel = aov(data$air_yards ~ data$home_team * data$away_team)
summary(homeawayPassModel)
favstats(data$kick_distance~data$temp) # if it sucks to kick in the cold, it's a minute effect in EDA
favstats(data$air_yards~data$temp) # ditto for passing
  # a few outliers, but nothing seemingly out of the ordinary - all are exceptional in the same way
  # the really low bar is for Mile High game_stadium (home: DEN), curious!
par(mar=c(8, 4.1, 4.1, 2.1))
boxplot(data$air_yards~data$game_stadium, las = 3, main = "Intended Passing Yardage by Game Stadium", xlab = "Stadium", ylab = "Intended Passing Yardage")
  # most passes are not long (see favstats), but of course, there are hail marys and longer passes
  # most passes are under 10 yards
boxplot(data$kick_distance~data$game_stadium, las = 2, main = "Actual Kicking Distance by Game Stadium", xlab = "Stadium", ylab = "Kick Distance")
  # little difference between bars is what we want to see, good!
boxplot(data$kick_distance~data$away_team, las = 2)
  # ditto
boxplot(data$air_yards~data$home_team, las = 2)
  # 4all teams play at roughly similar level
boxplot(data$air_yards~data$away_team, las = 2)
  # ditto
boxplot(data$kick_distance~data$temp, main = "Kick Distance by Temperature", xlab = "Temperature (Degrees Fahrenheit)", ylab = "Kick Distance")
  # much more variance at lower temperatures, but past freezing, it stabilizes quite a bit - a mental block? Probably more games are played at higher temps, so more data
boxplot(data$air_yards~data$temp, main = "Intended Passing Yardage by Temperature", xlab = "Temperature (Degrees Fahrenheit)", ylab = "Intended Passing Yardage")
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
# Secondary data cleansing
kickData = data
passData = data
kickreqd <- as.vector(c("kick_distance", "game_stadium", "temp"))
passreqd <- as.vector(c("air_yards", "game_stadium", "temp", "cp", "cpoe"))
kickData = kickData[,kickreqd]
passData = passData[,passreqd]
kickData = na.omit(kickData)
passData = na.omit(passData)
# Do not run below code
if(FALSE) {
kickData %>% na.omit('kick_distance', na.action = "omit")
kickData %>% na.omit('game_stadium', na.action = "omit")
kickData %>% na.omit('temp', na.action = "omit")
passData %>% drop_na('air_yards')
passData %>% drop_na('game_stadium')
passData %>% drop_na('temp')
}
##########################################################################
# Construct F-test for overall model

kickModel = aov(kickData$kick_distance~kickData$temp*kickData$game_stadium, na.action = na.exclude)
passModel = aov(passData$air_yards~passData$temp*passData$game_stadium, na.action = na.exclude)
nullKickModel = aov(kickData$kick_distance~1, na.action = na.exclude)
nullPassModel = aov(passData$air_yards~1, na.action = na.exclude)

anova(kickModel, nullKickModel)
anova(passModel, nullPassModel)

# Check assumptions for two-way ANOVA with interaction
plot(kickModel, 1:2)
  # residuals vs fitted plot looks wonky, but it's because there's so much data that patterns are emerging
  # normal QQ plot looks okay, but not great - it'd pass the fat marker test, but not the pencil test
plot(passModel, 1:2)
  # residuals vs fitted plot looks bad, bc there's so much similar data and temperature and game_stadium are related
  # a lot of columns are showing, but not predictably - we should interpret results with care
  # normal QQ plot looks BAD - there's a definite curve that strays away from a normal curve on either end
  # this could be interpreted as meaning that there are some really good passes and some really bad passes that far outweigh the normal pass
fligner.test(kickData$kick_distance, interaction(kickData$temp,kickData$game_stadium))
fligner.test(passData$air_yards, interaction(passData$temp,passData$game_stadium))
# need to test
# remember: big p-val means homoskedasticity

summary(kickModel)
summary(passModel)

##########################################################################
# Construct F-test for two-way interactions

kickModel2 = aov(kick_distance ~ temp * game_stadium, data = kickData)
passModel2 = aov(air_yards ~ temp * game_stadium, data = passData)
summary(kickModel2)
  # The interaction is not significant at 0.05 = alpha
summary(passModel2)
  # The interaction IS significant at 0.05 = alpha

##########################################################################
# Construct the model for kicking (since interaction's not significant)
realKickModel = aov(kick_distance ~ temp + game_stadium, data = kickData)
summary(realKickModel)
  # Stadium is significant, temperature is not
realKickLM = lm(kick_distance ~ temp + game_stadium, data = kickData)
summary(realKickLM)
plot(realKickLM, 1:2)

##########################################################################
# Examine cp and cpoe
n_ij = xtabs(~temp+game_stadium, data = passData)
xtabs(cp ~ temp + game_stadium, data = passData)/n_ij3
# Again, some interactions!

cpStadiumModel = aov(cp ~ game_stadium*temp, data = passData)
summary(cpModel)
nullCpModel = aov(cp ~ 1, data = passData)
anova(cpStadiumModel, nullCpModel)
fligner.test(passData$cp, interaction(passData$temp, passData$game_stadium))

plot(cpStadiumModel, 2)
# oof that ain't it chief, need to use a Welch 2-sample t-test instead
summary(cpStadiumModel)

t(rank(passData$cp) ~ passData$game_stadiumpassData$temp)

