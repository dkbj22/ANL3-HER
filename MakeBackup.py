import json 
import collections

class MakeBackup:
    def makeBackup():
        filePath = "Backup.json"

        for account in "Backup.json":
            with open (filePath) as lib:
                json.load(lib).pop(account)
#            with open(filePath, "w") as file:
#                json.dump(jsonFile, file, indent=4)

        for account in "AllAccounts.json":
            accountCopy = account
            with open (filePath) as lib:
                json.load(lib).append(accountCopy)
#            with open(filePath, "w") as file:
#                json.dump(jsonFile, file, indent=4)