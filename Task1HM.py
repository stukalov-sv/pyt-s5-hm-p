# Напишите программу, удаляющую из текста все слова, содержащие "абв"

text = 'абв Ура, питон круто, очеагбвнь инетресные семинарабвы! абв'
text = text.split()
result = ' '.join(filter(lambda x: 'абв' not in x, text))

print(result)
