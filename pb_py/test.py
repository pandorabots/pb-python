import main

host = 'pbdpl.pandorabots.com'
botname = 'brebby'
app_id = 'un6a04c163'
user_key = 'pb265413298584842607794142375618755632950'
test_filename = 'test.aiml'

# test create
print(main.create_bot(user_key, app_id, host, botname))

# test list_bots
print(main.list_bots(user_key, app_id, host))

# upload file
print(main.upload_file(user_key, app_id, host, botname, test_filename))

# list files
print(main.list_files(user_key, app_id, host, botname))

# get file
print(main.get_file(user_key, app_id, host, botname, test_filename))

# download bot
#print(main.download_bot(user_key, app_id, host, botname))

# compile_bot
print(main.compile_bot(user_key, app_id, host, botname))

# talk
print(main.talk(user_key, app_id, host, botname, 'hi'))

# debug
print(main.talk(user_key, app_id, host, botname, 'hi', False, True, True, True))

#atalk
print(main.atalk(user_key, app_id, host, botname, 'hi'))

# delete file
print(main.delete_file(user_key, app_id, host, botname, test_filename))

# test delete
print(main.delete_bot(user_key, app_id, host, botname))

