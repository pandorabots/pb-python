import requests

host_base = "https://"

def create_bot(user_key,username,host,botname):
    path = '/bot/' + username +'/' + botname
    url = host_base + host + path
    query = {"user_key": user_key}
    response = requests.put(url, params=query)
    if response.ok:
        output = botname + ' has been created!'
    else:
        output = 'Bot creation failed! ' + response.json()['message'] + '.'
    print output

def delete_bot(user_key,username,host,botname):
    path = '/bot/' + username +'/' + botname
    url = host + path
    url = host_base + host + path
    query = {"user_key": user_key}
    response = requests.delete(url, params=query)
    if response.ok:
        output = botname + ' has been deleted!'
    else: 
        output = 'No bot named ' + botname + ' was found. '
        output += '%d %s' % (response.status_code, response.reason)
    print output

def upload_file(user_key,username,host,botname,filename,file_kind):
    path = '/bot/' + username + '/' + botname + '/'
    if file_kind == 'pdefaults' or file_kind =='properties':
        path += file_kind
    if file_kind == 'map' or file_kind == 'set' or file_kind == 'substitution':
        path += file_kind + '/' + filename.split('.')[0]
    if file_kind == 'aiml':
        path += 'file/' + filename
    url = host_base + host + path
    data = open(filename,'rb').read()
    query = {"user_key": user_key}
    response = requests.put(url, params=query, data=data)
    if response.ok:
        print filename + ' successfully uploaded'
    else:
        print response.reason

def compile_bot(user_key,username,host, botname):
    path = '/bot/' + username +'/' + botname + '/verify'
    url = host_base + host + path
    query = {"user_key": user_key}
    response = requests.get(url, params=query)
    if response.ok:
        output = botname + ' has been successfully compiled!'
    else:
        result = response.json()
        message = result["message"]
        error = str(result["errors"][0])
        output = message + '\n' + error + '\n'
    print output

def talk(user_key, username, host, botname, input_text, session_id, recent=False, reset=False, trace=False, clientID=false):
    path = '/talk/' + username + '/' + botname
    url = host_base + host + path
    query = {"user_key": user_key,
             "input": input_text
             }
    if recent:
        query['recent'] = recent
    if session_id:
        query['sessionid'] = session_id
    if reset:
        query['reset'] = reset
    if trace:
        query['trace'] = trace
    if clientID:
        query['client_name'] = clientID
    response = requests.post(url, params=query)
    result = response.json()
    status = result['status']
    if status == 'ok':
        output = result['responses'][0] + '\n'
        if reset:
            output += 'Bot has been reset.\n'
        if trace:
            trace_text = result['trace']
            output += 'Trace: \n'
            length = range(len(trace_text))
            every_other = length[::2][:-1]
            for elt in every_other:
                output+='Level: ' + str(trace_text[elt]['level']) 
                output += ' Sentence to process: ' 
                for elt1 in range(len(trace_text[elt]['input'])):
                    output += str(trace_text[elt]['input'][elt1]) + ' '
                output += '\nMatched pattern: ' + str(trace_text[elt+1]['matched'][0])
                output += ' from file: ' + trace_text[elt+1]['filename'] + '\n'
                output += 'template: ' + trace_text[elt+1]['template'] + '\n\n'
        if 'sessionid'  in result:
            sessionid = result['sessionid']
    else:
        output = result['message']
        sessionid = ''
    print output
    return sessionid


def debug_bot(user_key, username, host, botname, input_text, session_id='', recent=False, reset=False, trace=False):
    talk(user_key, username, host, botname, input_text, session_id, recent, reset, trace)

                          
