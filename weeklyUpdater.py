#import all needed libraries
import shutil
import pandas as pd
DATA_SOURCE = "C:\\Users\\Avery\\OneDrive\\Desktop\\CS2 Project\\Data"
DATA_DESTINATION = "C:\\Users\\Avery\\OneDrive\\Desktop\\HardWareWebsite"

#copy over spreadsheets
shutil.copy(src= DATA_SOURCE + "\\Main.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CounterStrike2.xlsx")
shutil.copy(src= DATA_SOURCE + "\\Bans.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\PremierBans.xlsx")
shutil.copy(src= DATA_SOURCE + "\\Faceit.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CSFaceit.xlsx")
shutil.copy(src= DATA_SOURCE + "\\premap.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CSPreMatchStatistics.xlsx")

#convert over to CSV
#eh, freak it. having the zip file was nice. can python do that for me or do i need to sob myself to sleep.
pd.read_excel(DATA_SOURCE + "\\Main.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\main.csv", index=None, header=True)
pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="FirstBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\firstBan.csv", index=None, header=True)
pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="SecondBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\secondBan.csv", index=None, header=True)
pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="ThirdBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\thirdBan.csv", index=None, header=True)
pd.read_excel(DATA_SOURCE + "\\Faceit.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CSFaceit.csv", index=None, header=True)
pd.read_excel(DATA_SOURCE + "\\premap.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CSPreMatchStatistics.csv", index=None, header=True)