Updated to work with Ingress version 2.58.1

## Ingress Telegrambot
## Usage
## installation

# ingress telegrambot

This is a simple telegram bot for ingress agents who wants to save there stats in a database

It can receive and send stats from multiple ingress agents.
The telegram userid will be used to separate the agents. 
So don't send multiple agent stats with 1 telegram account, that will give you strange results when you ask the bot for the agent stats.

You don't need to create a database, the script will create the data if needed.
If ingress change the game in anyway, so that the agent stats aren't what this script expect, the script will crash.
If i have time, i will fix this as soon as possible. (as long as i play ingress)
Change the database by hand if you don't want to lose you're stats.

Tested and used with a Raspberry Pi 2, with debian as OS.

The bot can reply on some simple commands.



# Usage

Copy the agent stats from ingress and past it into telegram, so that you send the data to you're bot.

![Agent stat](https://github.com/w2k8/ingress-telegrambot/blob/master/images/AgentName.png)

When you have set: 'reply_stats: True' you should receive a message like this:
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
Hacks - 31737
Drone Hacks - 46
Glyph Hack Points - 52024
Longest Hacking Streak - 730
Agents Successfully Recruited - 0
Mission Day(s) Attended - 0
NL-1331 Meetup(s) Attended - 1
First Saturday Events - 3
Recursions - 1
```

When you have set: 'reply_diff: True'
you should receive a message like this:
It contains the difference between the last submit.
You can set what you want to receive or not with the bitstring 'reply_diff_index'
every 'bit' correspond with a item in the list agent_stats_objects.

```
Thanks for submitting you're stats.

Last submit was: 2020-08-05 18:42:07

Displaying changes since last submit
Current AP - 69969
Unique Portals Visited - 1
Unique Portals Drone Visited - 2
Portal Scans Uploaded - 8
Scout Controller on Unique Portals - 8
Resonators Deployed - 141
Links Created - 6
Control Fields Created - 5
Mind Units Captured - 178
XM Recharged - 39958
Portals Captured - 14
Unique Portals Captured - 1
Mods Deployed - 30
Resonators Destroyed - 87
Portals Neutralized - 16
Enemy Links Destroyed - 6
Enemy Fields Destroyed - 3
Hacks - 112
Drone Hacks - 1
Glyph Hack Points - 506
```

# Installation

Install the required packages from requirement.txt

If you want, you can Create a supervisor config file or create a service. 
You can, if you want, use python virtual environment.

Example Supervisor conf:
```
[program:telegrambot]
command=/srv/venv/bin/python3 agentstats.py
directory=/data/telegrambot
stdout_logfile=//data/telegrambot/process_output.txt
redirect_stderr=true
```

