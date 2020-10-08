import time
import requests
import json
import sys
import getopt


APICEM_IP = "10.74.82.189"
USERNAME = "admin"
PASSWORD = "c1sco@1234"
VERSION = "v1"
MYFolder = "./clientdata/"
device_Folder = "./devicedata/"
mytimeinterval = 30
runcount = 1

def get_X_auth_token(ip,ver,uname,pword):
    # The url for the post ticket API request
    post_url = "https://"+ip+"/dna/system/api/"+ver+"/auth/token"
    #print('get_X_auth_token:%s\n' % ip)
    #print('get_X_auth_token username:%s\n' % uname)
    #print('get_X_auth_token password:%s\n' % pword)
    #print(post_url)
    # All APIC-EM REST API query and response content type is JSON
    headers = {'content-type': 'application/json'}
    # POST request and response
    try:
        requests.packages.urllib3.disable_warnings()
        r = requests.post(post_url, auth=(uname,pword), headers=headers,verify=False)
        # Remove '#' if need to print out response
        #print("get_X_auth_token\n")
        data = r.json()
        #print(data["Token"])
        return data["Token"]
        
    except:
        # Something wrong, cannot get service ticket
        print ("Status: %s"%r.status_code)
        print ("Response: %s"%r.text)
        sys.exit ()

def get_allsiteoverall(ip,ver,uname,pword):
    ticket = get_X_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://"+ip+"/dna/intent/api/v1/site-health"
    print ("\nExecuting get_siteoverall:\n")
    #print(url)
    millis = int(round(time.time() * 1000))
    params={'timestamp':str(millis)}
    try:
    # The request and response of "GET" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.get(url,headers=headers,params=params,verify = False)
        print ("GET '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET get_overallclienthealth")
       sys.exit()

def get_overallclienthealth(ip,ver,uname,pword):
    print('get_overallclienthealth')
    ticket = get_X_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://"+ip+"/dna/intent/api/v1/client-health"
    print ("\nExecuting get_overallclienthealth:\n")
    #print(url)
    millis = int(round(time.time() * 1000))
    params={'timestamp':str(millis)}
    try:
    # The request and response of "GET" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.get(url,headers=headers,params=params,verify = False)
        print ("GET '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET get_overallclienthealth")
       sys.exit()

def get_devicelist(ip,ver,uname,pword):
    print('get_devicelist')
    ticket = get_X_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://"+ip+"/dna/intent/api/v1/network-device"
    #print ("\nExecuting get_devicelist:\n")
    #print(url)
    params={'family':'Unified AP'}
    try:
        # The request and response of "GET" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.get(url,headers=headers,params=params,verify = False)
        print ("GET '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET get_devicelist")
       sys.exit()

def set_dnacrate(ip,ver,uname,pword):
    #print('set_dnacrate')
    ticket = get_X_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://"+ip+"/api/dnacaap/v1/dnacaap/management/ratelimit-default-config"
    #print ("\nExecuting set_dnacrate:\n")
    #print(url)
    data={'rate':200,'windowUnit': 'minute','windowDuration': 1,'maxConcurrentExecutionsPermitted': 0}
    try:
    # The request and response of "POST" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.post(url,data=json.dumps(data),headers=headers,verify = False)
        print ("POST '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET get_devicelist")
       sys.exit()

def get_devicedetailbymacaddr(ip,ver,uname,pword,macaddr):
    #print('devicedetailbymacaddr')
    ticket = get_X_auth_token(ip,ver,uname,pword)
    #headers = {"X-Auth-Token": ticket}
    headers = {'content-type':'application/json','X-Auth-Token':ticket}
    url = "https://"+ip+"/dna/intent/api/v1/device-detail"
    #print ("\nExecuting devicedetailbymacaddr:\n")
    #print(url)
    millis = int(round(time.time() * 1000))
    params={'timestamp':str(millis),'searchBy':macaddr,'identifier':'macAddress'}
    try:
    # The request and response of "GET" request
        requests.packages.urllib3.disable_warnings()
        resp= requests.get(url,headers=headers,params=params,verify = False)
        #print ("GET '%s' Status: "%url,resp.status_code,'\n') # This is the http request status
        return(resp)
    except:
       print ("Something wrong with GET devicedetailbymacaddr")
       sys.exit()

