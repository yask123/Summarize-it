from summarizer import textrank
from flask import Flask, jsonify, request
import requests
import pycps
from slacker import Slacker
import json
import os

slack = Slacker('xoxp-6562741812-6562848885-6651067744-cb5f98')
app = Flask(__name__)

@app.route("/slack", methods=['POST'])
def slackReq():
	req_data = request.form
	channel_id = req_data.getlist('channel_id')
	response =  slack.channels.history(channel_id)
	a = (response.body)
	para = ""
	concepts = ""
	for i in range(len(a['messages']) - 1, -1, -1):
		para += a['messages'][i]['text'] + ". "
	para = para.decode("utf-8")

	payload = {'apikey': 'a429a338-07a1-4b6e-bd46-c75b1fab8c89', 'text': para}
	r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)
	json_r = json.loads(r.text)
	for i in range(len(json_r['concepts'])/2):
		concepts += json_r['concepts'][i]['concept'] + ", "

	summary_token = textrank(para)
	summary = ""
	for i in summary_token:
		summary += i
		summary += " "

	res = "*Summary:* \n " + summary + "\n \n" + "*Concepts:*  \n" + concepts
	print res
	return str(res)


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)





# con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'Angel-hack', 'ketanbhatt1006@gmail.com', 'Updated@2015', '100581')

# con.insert({5: '<text>foobar</text>',
#             6: '<text>baz</text>', 
#             'id7': {'title': 'Loerem Ipsum', 'text': 'Long, long text'}})
