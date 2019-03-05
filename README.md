
## Pandorabots API module for Python 

  
This is a guide for the Pandorabots SDK for the Python programming language. It provides usage guidelines as well as code examples.

  

Please read the [Documentation](https://developer.pandorabots.com/docs).

  

  

#### Installation

------------

The easiest way to install the latest version is to clone the repository from

Github and install it:

```
git clone https://github.com/pandorabots/pb-python.git
cd pb-python
python setup.py install
```

#### Usage
Import the Pandorabots object and create an instance with your credentials:

Note: `botname` is not required to create the object but is necessary to run bot-specific APIs

```
from main import Pandorabots
 
host = 'YOUR HOST'
botname = 'YOUR BOTNAME'
app_id = 'YOUR APP_ID'
user_key = 'YOUR USER_KEY'
test_filename = 'test.aiml'
 
API = Pandorabots(user_key, app_id, host, botname)
```
Each method returns the response from the Pandorabots API.

To create a bot:
```
result = API.create_bot(botname)
```
To select a bot (if one not specified in initial object creation):
```
API.selectBot(botname)
```
To get a list of your bots:
```
result = API.list_bots()
```
To delete a bot:
```
result = API.delete_bot(botname)
```
To upload a file to a bot:
```
filename = 'test.aiml'
result = API.upload_file(filename)
```
To delete a file:
```
result = api.delete_file(filename)
```
To get a list of all your bot's files:
```
result = API.list_files()
```
To get a file:
```
filename = 'test.aiml'
result = API.get_file(filename)
```
To download a bot as a zip file to the current directory:
```
API.download_bot()
```
To compile a bot:
```
result = API.compile_bot()
```
To talk to a bot you need to send an input object of the form:
```
input_object = {'message':'hi',
				'trace':True,
				'reset':True,
				'that':'Hello',
				'topic': 'greetings',		
				'sessionid': '123',
				'recent': True,
				'reload':True,
				'extra': True,
				'client_name': 'client_name'}

result = API.talk(input_object)
```
Only the `message` parameter is required. The other paramters can be included for debugging purposes. Note: `client_name` and `trace` be specified concurrently for security purposes.

To talk with your bot via the atalk (anonymous talk) api send an input object of the form:
```
result = API.atalk(input_object)
```
For more information see the [developer docs](https://developer.pandorabots.com/docs) or the test file `test.py` in the `pb_py` folder.