def getdeviceinfo(ip,ver,uname,pword):
    dnac_device = {}
    dnac_device['time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    dnac_aplist=[]
    resp = get_devicelist(ip,ver,uname,pword)
    if (resp.status_code == 200) :
       # Get the json-encoded content from response
       response_json = resp.json()
       #print(json.dumps(response_json,indent=2))
       for siteitem in response_json['response']:
              tmp_device = {}
              tmp_device['macAddress']=siteitem['macAddress']
              tmp_device['platformId']=siteitem['platformId']
              tmp_device['reachabilityStatus']=siteitem['reachabilityStatus']
              tmp_device['hostname']=siteitem['hostname']
              tmp_resp = get_devicedetailbymacaddr(ip,ver,uname,pword,siteitem['macAddress'])
              if (tmp_resp.status_code == 200) :
                   try: 
                      tmp_resp_json = tmp_resp.json()
                      #print('tmp_device json track\n')
                      #print(json.dumps(tmp_resp_json,indent=2))
                      tmp_device['location']=tmp_resp_json['response'].get('location','')
                      tmp_device['overallHealth']=tmp_resp_json['response'].get('overallHealth','0')
                      #tmp_device['location']=tmp_resp_json['response'].['location']
                      #tmp_device['overallHealth']=tmp_resp_json['response']['overallHealth']
                   except:
                      print('tmp_device json track Error\n')
              #print(tmp_device)
              dnac_aplist.append(tmp_device)
              time.sleep(0.5)
       dnac_device['AP'] = dnac_aplist
       #print(json.dumps(dnac_device,indent=2) )
       #write to file
       millis = int(round(time.time() * 1000))
       fielname = device_Folder+'device'+str(millis)+'.json'
       #print(fielname)
       with open(fielname,"w") as f:
          json.dump(dnac_device,f)
          print("write file finish\n")
    else :
       print("get allsiteoverall error code %d" % status)

def getdnacinfo(ip,ver,uname,pword):
    #print('getdnacinfo_IP:%s\n' % ip)
    dnac_dir= {}
    dnac_dir['time']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    #Get Allsite Healt Overall
    resp = get_allsiteoverall(ip,ver,uname,pword)
    status = resp.status_code
    if (status == 200) :
       # Get the json-encoded content from response
       response_json = resp.json()
       #print(json.dumps(response_json,indent=2))
       for siteitem in response_json['response']:
           if (siteitem['siteName'].strip() =='All Sites'):
             try:
                dnac_dir['wirelessDeviceGoodCount']=siteitem.get('wirelessDeviceGoodCount','0')
                dnac_dir['wirelessDeviceTotalCount']=siteitem.get('wirelessDeviceTotalCount','0')
                #dnac_dir['wirelessDeviceGoodCount']=siteitem['wirelessDeviceGoodCount']
                #dnac_dir['wirelessDeviceTotalCount']=siteitem['wirelessDeviceTotalCount']
                #print(dnac_dir)
                break
             except:
                print('siteitem111 track Error\n')
           else :
           	   #print("other row\n")
           	   continue
    else :
       print("get allsiteoverall error code %d" % status)

    #time.sleep(10)
    #Get Overall Client health
    resp = get_overallclienthealth(ip,ver,uname,pword)
    status = resp.status_code
    if (status == 200) :
       # Get the json-encoded content from response
       response_json = resp.json()
       #print(json.dumps(response_json,indent=2))
       for siteitem in response_json['response']:
           if (siteitem['siteId'].strip() =='global'):
              ll_resp=siteitem['scoreDetail']
              for subitem in ll_resp:
                  if (subitem['scoreCategory']['value'] == 'WIRELESS'):
                     try:
                        dnac_dir['wirelessclientCount']=subitem.get('clientCount','0')
                        dnac_dir['wirelessscore']=subitem.get('scoreValue','0')
                        #dnac_dir['wirelessclientCount']=subitem['clientCount']
                        #dnac_dir['wirelessscore']=subitem['scoreValue']
                        #lll_json=subitem['scoreList']
                        lll_json=subitem.get('scoreList','')
                        #print("ttt\n")
                        #print(json.dumps(lll_json,indent=2))
                        for lastitem in lll_json:
                           if (lastitem['scoreCategory']['value'].strip() =='POOR'):
                               dnac_dir['poolclientcount']=lastitem.get('clientCount','0')
                               ttt_json = lastitem.get('scoreList','')
                               #ttt_json = lastitem['scoreList']
                               for  tttitme in ttt_json:
                                   if (tttitme['scoreCategory']['value'].strip() =='OTHER'):
                                       dnac_dir['poorclient_other_count']=tttitme['clientCount']
                                       continue
                                   elif(tttitme['scoreCategory']['value'].strip() =='DHCP'):
                                       dnac_dir['poorclient_dhcp_count']=tttitme['clientCount']
                                       continue
                                   elif(tttitme['scoreCategory']['value'].strip() =='AAA'):
                                       dnac_dir['poorclient_aaa_count']=tttitme['clientCount']
                                       continue
                               continue
                           elif (lastitem['scoreCategory']['value'].strip() =='GOOD'):
                               dnac_dir['goodclientcount']=lastitem['clientCount']
                               continue
                           elif(lastitem['scoreCategory']['value'].strip() =='FAIR'):
                               dnac_dir['fairclientcount']=lastitem['clientCount']
                               continue
                           elif(lastitem['scoreCategory']['value'].strip() =='IDLE'):
                               dnac_dir['idleclientcount']=lastitem['clientCount']
                               continue
                           elif(lastitem['scoreCategory']['value'].strip() =='NODATA'):
                               dnac_dir['nodataclientcount']=lastitem['clientCount']
                               continue
                           elif(lastitem['scoreCategory']['value'].strip() =='NEW'):
                               dnac_dir['newclientclientcount']=lastitem['clientCount']
                               continue
                           else:
                              continue
                        #print(dnac_dir)
                        break
                     except:
                         print('siteitem222 track Error\n')
                  else:
                   	  print("other Client type\n")
                   	  continue
              break
           else :
              print("other row\n")
              continue
       #write to file
       millis = int(round(time.time() * 1000))
       fielname = MYFolder+'client'+str(millis)+'.json'
       #print(fielname)
       with open(fielname,"w") as f:
          json.dump(dnac_dir,f)
          print("write file finish\n")
    else :
       print("get get_overallclienthealth error code %d" % status)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "hu:p:i:t:c:", ["help", "username=", "password=","ip=","timeinterval=","runcount="])
  except getopt.GetoptError:
    print('Error: test_arg.py -u <username> -p <password> -i <ip address> -t <timeinterval> -c <runcount>')
    print('ERRor: test_arg.py--username=<username> --password=<password> --ip <ip address> --timer <timeinterval> --count <runcount>')
    sys.exit(2)


  m_APICEM_IP = APICEM_IP
  m_USERNAME = USERNAME
  m_PASSWORD = PASSWORD

  #处理 返回值options是以元组为元素的列表。
  for opt, arg in opts:
        if opt in ("-h", "--help"):
            print('test_arg.py -u <username> -p <password> -i <ip address> -t <timeinterval> -c <runcount>')
            print('or: test_arg.py --username=<username> --password=<password> --ip <ip address> --timer <timeinterval> --count <runcount>')
            sys.exit()
        elif opt in ("-u", "--username"):
            m_USERNAME = arg
        elif opt in ("-p", "--password"):
            m_PASSWORD = arg
        elif opt in ("-i", "--ip"):
            m_APICEM_IP = arg
        elif opt in ("-t", "--timer"):
            mytimeinterval = int(arg)
        elif opt in ("-c", "--count"):
            runcount = int(arg)
  print('username:%s \n' % m_USERNAME)
  print('password:%s \n' % m_PASSWORD)
  print('IP Address:%s \n' % m_APICEM_IP)
  print('Time Inteval:%d \n' % mytimeinterval)
  print('runcount:%d \n' % runcount)
  #getdnacinfo()
  set_dnacrate(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
  if (runcount == 0) :
     print('Run forever\n')
     while True:
        getdnacinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
        time.sleep(1)
        getdeviceinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
        time.sleep(mytimeinterval*60)
  else :
     while (runcount > 0) :
       getdnacinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
       getdeviceinfo(m_APICEM_IP,VERSION,m_USERNAME,m_PASSWORD)
       runcount = runcount -1
       if (runcount == 0):
          print('Run finish and exit\n')
          sys.exit(2)
       else:
          time.sleep(mytimeinterval*60)

if __name__ == "__main__":
    # sys.argv[1:]为要处理的参数列表，sys.argv[0]为脚本名，所以用sys.argv[1:]过滤掉脚本名。
    print(sys.argv)
    main(sys.argv[1:])
