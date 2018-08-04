import requests
import csv

csvfile = open('honestbee.csv', 'w')
fieldnames = ["Name", "Clone URL", "Latest Commit Date", "Latest Author"]
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

lines = [line.rstrip('\n') for line in open('honestbee.txt')]
for line in lines:
    print "-------------------------- " + line + " --------------------------"
    if "/" in line:
        user, repo = line.split('/')
    repos = requests.get("https://api.github.com/users/" + user + "/repos")
    status_code = repos.status_code
    user_repos = repos.json()
    if status_code == 200:
        for user_repo in user_repos:
            if repo == user_repo['name']:
                finalrow = dict()

                commits_url = requests.get(user_repo['commits_url'].split('{')[0]).json()
                latest_commit_date = commits_url[0]['commit']['committer']['date']
                latest_author = commits_url[0]['commit']['author']['name']

                finalrow["Name"] = user_repo['name']
                finalrow["Clone URL"] = user_repo['clone_url']
                finalrow["Latest Commit Date"] = latest_commit_date
                finalrow["Latest Author"] = latest_author
                writer.writerow(finalrow)
                # print "Name : " + user_repo['name']
                # print "Clone URL : " + user_repo['clone_url']
                # print "Latest Commit Date : " + latest_commit_date
                # print "Latest Author : " + latest_author
                # print "\n"
    else:
        print line + " : Please check user and repo from input file \n"
