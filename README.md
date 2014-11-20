###pb-python###

Pandorabots API module for Python

﻿This is a guide for the Pandorabots SDK for the Python programming language. It provides usage guidelines as well as code examples.

Please read the [Documentation.] (https://developer.pandorabots.com/docs)


Installation
------------
The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install PbPython

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/pandorabots/pb-python.git
    cd pb-python
    python setup.py install

 All you have to do is write the following lines to the top of your code.

```

from pb_py import main as API
host = 'aiaas.pandorabots.com'

```

Each API call returns a value indicating the success of the call. In the event of an error, a message is returned detailing the error. To receive visual feedback as to the success of your call simply print the result, as in the following examples.

To create a bot:

```

result = API.create_bot(user_key, app_id, host, botname)
print result

```

To get a list of your bots:

```

result = API.list_bots(user_key, app_id, host)
print result

```

To delete a bot:

```

result = API.delete_bot(user_key, app_id, host, botname)
print result

```

To upload a file to a bot:

```

result = API.upload_file(user_key, app_id, host, botname, filename)
print result

```

To delete a file:

```

result = api.delete_file(user_key, app_id, host, botname, filename)
print result

```

To get a list of all your bot's files:

```

result = API.get_files(user_key, app_id, host, botname)
print result

```

To download a bot as a zip file:

```

result = API.download_bot(user_key, app_id, host, botname)
print result

```

By default the bot downloads to the folder where the call was made from, but alternatively you can specify a folder as a download location:

```

result = API.download_bot(user_key, app_id, host, botname, '~/username/Downloads/'
print result

```

To compile a bot:

```

result = API.compile_bot(user_key, app_id, host, botname)
print result

```

To talk to a bot. It has the optional parameters of _recent_, _session_id_, _reset_, and _client_name_.

```

API.talk(user_key, app_id, host, botname, input_text, session_id, recent=True)

```

This call returns both the bot's response and the session id. Here is an example that shows capturing and displaying these values.

```

result = API.talk(user_key, app_id, host, botname, input_text, session_id, recent=True)
bot_response = result['response']
session_id = result['sessionid']
print bot_response, session_id

```

To debug input to a bot:

Note: session_id, reset, trace, and recent  are all optional parameters. In the example provided, they are all passed in as _True_. Trace, if included, will include AIML trace information for an input  Reset resets a bot’s memory, erasing predicates as well as that and topic information. 

```

result = API.debug_bot(user_key, app_id, host, botname, input_text, session_id=True, reset=True, trace=True, recent=True)
print result

```

It should be noted that storing the return values of the various API calls, as in the previous examples, is not required. The following two examples accomplish the same thing, the only difference being that the second example provides feedback as to the success or failure of the call.

Example 1: 

```

API.create_bot(user_key, app_id, host, botname)

```

Example 2:

```

result = API.create_bot(user_key, app_id, host, botname)
print result

```

 


