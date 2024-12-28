import requests
from datetime import datetime


date = datetime.now().strftime("%d-%m-%Y")
api = "https://api.aladhan.com"

res = requests.get("%s/v1/timings/%s?latitude=36.73626208158312&longitude=3.107711630740893" % (api,date))
data = res.json()
timings = data["data"]["timings"]


def print_timings():
     print("إِنَّ الصَّلَاةَ كَانَتْ عَلَى الْمُؤْمِنِينَ كِتَابًا مَوْقُوتًا")
     print(datetime.now().ctime())
     for time in timings.keys():
          print("%s : %s" % (time,timings[time]))  
     
print_timings()
