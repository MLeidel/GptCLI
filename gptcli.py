'''
gptcli.py
by Michael Leidel, Jan 12 2023
besides the query itself, other commands are:
  bye     or just hit Enter key to exit
  log     print out the log contents to the console
  clear   purge the log contents
Updated to OpenAI API v1.333, Nov 2023
'''
import sys, os
import datetime
from termcolor import cprint
from openai import OpenAI

MODEL = "gpt-4o"

now = datetime.datetime.now()

def printlog(msg, out):
  with open("gptlog.txt", "a") as flog:
    flog.write(str(now.strftime("%Y-%m-%d %H:%M:%S ")))
    flog.write(msg + "\n>>>")
    flog.write(out + "\n--------------------------\n\n")

openmsg = '''
\nWelcome to GPTcli
Python CLI for OpenAI
...Enter your query and then hit Enter...

Enter to EXIT
Enter 'log' to print log.
Enter 'clear' to clear the log.
'''

if len(sys.argv) <= 1:
  cprint(openmsg, 'yellow', attrs=['reverse'])
  print(f"Model: {MODEL}")

while True:
# check for command-line query
  try:
      client = OpenAI(
      api_key = os.environ.get("GPTKEY")  # openai API
      )
  except Exception as e:
      print("Could Not Read Key file\n", "Did you enter your Gpt Key?")
      sys.exit()

  if len(sys.argv) > 1:
    querytext = ' '.join(sys.argv[1:])
  else:
    print()
    quest = "gptcli: " + "Enter prompt or command "
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

  response = client.chat.completions.create(
      # model="gpt-3.5-turbo",
      # model="gpt-4",
      model=MODEL,
      messages=[{"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content" : querytext.strip()}
      ]
  )

  output = response.choices[0].message.content
  cprint(output, 'green', attrs=['bold',]) # 'reverse'
  printlog(querytext, output)

  if len(sys.argv) > 1:
    break  # exit the while loop (quit)
