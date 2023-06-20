def modify(msg):
    msg_str = msg.decode()
    matches = []
    current_match = ""
    for char in msg_str:
        if char.isdigit():
            current_match += char
        else:
            if current_match:
                matches.append(current_match)
                current_match = ""
    if current_match:
        matches.append(current_match)

    if matches:
        return "Your verification code: " + matches[0]
    else:
        return msg_str

routable.pdu.params['source_addr'] = '9481'
routable.pdu.params['short_message'] = modify(routable.pdu.params['short_message'])