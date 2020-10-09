# Unified customer oriented localized Enterprise Network Management Platform Base on Cisco DNA Solution Demo Code
   Cisco have stronger competitors such as Huawei, H3C and Aruba in China market. Most of customers have multi-vendor deployment in their campus network. And customers also want to have single plane to manage all network devices.
   Second is most of customers have requirements on network visibility, customization, localization, personalization to meet their business support。
   Third is IT operations need to provide more innovative services, integrate network management and service within company workflow and customer private apps.
   This is a expamle code using DNAC platform Southbound SDK to provide capability to integrate third party’s devices，Cisco DNA will be the unified management platform. We also Using Northbound SDK to provide network visibility  customization, localization, personalization，notification. and integrate with third party’s applicationfor using DNA southbound SDK and northbound API.

Pro tips:

    Code Exchange displays the first few content lines of your README in the tile it creates for your repo. If you enter a GitHub Description, Code Exchange uses that instead.
    Code Exchange works best with READMEs formatted in GitHub's flavor of Markdown. Support for reStructuredText is a work in progress.

Other things you might include:

    Technology stack: This Example Code is composed with 4 moduel,every moduel is can be used independently.   
1.DNAC-intergrate-Huawei5720.zip :--- This is Sample code for using DNAC southbound SDK to intergarte Huawei S5720 Switch in to DNAC platform,you must install DNAC southbound SDK tools first,then unzip file and load all file into SDK application and compile it,and install the .sdu file in to you DNAC.

2.assurnace_haixin.py :--- This is a Saple code using Python,this code is get data from DNAC and can be display on Splunk,you can using follow command to run the code python3 assurnace_haixin.py -u admin -p Cisc0123 -i 172.16.63.248 -t 1 -c 1, 'admin is DNAC username,'Cisc0123' is DNAC password,'172.16.63.248' is DNAC IP address, -t is mean how many minute to get data from dnac once,'-c' is mean how many time you want to retrieve data from DNAC,if =0 mean,this will run for ever.

3.dnabot_xuda.js :--- this is Demo code for using Webex Team Bot to intergrate with DNAC,you can using /hello，/getdevicecount，/getsiteinfo,  /testmyclient command on you webex Team Bot to get the infomation from DNAC,this code is using JS.Node,you also need to install ngrok and npm first.

4.WeChat_Dev.zip :--- This is Demo for How intergrate DNAC request in Wechat, you should install Wechat develop Tools first and using this tool to compile the code and publish in WeChat.
    Status:  Beta. It's OK to write a sentence, too. The goal is to let interested people know where what they can expect from this code.
    Screenshot: If the code has visual components, place a screenshot after the description; e.g.,

add-image-here
Use Case Description

Describe the problem this code addresses, how your code solves the problem, challenges you had to overcome as part of the solution, and optional ideas you have in mind that could further extend your solution.
Installation

Detailed instructions on how to install, configure, and get the project running. Call out any dependencies. This should be frequently tested and updated to make sure it works reliably, accounts for updated versions of dependencies, etc.
Configuration

If the code is configurable, describe it in detail, either here or in other documentation that you reference.
Usage

Show users how to use the code. Be specific. Use appropriate formatting when showing code snippets or command line output.
DevNet Sandbox

A great way to make your repo easy for others to use is to provide a link to a DevNet Sandbox that provides a network or other resources required to use this code. In addition to identifying an appropriate sandbox, be sure to provide instructions and any configuration necessary to run your code with the sandbox.
How to test the software

Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. If the repo includes automated tests, detail how to run those tests. If the repo is instrumented with a continuous testing framework, that is even better.
Known issues

Document any significant shortcomings with the code. If using GitHub Issues to track issues, make that known and provide any templates or conventions to be followed when opening a new issue.
Getting help

Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

Example

If you have questions, concerns, bug reports, etc., please create an issue against this repository.
Getting involved

This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on how to contribute should be stated with a link to CONTRIBUTING file.
Credits and references

    Projects that inspired you
    Related projects
    Books, papers, talks, or other sources that have meaningful impact or influence on this code

Licensing info

A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to Code Exchange or Automation Exchange requires a commitment to maintain the code and help the community use and contribute to the code.

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc. This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

    Cisco employees can find licensing options and guidance here.

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on Add a license and select from a set of OSI approved open source licenses. See detailed instructions.

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select Create New File, type LICENSE into the filename box, and you will be given the option to select from a set of common open source licenses. See detailed instructions.

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the 3-Clause BSD license template has the following copyright notice:

Copyright (c) <YEAR>, <COPYRIGHT HOLDER>

See the LICENSE for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See LICENSE for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the LICENSE itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see NOTICE.

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see https://github.com/cisco/ChezScheme/blob/master/NOTICE.
Best practices

Information below can help you make your repo meet our requirements and be more useful to others.
Good practices

    Manage sensitive data for scripts. For example, store passwords/API keys and other sensitive data in env.py or parse it as arguments. In Python, you can use ConfigParser for applications and programs: encrypt sensitive data in your database.
    Include in Installation section how to run your script for different OS like Windows/macOS/Linux
    Print usage if you run script or program without any input data (support -h -help flags)
    Catch an error and print useful information in console and interface
    Add error management to handle if users miss some parameters or add them in the wrong format
    Add links for resources where users can test code/app. For example, add links DevNet sandboxs (Always-on or reservable). You can find a list of all available sandboxes here https://devnetsandbox.cisco.com/RM/Topology
    Add links where users can download and how to install additional soft/app/libraries that are needed to run your code. For example, installer for Python, node, etc.
    Add NOTICE file with copyright if you use GPLv3 or Apache 2.0 license (sample)
    Dockerize app or part of an app, like a server/client

Bad practices

    Use bad quality screenshots
    Users need to rename some files like variables_template.py
    Users need to include credentials in source file
    Don’t describe in which format users need to type or paste in file API endpoint or server IP. For example, sometimes devs write in code api_endpoint = “https://" + IP +"/", such that users need to paste the IP only without a slash at the end or a protocol specification. Please clarify this information in README.


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

