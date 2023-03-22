def modify(message):
    lookup_json = {
        'google': 'G-o-o-g-l-e',
        'truecaller': 'True-caller'
    }
    message = str(message.decode())
    for word in message.split():
        if word.lower() in list(lookup_json.keys()):
            message = message.replace(word, lookup_json[word.lower()])
    return bytes(message, 'utf-8')

routable.pdu.params['source_addr'] = '9543'
routable.pdu.params['short_message'] = modify(routable.pdu.params['short_message'])