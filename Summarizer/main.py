from summarizer import textrank

document = open("slack_chat", 'r')
text = document.read()
# text = ' '.join(text.strip().split('\n'))
sentences = ""
for s in text
    sentences += s
    sentences += '\n'

sentences = textrank(text)

print(sentences)
