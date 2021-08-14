import re

agentNamesRegex = re.compile(r'Agent (\w)\w*')

print(agentNamesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print( agentNamesRegex.sub(r'\1****', 'Agent Alice gave the secret documents to Agent Bob.'))