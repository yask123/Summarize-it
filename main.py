from flask import Flask, jsonify, request
import requests
import pycps
from slacker import Slacker
import json
import os

slack = Slacker('xoxp-6562741812-6562848885-6651067744-cb5f98')
app = Flask(__name__)

@app.route("/summarize", methods=['POST'])
def slack():
	print dir(request)
	# response =  slack.channels.history(channel_id)
	# a = (response.body)

	# return (a)
	return "Yoyo"

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)



# payload = {'apikey': 'a429a338-07a1-4b6e-bd46-c75b1fab8c89', 'text': 'Someone I know recently combined Maple Syrup.'}

# r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)

# print r.text


# con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'Angel-hack', 'ketanbhatt1006@gmail.com', 'Updated@2015', '100581')

# con.insert({5: '<text>foobar</text>',
#             6: '<text>baz</text>', 
#             'id7': {'title': 'Loerem Ipsum', 'text': 'Long, long text'}})
