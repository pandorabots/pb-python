###pb-python###

Pandorabots API module for Python

﻿This is a guide for the Pandorabots SDK for the Python programming language. It provides usage guidelines as well code examples.

Each API requires an API Key, which can be received after registering at: http:/developer.pandorabots.com


Installation
------------
The easiest way to install the latest version
is by using pip/easy_install to pull it from PyPI:

    pip install PbPython

You may also use Git to clone the repository from
Github and install it manually:

    git clone https://github.com/pandorabots/pb-python.git
    python setup.py install

 All you have to do is write the following line at the top of your code.

```

import Pandorabots_API_Calls as API

```

To create a bot:

```

API.create_bot(user_key, username, botname)

```

To delete a bot:

```

API.delete_bot(user_key, username, botname)

```

To upload a file to a bot:

Note: The argument specified by filename should in the same folder as your code, and have one of the following extensions: “.aiml”, “.map”, “.set”, “.substitution”, “.properties”, or “.pdefaults”. The file_kind must be one of the six acceptable aiml filetypes: “aiml”, “map”, “set”, “substitution”, “properties”, or “pdefaults”.

```

API.upload_file(user_key, username, botname, filename, file_kind)

```

To compile a bot:

```

API.compile_bot(user_key, username, botname)

```

To initiate a conversation with a bot. This function returns a _session_id_, which allows the bot to maintain information about individual conversations. Note: _recent_ is an optional parameter, which in this example is passed in as _True_.

```

session_id = API.init_talk(user_key, username, botname, input_text, recent=True)

```

To continue a conversation with a bot. This function requires a session_id, such as the one returned in the previous example. Note: _recent_ is an optional parameter, which in this example is passed in as _True_.

```

API.talk(user_key, username, botname, input_text, session_id, recent=True)

```

To debug input to a bot:

Note: session_id, reset, trace, and recent  are all optional parameters. In the example provided, they are all passed in as _True_. Trace, if included, will include AIML trace information for an input  Reset resets a bot’s memory, erasing predicates as well as that and topic information. Trace 

```

API.debug_bot(user_key, username, botname, input_text, session_id=True, reset=True, trace=True, recent=True)

```



 


