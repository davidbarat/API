import jsonimport reimport base64import configparserimport requestsimport datetimeimport pandas as pdfrom enum import Enumfrom time import sleepfrom json import loads
config = configparser.ConfigParser()config.read('config.cfg')if config['DEFAULT']:    TOKEN = config['DEFAULT']['TOKEN']    urlAPI = config['DEFAULT']['urlAPI']else:   print("EXIT: erreur de configuration")   exit(255)
#print('https://' + TOKEN + '@' + urlAPI + iti2 )#print('https://' + urlAPI + ' -u ' + TOKEN + ':')#f={}#f = requests.get('https://' + TOKEN + '@' + urlAPI )f = requests.get('https://' + urlAPI, auth=(TOKEN,''))
res = f.json()#print(f)
#print(f["journeys"])new_dic ={}for date in res['journeys']:     #date['test'] = date['distances']['car']    #date['test'] = date['sections']['from']['administrative_region']['insee']    #new_dic['href'] = date['links'][0]['href']    new_dic['from'] = date['sections'][0]['from']['administrative_region']['name']    new_dic['insee'] = date['sections'][0]['from']['administrative_region']['insee']    new_dic['heure_depart'] = date['departure_date_time']    new_dic['heure_arrivee'] = date['arrival_date_time']    new_dic['duree'] = date['durations']['total']/60    new_dic['lat'] = date['sections'][0]['from']['administrative_region']['coord']['lat']    new_dic['lon'] = date['sections'][0]['from']['administrative_region']['coord']['lon']    new_dic['co2'] = date['co2_emission']['value']
print(new_dic)
#for info_trajet in f["journeys"]:# print(f.values())    #gare_arrivee['name'] = info_trajet['stop_point']
#print (gare_arrivee)
#heure_depart [] = departure_date_time

#data = json.dumps(slf)#js = json.load("f")
#print(json_to_python)
#{ d["tickets"] for d in loads('slf') }
