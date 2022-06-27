inventory = ['Куртка', 'Штаны', 'Кaстрюля', 'Нож']
strategy = input('выберите стратегию LIFO/FIFO')
answer = ''
uItems = input('что у вас?')
if strategy == 'LIFO':
	while uItems != answer:
		print('Спасибо')
		inventory.append(uItems)
		uItems = input('что у вас?')

	while uItems == answer:
		last_item = inventory.pop()
		print(f'Возьмите, вот вам ,{last_item}')
		second_answer = input('Что нибудь еще?')
		if second_answer == answer:
		  print('Захолите позже')
		break
elif strategy == 'FIFO':
	uItems = input('что у вас?')
	while uItems != answer:
		print('Спасибо')
		inventory.append(uItems)
		uItems = input('что у вас?')

	while uItems == answer:
		last_item = inventory.reverse()
		last_item = inventory.pop()
		print(f'Возьмите, вот вам ,{last_item}')
		second_answer = input('Что нибудь еще?')
		if second_answer == answer:
		  print('Заходите позже')
		break