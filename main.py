import requests
import json
from bs4 import BeautifulSoup
from xlwt import Workbook 
import os
import csv

def cricbuzz(csvfile):
    
    # ///////////////////     cricket team fetch
    page = requests.get("https://www.cricbuzz.com/cricket-schedule/series")
    soup = BeautifulSoup(page.content, 'html.parser')
    tag_find = soup.select(".text-hvr-underline")
    # //////////////////////  fetch end 
    
    with open(csvfile,'w') as csvfile :
        feildname = ['match']   
        writer = csv.DictWriter(csvfile,feildname)
        writer.writeheader()
        for team in tag_find:
            writer.writerow({'match':team.get_text()})

if __name__ == "__main__":
    print("main function running !")
    
    if os.path.exists('list.csv'):
        print("file exist : >> " + "list.csv")
        os.remove('list.csv')
        cricbuzz("list.csv")
    else:
        cricbuzz("list.csv")
