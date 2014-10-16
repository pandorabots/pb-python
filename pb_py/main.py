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
    return output

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
    return output

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
        return filename + ' successfully uploaded'
    else:
        return response.reason

def compile_bot(user_key,username,host, botname):
    path = '/bot/' + username +'/' + botname + '/verify'
    url = host_base + host + path
    query = {"user_key": user_key}
    response = requests.get(url, params=query)
    if response.ok:
        output = botname + ' has been successfully compiled!'
    else:
        result = response.json()
        print result
        message = result["message"]
        error = str(result["errors"][0])
        output = message + '\n' + error + '\n'
    return output

def talk(user_key, username, host, botname, input_text, session_id=False, recent=False, reset=False, trace=False, clientID=False):
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
    output = {}
    if status == 'ok':
        print result
        output["response"] =  result['responses'][0]
        if reset:
            output["output"] = 'Bot has been reset.'
        if trace:
            trace_text = result['trace']
            trace_string = 'Trace: '
            length = range(len(trace_text))
            every_other = length[::2][:-1]
            for elt in every_other:
                trace_string +='Level: ' + str(trace_text[elt]['level']) 
                trace_string += ' Sentence to process: ' 
                for elt1 in range(len(trace_text[elt]['input'])):
                    trace_string += str(trace_text[elt]['input'][elt1]) + ' '
                trace_string += 'Matched pattern: ' + str(trace_text[elt+1]['matched'][0])
                trace_string += ' from file: ' + trace_text[elt+1]['filename']
                trace_string += 'template: ' + trace_text[elt+1]['template']
            output["trace"] = trace_string
        if 'sessionid'  in result:
            output["sessionid"] = result['sessionid']
    else:
        output["response"] = result['message']
    return output


def debug_bot(user_key, username, host, botname, input_text, session_id='', recent=False, reset=False, trace=False):
    response = talk(user_key, username, host, botname, input_text, session_id, recent, reset, trace)
    return response
                          
