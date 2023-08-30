from github import Github
import os
import pandas as pd

access_token = USER = os.getenv('GH_API_ACCESS')
token = Github(access_token)
repo = token.get_repo('quarkusio/quarkus')
issues = repo.get_issues(state='open')

print("Number of issues in total: ", issues.totalCount)
for issue in issues.get_page(1):
    print(issue.number, issue.title, issue.labels)

print(type(issues)) 

# turn issues into pandas dataframe
issues_df = pd.DataFrame([issue in issues])
print(issues_df)
