import io

from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

#enter the name of your file
with io.open("kite runner.txt", "r", encoding="utf-8") as my_file:
     d = my_file.read() 

print(d)


x=d
text = x
# The target language
target = 'hi'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
z=format(translation['translatedText'])


#enter the target file name
with io.open('gg.txt','w',encoding='utf8') as f:
    f.write(z)


#file = open('gg.txt','w','utf-8')
#file.write(z)
f.close()
print(z)

