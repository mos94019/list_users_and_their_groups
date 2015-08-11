#!/usr/bin/env python
""" Parses /etc/passwd and /etc/group. For each user, lists the username, userid, and 
associated groups
"""

import pprint

class User:
    def __init__(self):
        self.userid = 0
        self.usergroups = []
        self.username = ''

users = []
with open('/etc/passwd') as passwd:
    for line in passwd:
        if '#' in line:
            continue
        fields = line.strip().split(':')
        username = fields[0]
        userid = fields[2]
        user = User()
        users.append(user)
        user.userid = userid
        user.username = username

groups = []
with open('/etc/group') as group:
    for line in group:
        if '#' in line:
            continue
        fields = line.strip().split(':')
        group_name = fields[0]
        members_list = fields[3]
        if members_list:
            members = members_list.split(',')
            for member in members:
                for user in users:
                    if member == user.username:
                        user.usergroups.append(group_name)

for user in users:
    pprint.pprint(user.username + " " +  str(user.userid) + " " + str(user.usergroups))


