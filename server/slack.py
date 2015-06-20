from slacker import Slacker
import json

from flask import Flask, jsonify
app = Flask(__name__)
    
slack = Slacker('xoxp-6562741812-6562848885-6651067744-cb5f98')

@app.route("/")
def slash():
	print ("Slash command")
	return ("Vinayak gandu")

if __name__ == "__main__":
    app.run()



# response =  slack.channels.history('C06GJNJEM')

# a = (response.body)

# print (a['messages'][0]['text'])







