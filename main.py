
from summarizer import textrank
from flask import Flask, jsonify, request
import requests
from slacker import Slacker
import json
import os
from config import *

slack = Slacker(keys["slack"])
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
	print para
	#Use your own api key
	payload = {'apikey': 'a429a338-07a1-4b6e-bd46-c75b1fab8c89', 'text': para}
	r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)
	json_r = json.loads(r.text)
	for i in range(len(json_r['concepts'])/2):
		temp = json_r['concepts'][i]['concept']
		if (len(temp) >= 4) and (" " in temp) and (temp != "joined the channel"):
			concepts += temp + ", "

	summary_token = textrank(para)
	summary = ""
	for i in summary_token:
		if "has joined the channel" not in i:
			summary += i + " "

	res = "*Chat Summary:* \n " + summary + "\n \n" + "*Topics Discussed:*  \n" + concepts

	print res
	return str(res)


if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
