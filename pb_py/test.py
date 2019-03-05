from main_class import Pandorabots

host = 'YOUR HOST'
botname = 'YOUR BOTNAME'
app_id = 'YOUR APP_ID'
user_key = 'YOUR USER_KEY'
test_filename = 'test.aiml'

simple_input = {'message':'hi'}
advanced_input = {'message':'hi',
                  'trace':True,
                  'reset':True,
                  'that':'Hello',
                  'topic': 'greetings',
                  'sessionid': '123',
                  'recent': True,

                  'reload':True,
                  'extra': True
                  }
atalk_input = {'message':'hi',
               'sessionid': '123',
               'recent': True
                }

main = Pandorabots(user_key, app_id, host, botname)

# test create
print(main.create_bot(botname).text)

# test list_bots
print(main.list_bots().text)

# upload file
print(main.upload_file(test_filename).text)

# list files
print(main.list_files().text)

# get file
print(main.get_file(test_filename).text)

# download bot
print(main.download_bot().text)

# compile_bot
print(main.compile_bot().text)

# talk
print(main.talk(simple_input).text)

# debug
print(main.talk(advanced_input).text)

#atalk
print(main.atalk(atalk_input).text)

# delete file
print(main.delete_file(test_filename).text)

# test delete
print(main.delete_bot(botname).text)
