import sys

jira_desc = "This is Jira story: {}\n"+"It has below changes:-\n"+"a) error fixed.\n b) new features added.".format(sys.argv[1])
print(jira_desc)
