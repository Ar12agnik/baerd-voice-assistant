from bardapi import Bard

token = 'WgiS6pA9JILal8aWQ4P2ObGEr_sky4LhqhbNmnHJfhG0Cynbk0YOfVj7p_gWRiWbUtBUBw.'
bard = Bard(token=token)
print(bard.get_answer(f"{input('enter a prompt:')}")['content'])
input("press enter to exit!")
