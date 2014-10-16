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

To create a bot:

```

API.create_bot(user_key, username, host, botname)

```

To delete a bot:

```

API.delete_bot(user_key, username, host, botname)

```

To upload a file to a bot:

Note: The argument specified by filename should in the same folder as your code, and have one of the following extensions: “.aiml”, “.map”, “.set”, “.substitution”, “.properties”, or “.pdefaults”. The file_kind must be one of the six acceptable aiml filetypes: “aiml”, “map”, “set”, “substitution”, “properties”, or “pdefaults”.

```

API.upload_file(user_key, username, host, botname, filename, file_kind)

```

To compile a bot:

```

API.compile_bot(user_key, username, host, botname)

```

To talk to a bot. It has the optional parameters of _recent_, _session_id_, _reset_, and _client_name_.

```

API.talk(user_key, username, host, botname, input_text, session_id, recent=True)

```

This call returns both the bot's response and the session id. Here is an example that shows capturing and displaying these values.

```

result = API.talk(user_key, username, host, botname, input_text, session_id, recent=True)
bot_response = result['response']
session_id = result['sessionid']
print bot_response, session_id

```


To debug input to a bot:

Note: session_id, reset, trace, and recent  are all optional parameters. In the example provided, they are all passed in as _True_. Trace, if included, will include AIML trace information for an input  Reset resets a bot’s memory, erasing predicates as well as that and topic information. 

```

API.debug_bot(user_key, username, host, botname, input_text, session_id=True, reset=True, trace=True, recent=True)

```



 


