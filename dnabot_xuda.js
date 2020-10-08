//
// Copyright (c) 2016 Cisco Systems
// Licensed under the MIT License 
//

/* 
 * a Webex Teams bot that:
 *   - sends a welcome message as he joins a room, 
 *   - answers to a /hello command, and greets the user that chatted him
 *   - supports /help and a 'fallback' helper message
 *
 * + leverages the "node-sparkclient" library for bot to Webex communications.
 * 
 */

const WebexChatBot = require("node-sparkbot");
const bot = new WebexChatBot();

// Remove comment to overload default '/' prefix to identify bot commands
//bot.interpreter.prefix = "#"; 

const SparkAPIWrapper = require("node-sparkclient");
if (!process.env.ACCESS_TOKEN) {
    console.log("Could not start as this bot requires a Webex Teams API access token.");
    console.log("Please add env variable ACCESS_TOKEN on the command line");
    console.log("Example: ");
    console.log("> ACCESS_TOKEN=XXXXXXXXXXXX DEBUG=sparkbot* node helloworld.js");
    process.exit(1);
}
const client = new SparkAPIWrapper(process.env.ACCESS_TOKEN);





//
// Help and fallback commands
//
bot.onCommand("help", function (command) {
    client.createMessage(command.message.roomId, "Hi, I am the Hello World bot !\n\nType /hello to see me in action.", { "markdown":true }, function(err, message) {
        if (err) {
            console.log("WARNING: could not post message to room: " + command.message.roomId);
            return;
        }
    });
});
bot.onCommand("fallback", function (command) {
    client.createMessage(command.message.roomId, "Sorry, I did not understand.\n\nTry /help.", { "markdown":true }, function(err, response) {
        if (err) {
            console.log("WARNING: could not post Fallback message to room: " + command.message.roomId);
            return;
        }
    });
});


//
// Bots commands here
//
bot.onCommand("hello", function (command) {
    let email = command.message.personEmail; // User that created the message orginally 
    client.createMessage(command.message.roomId, `Hello, your email is: **${email}**`, { "markdown":true }, function(err, message) {
        if (err) {
            console.log("WARNING: could not post message to room: " + command.message.roomId);
            return;
        }
    });
});


