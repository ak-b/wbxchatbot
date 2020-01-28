import requests
from orionsdk import SwisClient
import re
from wibot.utils import get_config 

configs = get_config()

SOLARWINDS_URL = configs['SOLARWINDS_URL']
SOLARWINDS_USERNAME = configs['SOLARWINDS_USERNAME']
SOLARWINDS_PASSWORD = configs['SOLARWINDS_PASSWORD']

verify = False
if not verify:
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def cpuwatch(threshold):
  th = int(threshold)
  swis = SwisClient(SOLARWINDS_URL, SOLARWINDS_USERNAME, SOLARWINDS_PASSWORD)
  query="""
     SELECT N.Caption, N.CPULoad, MAX(N.CPULoadHistory.MaxLoad) AS MaxLoad
     FROM Orion.Nodes N
     WHERE N.CPULoadHistory.DateTime > ADDHOUR(-24, GETUTCDATE())
     GROUP BY N.Caption, N.CPULoad
     ORDER BY N.CPULoad DESC
  """
  results = swis.query(query)
  devices = []
  counter = 0
  for row in results['results']:
      if re.search('asa',row['Caption']) or re.search('ftd',row['Caption']) or re.search('fpr',row['Caption']):
        if row['MaxLoad'] > th:
          counter = counter+1
          devices.append(row['Caption'])

  if counter == 0:
    print("Device CPU has not crossed {}% in the past 24 hrs".format(threshold))
  else:
    print("FWs where CPU crossed {}% in the past 24hrs".format(threshold))
    print("===========================================")
    for row in devices:
      print(row)
            