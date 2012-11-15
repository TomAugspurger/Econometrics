data = read.csv("clean_growth.csv")

# Regessions: growth on
# 1: tradeshare and yearsschool

q1 <- rq(growth ~ tradeshare + yearsschool, tau=.5, data)

summary(q1)
