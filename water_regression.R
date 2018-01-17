waterdata<-read.csv("F:/Projects/linear_regression/beijing.csv")
lm1<-lm(NH3~NH3_total_discharg+NH3_industrial_discharge,data=waterdata)

summary(lm1)
