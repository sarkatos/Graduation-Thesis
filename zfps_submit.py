#!/usr/bin/env python3

import requests
import json

# Script name: zfps_submit.py
def submit_post(ra_list,dec_list):

  ra = json.dumps(ra_list)
  dec = json.dumps(dec_list)
  '''
  jds = 2458000.5         # start JD for all input target positions.
  jdstart = json.dumps(jds)
  print(jdstart)

  jde = 2460100.5         # end JD for all input target positions.
  jdend = json.dumps(jde)
  print(jdend)
  '''

  email = '00324610@ufrgs.br'     # email you subscribed with.
  userpass = 'rxfb361'                    # password that was issued to you.


  payload = {'ra': ra, 'dec': dec,
             'email': email, 'userpass': userpass}

  # fixed IP address/URL where requests are submitted:
  url = 'https://ztfweb.ipac.caltech.edu/cgi-bin/batchfp.py/submit'
  r = requests.post(url,auth=('ztffps', 'dontgocrazy!'), data=payload)
  print("Status_code=",r.status_code)

#--------------------------------------------------
# Main calling program. 

with open('ra_dec_10_SN_20.txt') as f: # mudar nome do documento com as coordenadas aqui
    lines_zero = f.readlines()
f.close()

print("Number of (ra,dec) pairs =", len(lines_zero))
if len(lines_zero) > 1500:
    begining = 0
    ending = 1499
    flag = 0
    while flag == 0:
        if ending == len(lines_zero):
            flag = 1
        lines = lines_zero[begining:ending]
        ralist = []
        declist = []
        i = 0
        for line in lines:
            x = line.split()
            radbl = float(x[0])
            decdbl = float(x[1])

            raval = float('%.7f'%(radbl))
            decval = float('%.7f'%(decdbl))

            ralist.append(raval)
            declist.append(decval)

            i = i + 1
            rem = i % 1500 # Limit submission to 1500 sky positions.

            if rem == 0:
                submit_post(ralist,declist)
                ralist = []
                declist = []

        if len(ralist) > 0:
            submit_post(ralist,declist)
        begining = begining + 1500
        ending = ending + 1500
        if ending > len(lines_zero):
            ending = len(lines_zero)
else:
    lines = lines_zero
    ralist = []
    declist = []
    i = 0
    for line in lines:
        x = line.split()
        radbl = float(x[0])
        decdbl = float(x[1])

        raval = float('%.7f'%(radbl))
        decval = float('%.7f'%(decdbl))

        ralist.append(raval)
        declist.append(decval)

        i = i + 1
        rem = i % 1500 # Limit submission to 1500 sky positions.

        if rem == 0:
            submit_post(ralist,declist)
            ralist = []
            declist = []

    if len(ralist) > 0:
        submit_post(ralist,declist)

exit(0)