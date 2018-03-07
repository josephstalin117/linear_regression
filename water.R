
#read file
beijing<-read.csv("F:/Projects/linear_regression/beijing.csv",header=TRUE)
tianjin<-read.csv("F:/Projects/linear_regression/tianjin.csv",header=TRUE)
hebei<-read.csv("F:/Projects/linear_regression/hebei.csv",header=TRUE)

cols<-colnames(beijing)
other_factor_manage_list<-c()
other_factor_nature_list<-c()
water_quality_list<-c()
emissions_list<-c()

for(i in 1:length(cols)){
  if(i<11){
    other_factor_nature_list<-c(other_factor_nature_list,cols[i])
  }else if(i>=11 && i<16){
    water_quality_list<-c(water_quality_list,cols[i])
  }else if(i>=16 && i<30){
    emissions_list<-c(emissions_list,cols[i])
  }else{
    other_factor_manage_list<-c(other_factor_manage_list,cols[i])
  }
  
}

#print(other_factor_manage_list)
#print(other_factor_nature_list)
#print(water_quality_list)
#print(emissions_list)

interaction_ols<-function(water_qualitys,emissions,other_factors,data_source,output_file){
  lm_list<-c()
  
  for(water_item in water_qualitys){
    for(emissions_item in emissions){
      for(other_factor_item in other_factors){
        #print(water_item)
        #print(emissions_item)
        #print(other_factor_item)
        
        xnam<-c(emissions_item,other_factor_item)
        
        lm_item<-lm(as.formula(paste(paste(water_item," ~ "),paste(xnam,collapse = "*"))),data=data_source)
        
        f <- summary(lm_item)$fstatistic
        p <- pf(f[1],f[2],f[3],lower.tail=F)
        if(p<0.07){
          sink(output_file,append = TRUE)
          print(paste(paste(water_item," ~ "),paste(xnam,collapse = "*")))
          print(summary(lm_item))
          sink()
        }
      }
    }
  }
}

lm_list=interaction_ols(water_quality_list,emissions_list,other_factor_manage_list,hebei,"hebei.txt")

#lm_item<-lm(COD~1+wastewater_total_discharge*industrial_wastewater_treatment_facilities,data=beijing)
#summary(lm_item)

#summary(lm_list)


water_qualitys<-"COD"
emissions_item<-"wastewater_total_discharge"
other_factor_item<-"industrial_wastewater_treatment_facilities"
xnam<-c(emissions_item,other_factor_item)

lm_item<-lm(as.formula(paste(paste(water_qualitys," ~ "),paste(xnam,collapse = "*"))),data=beijing)
f <- summary(lm_item)$fstatistic
p <- pf(f[1],f[2],f[3],lower.tail=F)
