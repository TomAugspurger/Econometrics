data = read.csv("clean_growth.csv")

# Regessions: growth on
# 1: tradeshare and yearsschool

endog = data[["growth"]]

exog = data[,c('tradeshare', 'yearsschool')]
q1 <- rq(endog ~ tradeshare + yearsschool, tau=.5, exog)

summary(q1)
plot(q1)
