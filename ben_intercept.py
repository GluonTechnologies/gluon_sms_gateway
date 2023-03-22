import logging


lookup_json = {
    'google': 'g-o-o-g-l-e',
    'truecaller': 'true-caller'
}


def modify(message):
    message = str(message.decode())
    for word in message.split():
        if word.lower() in list(lookup_json.keys()):
            message = message.replace(word, lookup_json[word.lower()])
    return bytes(message, 'utf-8')

# Set logger
logger = logging.getLogger('logging-example')
if len(logger.handlers) != 1:
    hdlr = logging.FileHandler('/opt/log.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.DEBUG)

logger.info('Got pdu: %s' % routable.pdu.params)

routable.pdu.params['source_addr'] = '9543'
routable.pdu.params['short_message'] = modify(routable.pdu.params['short_message'])