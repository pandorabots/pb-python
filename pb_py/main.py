import requests

class Pandorabots:
    def __init__(self, user_key, app_id, host, botname=False, botkey=False):
        self.user_key = user_key
        self.app_id = app_id
        self.host = host
        self.botname = botname
        self.no_botname_error = {'error':'please set a botname via select_bot("your_botname")'}
        self.no_message_error = {'error':'please include a message string input to your bot, ex. {"message":"hello"}")'}
        self.no_botkey_error = {'error':'please set a botkey via set_botkey("your_botkey")'}
        self.use_api_host_error = {'error':'host must be "api.pandorabots.com" to use atalk with a botkey'}
        self.botkey = botkey
        
    def set_botkey(self, botkey):
        self.botkey = botkey

    def select_bot(self, botname):
        self.botname = botname

    def create_bot(self, botname):
        path = '/bot/' + self.app_id +'/' + self.botname
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.put(url, params=query)
        if response.ok :
            self.botname = botname
        return response
    
    def list_bots(self):
        path = '/bot/' + self.app_id
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.get(url, params=query)
        return response

    def delete_bot(self, botname):
        path = '/bot/' + self.app_id +'/' + self.botname
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.delete(url, params=query)
        return response

    def upload_file(self, filename):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id + '/' + self.botname + '/'
        filepath = filename
        if '/' in filename:
            filename = filename.split('/')[-1]
        file_kind = filename.split('.')[-1]
        if file_kind == 'pdefaults' or file_kind =='properties':
            path += file_kind
        if file_kind == 'map' or file_kind == 'set' or file_kind == 'substitution':
            path += file_kind + '/' + filename.split('.')[0]
        if file_kind == 'aiml':
            path += 'file/' + filename
        if path == '/bot/' + self.app_id +'/' + self.botname + '/':
            output = 'File type must be one of the following: substitution, properties, aiml, map, set, or pdefaults'
            return output
        url = "https://" + self.host + path
        data = open(filepath,'rb').read()
        query = {"user_key": self.user_key}
        response = requests.put(url, params=query, data=data)
        return response

    def list_files(self):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id + '/' + self.botname
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.get(url,params=query)
        return response
    
    def get_file(self, filename):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id + '/' + self.botname +'/'
        file_kind = filename.split('.')[-1]
        if file_kind == 'pdefaults' or file_kind =='properties':
            path += file_kind
        if file_kind == 'map' or file_kind == 'set' or file_kind == 'substitution':
            path += file_kind + '/' + filename.split('.')[0]
        if file_kind == 'aiml':
            path += 'file/' + filename
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.get(url, params=query)
        return response
    
    def download_bot(self):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id + '/' + self.botname 
        url = "https://" + self.host + path
        query = {"user_key": self.user_key,
                 "return": 'zip'}
        response = requests.get(url, params=query)
        return response

    def delete_file(self, filename):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id + '/' + self.botname + '/'
        file_kind = filename.split('.')[-1]
        if file_kind == 'pdefaults' or file_kind =='properties':
            path += file_kind
        if file_kind == 'map' or file_kind == 'set' or file_kind == 'substitution':
            path += file_kind + '/' + filename.split('.')[0]
        if file_kind == 'aiml':
            path += 'file/' + filename
        if path == '/bot/' + self.app_id +'/' + self.botname + '/':
            output = 'File type must be one of the following: substitution, properties, aiml, map, set, or pdefaults'
            return output
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.delete(url, params=query)
        return response

    def compile_bot(self):
        if not self.botname:
            return self.no_botname_error
        path = '/bot/' + self.app_id +'/' + self.botname + '/verify'
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        response = requests.get(url, params=query)
        return response

    def talk(self, input, usebotkey=False):
        if (usebotkey and not self.botkey) :
            return self.no_botkey_error
        if (usebotkey and not self.host == 'api.pandorabots.com'):
            return self.use_api_host_error
        if not usebotkey and not self.botname:
            return self.no_botname_error
        if not 'message' in input:
            return self.no_message_error
        path = '/atalk'
        if (not usebotkey):
            path += '/' + self.app_id + '/' + self.botname
        url = "https://" + self.host + path
        query = {"user_key": self.user_key}
        if usebotkey:
            query['botkey'] = self.botkey
        else:
            query["user_key"] = self.user_key
        if 'sessionid' in input:
            query['sessionid'] = input['sessionid']
        if 'recent' in input: 
            query['recent'] = str(input['recent'])
        if 'reset' in input:
            query['reset'] = str(input['reset'])
        if 'trace' in input:
            query['trace'] = str(input['trace'])
        if 'client_name' in input:
            query['client_name'] = input['client_name'] 
        if 'that' in input:
            query['that'] = input['that']
        if 'topic' in input:
            query['topic'] = input['topic']
        if 'reload' in input:
            query['reload'] = str(input['reload'])
        if 'extra' in input:
            query['extra'] = str(input['extra'])
        response = requests.post(url, params=query)
        return response
    
    def atalk(self, input, usebotkey=False):
        if (usebotkey and not self.botkey) :
            return self.no_botkey_error
        if (usebotkey and not self.host == 'api.pandorabots.com'):
            return self.use_api_host_error
        if not usebotkey and not self.botname:
            return self.no_botname_error
        if not 'message' in input:
            return self.no_message_error
        path = '/atalk'
        if (not usebotkey):
            path += '/' + self.app_id + '/' + self.botname
        url = "https://" + self.host + path
        query = {"input": input['message']}
        if usebotkey:
            query['botkey'] = self.botkey
        else:
            query["user_key"] = self.user_key
        if 'sessionid' in input:
            query['sessionid'] = input['sessionid']
        if 'recent' in input: 
            query['recent'] = str(input['recent'])
        if 'client_name' in input:
            query['client_name'] = input['client_name'] 
        response = requests.post(url, params=query)
        return response
