# get top voted Questions on Stack Overflow
This script is used for getting voted questions on Stack Overflow 

## How to run:
1. Open terminal, run ```cd ~ && git clone https://github.com/hoangvux116/top-quest-Stack```
2. Create a virtual environment:\
```cd top-quest-Stack```  
```virtualenv -p python3 venv```
3. Activate this venv and install requirement packages:\
```source venv/bin/activate```  
```pip install -r requirements.txt```
4. run ```python3  top-question_stack.py [N] [LABEL]```<br>
Remark: [N] = number of top voted question you would like to get <br><ul><ul>
	[LABEL] = name of topic, add a symbol '-' between every single word
