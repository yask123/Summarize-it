# Summarize It!

Summarize it is a chat summarizer plugin for instant messaging applications. It summarizes the large content of chat logs which enables users to quickly understand the current context of the conversation. Currently Summarize it works on top of Slack as its plugin.

## Installing Summarize It plugin for your slack
1. Create a token for your team `https://api.slack.com/web` 
2. Clone/fork this repository and create a file "config.py" like so:
    `keys = {
        "slack": "your-token-here"
    }`
3. Deploy the app at heroku/IBM bluemix etc.
4. Visit `https://<your-team-name>.slack.com/services/new/slash-commands`
5. Enter the command name you wish to use
6. Enter the request url as `<your-deployed-app-url>/slack`

## Using Summarize It plugin with slack
Type /your-command to initiate the plugin. The plugin will automatically summarize the above chat contents and display the summary.

## Screenshots

#### Hackathon Discussion
![Hackathon Discussion](img/hackathon-discussion.png)

#### Meeting Discussion
![Meeting Discussion](img/meeting-discussion.png)

## Authors and Contributors
Yask Srivastava (Developer), [Ketan Bhatt](https://github.com/ketanbhatt) (Developer), [Pranu Sarna](https://github.com/psarna94) (Developer) and [Vinayak Mehta](https://github.com/vortex-ape) (Data Scientist).

## Support or Contact
Having trouble with summarize it? Create an issue in the repository GitHub Repo.



[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/yask123/summarize-it/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

