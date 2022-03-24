letter='''Dear <|Name|>,
Greetings from ABC company. I am happy to tell about your selection.
You are selected!
Thanks & regards
Date: <|Date|> '''
name=input("Enter your name\n")
date=input("Enter date\n")
letter=letter.replace("<|Name|>" , name)
letter=letter.replace("<|Date|>" , date)
print(letter)