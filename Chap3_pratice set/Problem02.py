letter = ''' 
Dear <|Name|>,
You are selected!
Please come to our office at your earliest convenience.
<|Date|>'''
print(letter.replace("<|Name|>", "Ashutosh").replace("<|Date|>", "24 Sep 2030"))