import json

json_object = json.dumps(routable.pdu.params)
routable.pdu.params['source_addr'] = '9543'

f = open("/opt/log.txt", "a")
f.write("" + json_object)
f.close()