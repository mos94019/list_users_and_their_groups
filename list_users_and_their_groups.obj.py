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

user_dict =  {}
with open('/etc/passwd') as passwd:
    for line in passwd:
        if '#' in line:
            continue
        fields = line.strip().split(':')
        username = fields[0]
        userid = fields[2]
        user = User()
        user_dict[username] = user
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
                user_dict[member].usergroups.append(group_name)

for user in user_dict.keys():
    pprint.pprint(user_dict[user].username + " " +  str(user_dict[user].userid) + " " + str(user_dict[user].usergroups))


