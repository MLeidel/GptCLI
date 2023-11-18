# GptCLI

__Console program (Python) to access Gpt OpenAI Completion engine__  
Model: gpt-4-1106-preview

Requires: OpenAI >=1.0.0 API module

```bash
$ pip install termcolor openai

```

Execute like:

```python
$ python3 gptcli.py

#   program loops until user exits .. or

$ python3 gptcli.py What percentage of people have pets?

#   program exits after printing response

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
