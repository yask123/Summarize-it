from summarizer import textrank

document = open("snehanshu", 'r')
text = document.read()
text = ' '.join(text.strip().split('\n'))

sentences = textrank(text)

print(sentences)