// Bots commands here
//
bot.onCommand("getdevicecount", function (command) {
    let email = command.message.personEmail; // User that created the message orginally 
    //get DNAC token
    var request = require('request');
    var options = {
    uri: 'https://10.74.82.189/dna/system/api/v1/auth/token',
    method: 'POST',
    rejectUnauthorized : false,
    strictSSL : false,
    headers: {
        'content-type': 'application/json',
        'Authorization': 'Basic ' + new Buffer('admin' + ':' + 'c1sco@1234').toString('base64')
     }
    };

   var dnac_token ='';
   request(options, function (error, response, data) {
      console.log(error);
      console.log(response.statusCode);
      if (!error && response.statusCode == 200) {
         dnac_token = JSON.parse(data)['Token']
         console.log(dnac_token) // Print the shortened url.
         //get DNAC device count
         var options = {
             uri: 'https://10.74.82.189/dna/intent/api/v1/network-device/count',
             method: 'GET',
             rejectUnauthorized : false,
             strictSSL : false,
             headers: {
               'content-type': 'application/json',
               'X-Auth-Token': dnac_token
             }
         };

        console.log('111');
        var device_cnt = '';
        request(options, function (error, response, data) {
          console.log(error);
          console.log(response.statusCode);
          if (!error && response.statusCode == 200) {
             device_cnt = JSON.parse(data)['response'].toString();
             console.log(device_cnt) // Print the shortened url.
             client.createMessage(command.message.roomId, `DNAC设备数量总数为(DNAC Device Count): **${device_cnt}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
          }
      });
  }
});
    //client.createMessage(command.message.roomId, `Hello, your email is: **${email}**`, { "markdown":true }, function(err, message) {
      //  if (err) {
        //   console.log("WARNING: could not post message to room: " + command.message.roomId);
          //  return;
        //}
    //});
});



// Bots commands here
//
bot.onCommand("getsiteinfo", function (command) {
    let email = command.message.personEmail; // User that created the message orginally 
    //get DNAC token
    var request = require('request');
    var options = {
    uri: 'https://10.74.82.189/dna/system/api/v1/auth/token',
    method: 'POST',
    rejectUnauthorized : false,
    strictSSL : false,
    headers: {
        'content-type': 'application/json',
        'Authorization': 'Basic ' + new Buffer('admin' + ':' + 'c1sco@1234').toString('base64')
     }
    };

   var dnac_token ='';
   request(options, function (error, response, data) {
      console.log(error);
      console.log(response.statusCode);
      if (!error && response.statusCode == 200) {
         dnac_token = JSON.parse(data)['Token']
         console.log(dnac_token) // Print the shortened url.
         //get DNAC device count
         var options = {
             uri: 'https://10.74.82.189/dna/intent/api/v1/site-health',
             method: 'GET',
             rejectUnauthorized : false,
             strictSSL : false,
             headers: {
               'content-type': 'application/json',
               'X-Auth-Token': dnac_token
             }
         };

        //console.log('111');
        var networkHealthAverage = '';
        var networkHealthAccess = '';
        var networkHealthRouter = '';
        var networkHealthDistribution = '';
        var networkHealthWireless = '';
        var numberOfClients = '';
        request(options, function (error, response, data) {
          console.log(error);
          console.log(response.statusCode);
          if (!error && response.statusCode == 200) {
             networkHealthAverage = JSON.parse(data)['response'][0]['networkHealthAverage'].toString();
             networkHealthAccess = JSON.parse(data)['response'][0]['networkHealthAccess'].toString();
             networkHealthRouter = JSON.parse(data)['response'][0]['networkHealthRouter'].toString();
             networkHealthDistribution = JSON.parse(data)['response'][0]['networkHealthDistribution'].toString();
             networkHealthWireless = JSON.parse(data)['response'][0]['networkHealthWireless'].toString();
             numberOfClients = JSON.parse(data)['response'][0]['numberOfClients'].toString();
             console.log(networkHealthAverage) // Print the shortened url.
             console.log(networkHealthAccess) // Print the shortened url.
             console.log(networkHealthRouter) // Print the shortened url.
             console.log(networkHealthDistribution) // Print the shortened url.
             console.log(networkHealthWireless) // Print the shortened url.
             console.log(numberOfClients) // Print the shortened url.
             client.createMessage(command.message.roomId, `DNAC Site设备平均健康值(DNAC Site Device Average Health Score): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
             client.createMessage(command.message.roomId, `DNAC Site接入设备平均健康值(DNAC Site Access Device Average Health Score): **${networkHealthAccess}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
             client.createMessage(command.message.roomId, `DNAC Site路由设备平均健康值(DNAC Site Router Device Average Health Score): **${networkHealthRouter}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
             client.createMessage(command.message.roomId, `DNAC Site汇聚设备平均健康值(DNAC Site Distribution Device Average Health Score): **${networkHealthDistribution}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
             client.createMessage(command.message.roomId, `DNAC Site无线设备平均健康值(DNAC Site Wireless Device Average Health Score): **${networkHealthWireless}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
             client.createMessage(command.message.roomId, `DNAC Site在线用户数量（login client count）: **${numberOfClients}**`, { "markdown":true }, function(err, message) {
             if (err) {
                console.log("WARNING: could not post message to room: " + command.message.roomId);
                return;
             }
             });
          }
      });
  }
});
    //client.createMessage(command.message.roomId, `Hello, your email is: **${email}**`, { "markdown":true }, function(err, message) {
      //  if (err) {
        //   console.log("WARNING: could not post message to room: " + command.message.roomId);
          //  return;
        //}
    //});
});


// Bots commands here
//
bot.onCommand("testmyclient", function (command) {
    
    var networkHealthAverage = '10';
    client.createMessage(command.message.roomId, `你的客户端健康分值（you client health score）: **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = 'AP-23F-1905';
    client.createMessage(command.message.roomId, `你的客户端连接的AP名字(AP name for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = 'Shanghai/Dawning Tower/Floor 23';
    client.createMessage(command.message.roomId, `你的客户端连接的AP的位置(AP site for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = '10';
    client.createMessage(command.message.roomId, `你的客户端连接的AP设备健康值(AP health score for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });


    var networkHealthAverage = 'DNAC-Test';
    client.createMessage(command.message.roomId, `你的客户端连接的SSID名字(SSID Name for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });

    var networkHealthAverage = '802.11ac';
    client.createMessage(command.message.roomId, `你的客户端连接的协议(protocol for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });

    var networkHealthAverage = '5G';
    client.createMessage(command.message.roomId, `你的客户端连接的信道(band for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = '20';
    client.createMessage(command.message.roomId, `你的客户端连接的频道带宽(channel width for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = '1ms';
    client.createMessage(command.message.roomId, `你的客户端连接的登陆时间(onboarding time for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = '30.0';
    client.createMessage(command.message.roomId, `你的客户端信噪比(SNR for you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });
    var networkHealthAverage = '-62.0';
    client.createMessage(command.message.roomId, `你的客户端信号强度(rssi you client connected): **${networkHealthAverage}**`, { "markdown":true }, function(err, message) {
    if (err) {
       console.log("WARNING: could not post message to room: " + command.message.roomId);
       return;
     }
     });

});

//
// Welcome message 
// sent as the bot is added to a Room
//
bot.onEvent("memberships", "created", function (trigger) {
    let newMembership = trigger.data; // see specs here: https://developer.webex.com/endpoint-memberships-get.html
    if (newMembership.personId != bot.interpreter.person.id) {
        // ignoring
        console.log("new membership fired, but it is not us being added to a room. Ignoring...");
        return;
    }

    // so happy to join
    console.log("bot's just added to room: " + trigger.data.roomId);
    
    client.createMessage(trigger.data.roomId, "Hi, I am the Hello World bot !\n\nType /hello to see me in action.", { "markdown":true }, function(err, message) {
        if (err) {
            console.log("WARNING: could not post Hello message to room: " + trigger.data.roomId);
            return;
        }

        if (message.roomType == "group") {
            client.createMessage(trigger.data.roomId, "**Note that this is a 'Group' room. I will wake up only when mentionned.**", { "markdown":true }, function(err, message) {
                if (err) {
                    console.log("WARNING: could not post Mention message to room: " + trigger.data.roomId);
                    return;
                }
            });
        }      
    }); 
});

