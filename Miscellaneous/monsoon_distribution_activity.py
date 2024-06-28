import pandas as p
import numpy as np

#climatology data
clim = p.read_excel(r"C:\Users\akans\Downloads\StationWiseRainfall_kerala_July_1_7.xlsx",sheet_name="RF Clim",index_col="Jullian Days")

#2020 rainfall data
rfd = p.read_excel(r"C:\Users\akans\Downloads\StationWiseRainfall_kerala_July_1_7.xlsx",sheet_name="2020",index_col = "Jullian Days")
rfd = rfd.dropna() #dropping nan values for this case

#averaging station data
nrf= clim.mean(axis=1)
rf = rfd.mean(axis=1)

mona = []
mond = []

#to find monsoon distribution
for i in rfd.index:
    per = np.count_nonzero(np.array(rfd.loc[i])>2.4)/len(np.array(rfd.loc[i]))
    if per<0.25:
        mond[x].append("Isolated")
    elif per>=0.25 and per<0.5:
        mond.append("Scattered")
    elif per>=0.5 and per<0.75:
        mond.append("Fairly Widespread")
    else:
        mond.append("Widespread")

#to find monsoon activity
x = 0
for i in rfd.index:
    if rf[i]<0.5*nrf[i]:
        mona.append("Weak Monsoon")
    elif rf[i]>=0.5*nrf[i] and rf[i]<1.5*nrf[i]:
        mona.append("Normal Monsoon")
    elif rf[i]>=1.5*nrf[i] and rf[i]<4*nrf[i]:
        if mond[x]=="Widespread" or mond[x]=="Fairly Widespread":
            if np.count_nonzero(np.array(rfd.loc[i])>30.0)>1:
                mona.append("Active Monsoon")
            else:
                mona.append("Normal Monsoon")
        else:
            mona.append("Normal Monsoon")
    elif rf[i]>=4*nrf[i]:
        if mond[x]=="Widespread":
            if np.count_nonzero(np.array(rfd.loc[i])>50.0)>1:
                mona.append("Vigorous Monsoon")
    x = x+1

#output
monad = p.DataFrame({'Monsoon Distribution':mond,'Monsoon Activity':mona},index =rfd.index)
print(monad)
                            
                        
    

    
    
