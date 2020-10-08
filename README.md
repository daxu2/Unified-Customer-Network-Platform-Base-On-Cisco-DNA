# Unified-customer-oriented-localized-Enterprise-Network-Management-Platform-Base-on-Cisco-DNA-Solution Demo Code
Technology Summary :

1.Unified &amp; Customer-oriented &amp; localized Enterprise  Network Management Platform Base on Cisco DNA Solution,Monitor network every where，any time,and provide automaticly report  
2.3rd party switch integrate 
3.Customer-oriented Protal,not only IT view,but also need OT and Management Team view  
4.Notification and Integrate With WeChat and Webex Team,Real time notification Integrating customer workflow 
5.Self Service Integrate With WeChat and customer mobile app,Provide more self-service  for OT within workflow ,more automatic,more flexible IT Operation 
6.DNA Assurance Portal Localization

Business Summary:

1.Win &amp; Win &amp; Win:Cisco Win the Case,Partner Wim more Project,Customer IT win Trust from Management Team 
2.This is not only an Idea,it is real case/product, Total Booking Number：1M+ US$ 
3.Cisco Value Selling:Cross Archi Selling,From IT to OT,Focus on customer business value and solve really issue 
4.Partner Tranformation:From product selling to solution selling,More closely with customer core business,Partner develop skill Use case description  

How to Use Demo Code：

1.DNAC-intergrate-Huawei5720.zip :--- This is Sample code for using DNAC southbound SDK to intergarte Huawei S5720 Switch in to DNAC platform,you must install DNAC southbound SDK tools first,then unzip file and load all file into SDK application and compile it,and install the .sdu file in to you DNAC.

2.assurnace_haixin.py :--- This is a Saple code using Python,this code is get data from DNAC and can be display on Splunk,you can using follow command to run the code python3 assurnace_haixin.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.

3.dnabot_xuda.js :--- this is Demo code for using Webex Team Bot to intergrate with DNAC,you can using /hello，/getdevicecount，/getsiteinfo,  /testmyclient command on you webex Team Bot to get the infomation from DNAC,this code is using JS.Node,you also need to install ngrok and npm first.

4.WeChat_Dev.zip :--- This is Demo for How intergrate DNAC request in Wechat, you should install Wechat develop Tools first and using this tool to compile the code and publish in WeChat.

