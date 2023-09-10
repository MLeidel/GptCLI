'''
gptcli.py
by Michael Leidel, Jan 12 2023
besides the query itself, other commands are:
  bye     or just hit Enter key to exit
  log     print out the log contents to the console
  clear   purge the log contents
'''
import openai
import random
import sys, os
import datetime
from termcolor import cprint

prompt = ["Sup?",
"Hey, how’s it going?",
"Hey, wassup?",
"Hey, what",
"Hey, what’s good?",
"Hey, What’s new?",
"Hey, what’s the buzz?",
"Hey, what’s the deal?",
"Hey, what’s the word?",
"Heya!",
"How are you doin’?",
"Howdy!",
"Howdy, partner!",
"Howzit going?",
"How’s by you?",
"How’s it all?",
"How’s it all?",
"How’s it going?",
"How’s the day going?",
"How’s things?",
"Sup, dude?",
"Wassssssssssup!",
"Wassup?",
"Wasuuuuup",
"Wazzup?",
"Whassup?",
"What’s cookin’?",
"What’s crackin’?",
"What’s happening?",
"What’s shakin’?",
"What’s the buzz?",
"What’s the happenin’?",
"What’s the haps?",
"What’s the haps?",
"What’s the scoop?",
"Whazzup?",
"Yo, how’s it going?",
"Yo, wazzup?",
"Yo, what’s good?",
"Yo, what’s happenin’",
"Yo, What’s new?",
"Yo, what’s new?",
"Yo, what’s the biz?",
"Yo, what’s the buzz?",
"Yo, what’s the deal?",
"Yo, what’s the haps?",
"Yo, what’s the word?"]

now = datetime.datetime.now()

def printlog(msg, out):
  with open("gptlog.txt", "a") as flog:
    flog.write(str(now.strftime("%Y-%m-%d %H:%M:%S ")))
    flog.write(msg + "\n>>>")
    flog.write(out + "\n--------------------------\n\n")

openmsg = '''
\nWelcome to GPTcli
Python CLI for OpenAI's GptChat
...Enter your query and then hit Enter...
Just Hit Enter to EXIT
'''

while True:
# check for command-line query
  if len(sys.argv) > 1:
    querytext = ' '.join(sys.argv[1:])
    openai.api_key = os.environ.get("GPTKEY")
  else:
    cprint(openmsg, 'green', attrs=['bold', 'reverse'])
    inx = random.randint(0,48)
    print()
    quest = "gptcli: " + prompt[inx] + " "

    openai.api_key = os.environ.get("GPTKEY")

    cprint(quest, 'white', attrs=['bold',])
    querytext = input().strip()

  if querytext == "bye":
    sys.exit()
  elif querytext == "":
    sys.exit()
  elif querytext == "clear":
    os.remove("gptlog.txt")
    os.system("touch gptlog.txt")
    print("Log cleared.")
    continue
  elif querytext == "log":
    with open('gptlog.txt', 'r') as f:
      for line in f:
          print(line, end='')
    continue

  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      # model="gpt-4",
      messages = [{"role": "user", "content" : querytext.strip()}]
  )
  output = response['choices'][0]['message']['content']
  cprint(output, 'green', attrs=['bold',]) # 'reverse'
  printlog(querytext, output)

  if len(sys.argv) > 1:
    break  # exit the while loop
