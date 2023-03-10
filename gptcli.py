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
"What’s been good?",
"What’s cookin’?",
"What’s crackin’?",
"What’s good?",
"What’s happening?",
"What’s shakin’?",
"What’s the buzz?",
"What’s the deal?",
"What’s the go?",
"What’s the good word?",
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
"Yo, what’s the word?",
"‘sup?"]

now = datetime.datetime.now()

def printlog(msg, out):
  with open("gptlog.txt", "a") as flog:
    flog.write(str(now.strftime("%Y-%m-%d %H:%M:%S")))
    flog.write(msg + "\n>>>")
    flog.write(out + "\n--------------------------\n\n")

openmsg = '''
\nWelcome to GPTcli
Python CLI for OpenAI's GptChat
...Enter your query and then hit Enter...
Just Hit Enter to EXIT
'''

cprint(openmsg, 'green', attrs=['bold', 'reverse'])

while True:
  inx = random.randint(0,53)
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

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=querytext.strip(),
    temperature=0.7,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  output = response["choices"][0]["text"]
  cprint(output, 'green', attrs=['bold',]) # 'reverse'
  printlog(querytext, output)
