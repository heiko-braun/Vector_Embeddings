from github import Github
token = Github('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')
repo = token.get_repo('quarkusio/quarkus')
issues = repo.get_issues(state='open')
for issue in issues:
    print(issue.labels)