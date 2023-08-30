from github import Github
import os

access_token = USER = os.getenv('GH_API_ACCESS')
token = Github(access_token)
repo = token.get_repo('quarkusio/quarkus')
issues = repo.get_issues(state='open')
for issue in issues.head(5):
    print(issue.number, issue.title, issue.labels)