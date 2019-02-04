import dropbox

access_token = 'Qdc4fZ3xgNAAAAAAAAAArEkhOwxVt9_4YnA_pwDVoabx3ru-hiFZuy2Qio0Dl-Tm'
file_from = 'players.csv'
file_to = '/dropbox_py/players.csv'

dbx = dropbox.Dropbox(access_token)

with open(file_from, 'rb') as f:
		dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
