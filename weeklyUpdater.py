#import all needed libraries
import shutil
import pandas as pd
import os
import subprocess

DATA_SOURCE = "C:\\Users\\Avery\\OneDrive\\Desktop\\CS2 Project\\Data"
DATA_DESTINATION = "C:\\Users\\Avery\\OneDrive\\Desktop\\HardWareWebsite"

# --- CONFIGURATION ---
# Git commit message
COMMIT_MESSAGE = 'Auto: Weekly update of data'


#copy over spreadsheets
def copyXLSX():
    shutil.copy(src= DATA_SOURCE + "\\Main.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CounterStrike2.xlsx")
    shutil.copy(src= DATA_SOURCE + "\\Bans.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\PremierBans.xlsx")
    shutil.copy(src= DATA_SOURCE + "\\Faceit.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CSFaceit.xlsx")
    shutil.copy(src= DATA_SOURCE + "\\premap.xlsx", dst=DATA_DESTINATION + "\\Datasets\\xlsx\\CSPreMatchStatistics.xlsx")

#convert over to CSV
#eh, freak it. having the zip file was nice. can python do that for me or do i need to sob myself to sleep.
def copyCSV():
    pd.read_excel(DATA_SOURCE + "\\Main.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\main.csv", index=None, header=True)
    pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="FirstBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\firstBan.csv", index=None, header=True)
    pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="SecondBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\secondBan.csv", index=None, header=True)
    pd.read_excel(DATA_SOURCE + "\\Bans.xlsx", sheet_name="ThirdBan").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CounterStrike2\\thirdBan.csv", index=None, header=True)
    pd.read_excel(DATA_SOURCE + "\\Faceit.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CSFaceit.csv", index=None, header=True)
    pd.read_excel(DATA_SOURCE + "\\premap.xlsx").to_csv(DATA_DESTINATION + "\\Datasets\\csv\\CSPreMatchStatistics.csv", index=None, header=True)

def run_git_commands(repo_dir, commit_msg):
    """Run git add, commit, and push."""
    try:
        subprocess.run(['git', 'pull', 'origin', 'main'], cwd=repo_dir, check=True)
        subprocess.run(['git', 'add', '.'], cwd=repo_dir, check=True)
        subprocess.run(['git', 'commit', '-m', commit_msg], cwd=repo_dir, check=True)
        subprocess.run(['git', 'push'], cwd=repo_dir, check=True)
        print("Changes pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")

def main():
    copyXLSX()
    copyCSV()
    run_git_commands(DATA_DESTINATION, COMMIT_MESSAGE)

main()
x = input("Update was successful. You can close this command prompt now.")