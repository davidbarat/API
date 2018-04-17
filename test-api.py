import json
import re
import base64
import configparser
import requests
import datetime
import pprint
import pandas as pd
import matplotlib.pyplot as plt
from enum import Enum
from time import sleep
from json import loads

palette = plt.cm.spring

config = configparser.ConfigParser()
config.read('config.cfg')
if config['DEFAULT']:
    TOKEN = config['DEFAULT']['TOKEN']
    urlAPI = config['DEFAULT']['urlAPI']
else:
   print("EXIT: erreur de configuration")
   exit(255)

#print('https://' + TOKEN + '@' + urlAPI + iti2 )
#print('https://' + urlAPI + ' -u ' + TOKEN + ':')
#f={}
#f = requests.get('https://' + TOKEN + '@' + urlAPI )
f = requests.get('https://' + urlAPI, auth=(TOKEN,''))

res = f.json()
#print.pprint(res)

#print(f["journeys"])
depart_dic = {}
destination_dic = {}
for date in res['journeys']:
    
	#date['test'] = date['distances']['car']
    #date['test'] = date['sections']['from']['administrative_region']['insee']
    #arrive_dic['href'] = date['links'][0]['href']
    depart_dic['from'] = date['sections'][0]['from']['administrative_region']['name']
    depart_dic['insee'] = date['sections'][0]['from']['administrative_region']['insee']
    depart_dic['heure_depart'] = date['departure_date_time']
    depart_dic['duree'] = date['durations']['total']/60
    depart_dic['lat'] = date['sections'][0]['from']['administrative_region']['coord']['lat']
    depart_dic['lon'] = date['sections'][0]['from']['administrative_region']['coord']['lon']
    depart_dic['co2'] = date['co2_emission']['value']

    destination_dic['to'] = date['sections'][2]['from']['stop_point']['administrative_regions'][0]['name']
    destination_dic['insee'] = date['sections'][2]['from']['stop_point']['administrative_regions'][0]['insee']
    destination_dic['heure_arrivee'] = date['arrival_date_time']
    destination_dic['lat'] = date['sections'][2]['from']['stop_point']['administrative_regions'][0]['coord']['lat']
    destination_dic['lon'] = date['sections'][2]['from']['stop_point']['administrative_regions'][0]['coord']['lon']
    

print(depart_dic)
print(destination_dic)

coord_lat = [float(destination_dic['lat']), float(depart_dic['lat'])]
coord_lon = [float(destination_dic['lon']), float(depart_dic['lon'])]

print(coord_lon + coord_lat)


plt.scatter(coord_lon , coord_lat, marker = "o", c = 'blue')
plt.plot(coord_lon , coord_lat, color = 'red', linestyle = 'solid')
plt.title('Trajet ' + depart_dic['from'] + ' vers ' + destination_dic['to'] )

#x = [1, 2, 3, 4, 5]
#y1 = [1, 2, 3, 4, 5]
#y2 = [1, 4, 9, 16, 25]
#y3 = [25, 16, 9, 4, 1]
#plt.scatter(x, y1, s = 130, c = 'yellow', marker = '*', edgecolors = 'green')
#plt.scatter(x, y2, s = 50, c = 'red', marker = '+', linewidth = 3)
#plt.scatter(x, y3, s = 50, c = 'cyan', marker = 'o', edgecolors = 'none')

#for info_trajet in f["journeys"]:
#	print(f.values())
    #gare_arrivee['name'] = info_trajet['stop_point']

#print (gare_arrivee)

#heure_depart [] = departure_date_time



#data = json.dumps(slf)
#js = json.load("f")

#print(json_to_python)

#{ d["tickets"] for d in loads('slf') }
