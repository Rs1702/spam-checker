data=None

try:
  with open('key_word.txt','r') as f:
    data =f.read()

except FileNotFoundError:
  print("file not found!")

def spam_check(sentence, spam_list):
  sentence = sentence.lower()
  for word in spam_list:
    if word in sentence:
      print("mark as spam")
      return True
  print('The given snetence is safe.')
  return False

x=spam_check('hey there i am free', data.split(', '))
print(x)