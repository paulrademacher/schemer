from schemer import *

db = Database('manager')

repos = db.Table('repos')
repos.VarChar('Name')
repos.VarChar('UserName')
repos.VarChar('Url')  # len
repos.VarChar('RemoteOriginUrl')
repos.Boolean('Private')

users = db.Table('users')
users.VarChar('UserName')
users.VarChar('Email')

commits = db.Table('commits')
commits.VarChar('ShaLong')
commits.VarChar('ShaShort')
commits.Text('Comment')

print db
