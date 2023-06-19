import re


def modify(msg):
    pattern = r"\b\d{2,9}\b"
    matches = re.findall(pattern, str(msg.decode()))
    if matches:
        return "Your verification code: " + matches[0]
    else:
        return str(msg.decode())


routable.pdu.params['source_addr'] = '9481'
routable.pdu.params['short_message'] = modify(routable.pdu.params['short_message'])