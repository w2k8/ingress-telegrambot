## Ingress Telegrambot
## Usage
## installation

# ingress telegrambot

This is a simple telegram bot for ingress agents who wants to save there stats in a database

It can recieve and send stats from multiple ingress agents.
The telegram userid will be used to seperate the agents. 
So dont send multiple agent stats with 1 telegram account, that will give you strange results when you ask the bot for the agent stats.

You dont need to create a database, the script will create the data if needed.
If ingress change the game in anyway, so that the agent stats aren't what this script expect, the script will crash.
If i have time, i will fix this as soon as possible. (as long as i play ingress)
Change the database by hand if you dont want to lose youre stats.

Tested and used with a Raspberry Pi 2, with debian as OS.

The bot can reply on some simple commands.


/stats - This returns some graphs from the agent
![First image of Graph user stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName-1.png)
![Second image of Graph user stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName-2.png)
![Third image of Graph user stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName-3.png)

/test - this returns a simple graph from the agent
![Image of Graph user stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName-3.png)

/test1 - this returns a new graph from the agent
![Image of combined user stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/Figure_4.png)

# Usage

Copy the agent stats from ingress and past it into telegram, so that you send the data to youre bot.

![Agent stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName.png)


And you should recieve a message like this:
```
Agent stats:
Time Span - ALL TIME
Agent Name - AgentName
Agent Faction - Resistance
Date - 2020-07-21
Time - 20:01:28
Level - 9
Lifetime AP - 42744461
Current AP - 2725841
Unique Portals Visited - 2586
Unique Portals Drone Visited - 16
Furthest Drone Flight Distance - 1
Portals Discovered - 115
XM Collected - 123363070
OPR Agreements - 1084
Portal Scans Uploaded - 81
Scout Controller on Unique Portals - 14
Distance Walked - 1532
Resonators Deployed - 67866
Links Created - 14942
Control Fields Created - 8867
Mind Units Captured - 849377
Longest Link Ever Created - 19
Largest Control Field - 22313
XM Recharged - 74174676
Portals Captured - 8608
Unique Portals Captured - 1992
Mods Deployed - 10279
Resonators Destroyed - 38907
Portals Neutralized - 6593
Enemy Links Destroyed - 6340
Enemy Fields Destroyed - 3220
Max Time Portal Held - 479
Max Time Link Maintained - 203
Max Link Length x Days - 801
Max Time Field Held - 167
Largest Field MUs x Days - 123031
Forced Drone Recalls - 1
Unique Missions Completed - 98
Hacks Drone - 31737
Hacks Glyph - 46
Hack Points - 52024
Longest Hacking Streak - 730
Agents Successfully Recruited - 0
Mission Day(s) Attended - 0
NL-1331 Meetup(s) Attended - 1
First Saturday Events - 3
Recursions - 1
```

# Installation

Install the required packeges from requirement.txt

If you want, you can Create a supervisor config file or create a service
You can, if you want, use python virtual enviroment.

Example Supervisor conf:
```
[program:telegrambot]
command=/srv/venv/bin/python3 agentstats.py
directory=/data/telegrambot
stdout_logfile=//data/telegrambot/process_output.txt
redirect_stderr=true
```

