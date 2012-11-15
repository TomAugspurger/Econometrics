require(quantreg)
require(robustbase)

my_data = read.csv("clean_growth.csv")
no_malta = my_data[1:64,c('country_name', 'growth', 'tradeshare', 'yearsschool')]

# Regessions: growth on
# 1: tradeshare and yearsschool

l1 <- lm(growth ~ tradeshare + yearsschool, data = my_data)
l2 <- lm(growth ~ tradeshare + yearsschool, data = no_malta)

q1 <- rq(growth ~ tradeshare + yearsschool, tau=.5, data = my_data)
q2 <- rq(growth ~ tradeshare + yearsschool, tau=.5, data = no_malta)

# With malta
summary(l1)
summary(q1, se="nid")

# Without Malta 

summary(l2)
summary(q2, se="nid")