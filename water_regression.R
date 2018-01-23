beijing<-read.csv("F:/Projects/linear_regression/beijing.csv",header=TRUE)
tianjin<-read.csv("F:/Projects/linear_regression/tianjin.csv",header=TRUE)
hebei<-read.csv("F:/Projects/linear_regression/hebei.csv",header=TRUE)



#just test
#lm_beijing<-lm(log(NH3)~1+log(NH3_industrial_discharge)+log(NH3_domestic_discharge),data=beijing)


#industrial_wastewater_treatment_facilities

#quality_5~industrial_wastewater_treatment_facilities*wastewater_industrial_discharge
lm_beijing<-lm(quality_5~1+wastewater_industrial_discharge*industrial_wastewater_treatment_facilities,data=beijing)
lm_hebei<-lm(quality_5~1+wastewater_industrial_discharge*industrial_wastewater_treatment_facilities,data=hebei)
lm_tianjin<-lm(quality_5~1+wastewater_industrial_discharge*industrial_wastewater_treatment_facilities,data=tianjin)

#quality_5~industrial_wastewater_treatment_facilities*COD_industrial_discharge
#lm_beijing<-lm(quality_5~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=beijing)
#lm_hebei<-lm(quality_5~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=hebei)
#lm_tianjin<-lm(quality_5~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=tianjin)

#COD~industrial_wastewater_treatment_facilities*COD_industrial_discharge
#lm_beijing<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=beijing)
#lm_hebei<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=hebei)
#lm_tianjin<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=tianjin)

#COD~industrial_wastewater_treatment_facilities*COD_industrial_discharge
#lm_beijing<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=beijing)
#lm_hebei<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=hebei)
#lm_tianjin<-lm(COD~1+COD_industrial_discharge*industrial_wastewater_treatment_facilities,data=tianjin)

#fertilizer

#lm_beijing<-lm(quality_5~1+wastewater_industrial_discharge*industrial_wastewater_treatment_facilities,data=beijing)
#lm_hebei<-lm(quality_5~1+wastewater_industrial_discharge*industrial_wastewater_treatment_facilities,data=hebei)
#lm_tianjin<-lm(quality_5~1+log(wastewater_total_discharge)+log(COD_total_discharge)+log(NH3_total_discharg),data=tianjin)




#summary
summary(lm_beijing)
summary(lm_tianjin)
summary(lm_hebei)
#anova(lm_beijing)
#plot(lm_beijing, las = 1)
