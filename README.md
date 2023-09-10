# GptCLI

Console program to access Gpt openAI Completion engine gpt-3.5-turbo


Execute like:

```python
? python3 gptcli.py

#   program loops until user exits .. or

? python3 gptcli.py "What percentage of people have pets?"

#   program exits after printing response
#   NOTE: PARENTHESES ARE NOT needed around the query text

```
NOTE: simple bash script makes a smooth command line experience:

```bash
#!/bin/bash

cd ~/pathtoAppDirectory
python3 gptcli.py "$@"

```
---

Besides the query itself, other commands are:  
-  bye     
>program exits (or just hit Enter key to exit)
-  log     
>print out the log contents to the console
-  clear   
>purge the log contents

---

The _Gpt API key_ must be set up in an  
environment variable called 'GPTKEY'

---

moduals required: termcolor and openai modules
