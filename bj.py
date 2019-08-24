import random

class Card():
	def __init__(self, suit, number):
		self.suit = suit
		self.number = number
	def __str__(self):
		return (str(self.number) + '  \n ' + self.suit + '\n   ')

class Deck():
 	suits = ['H', 'D', 'S', 'C']
 	#numbers = [1,2,10,11,12,13]
 	numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
 	deck = []
 	def __init__(self):
 		# suits = ['H', 'D', 'S', 'C']
 		# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
 		for suit in self.suits:
 			for number in self.numbers:
 				self.deck.append(Card(suit, number))
 	def __str__(self):
 		#print(self.deck[0].str())
 		pri = '   '
 		for card in self.deck:
 		 	pri += card.__str__()
 		return pri
 	def shuffle(self):
 		random.shuffle(self.deck)
 	def deal_a_card(self):
 		card = self.deck.pop(0)
 		return card
# class Deck():
# 	suits = ['H', 'D', 'S', 'C']
# 	deck = {'H':[1,2,3,4,5,6,7,8,9,10,11,12,13],
# 			'D':[1,2,3,4,5,6,7,8,9,10,11,12,13],
# 			'S':[1,2,3,4,5,6,7,8,9,10,11,12,13],
# 			'C':[1,2,3,4,5,6,7,8,9,10,11,12,13]}
# 	def __init__(self):
# 		pass
# 	def __str__(self):
# 		pri = ''
# 		for suit,numbers in self.deck.items():
# 			for number in numbers:
# 				pri += Card(suit, number).__str__()
# 		return pri
# 	def shuffle(self):
# 		ran_suit = random.randint(0,3)
# 		print(ran_suit)

# d = Deck()
# print (d)
# print('Popped = ' + d.deal_a_card().__str__())
# print(d)

class Hand():
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0
	def add_card(self, card):
		self.cards.append(card)
		if card.number > 10:
			self.value += 10
		elif card.number == 1:
			self.aces += 1
			self.value += 11
		else:
			self.value += card.number

	def adjust_for_ace(self):
		if card.number == 1:
			self.aces.append(card)

class Chips():
	def __init__(self):
		self.total = 100
		self.bet = 0
	def win_bet(self):
		print('You won %d chips' % self.bet)
		self.total += self.bet *2
		self.bet = 0
	def loose_bet(self):
		print('You lost %d chips' % self.bet)
		self.bet = 0
	def tied():
		self.total += self.bet
		self.bet = 0

			
def take_bet(chips):
	valid = False
	while valid == False:
		try:
			bet = int(input('How much do you want to bet?'))
		except:
			print('Please enter a valid amount')
			continue
		else:
			if bet > chips.total:
				print('You do not have that many chips. You have %d chips' % chips.total)
			else:
				valid = True
	chips.bet += bet
	chips.total -= bet
def hit(deck,hand):
	 card = deck.deck.pop(0)
	 hand.add_card(card)
global playing
def hit_or_stand(deck, hand):
	playing = True
	while playing == True:
		play = input('Would you like to hit or stand. Enter "h" hit or "s" to stand.')
		if play.lower() == 'h':
			hit(deck,hand)
			print('\n' *100)
			show_some(player_hand, dealer_hand)
			#print('Total Value: ' + str(hand.value))
			if (player_hand.value > 21 and player_hand.aces > 0):
				player_hand.value -= 10
				player_hand.aces -= 1
				print('\n' *100)
				print('Ace can only be used as rank 1.')
				show_some(player_hand, dealer_hand)
		elif play.lower() == 's':
			print('Dealers Turn to play')
			playing = False
			break
		else:
			print('I did not understand that!')
			continue
def show_some(player,dealer):
	table = ""
	for i in range(len(dealer.cards)):
		if i == 0:
			table +=  '|    |'
		else:
			if dealer.cards[i].number <= 9:
				n = str(dealer.cards[i].number) + ' '
				table +=  '| ' + n + ' |'
			else:
				table +=  '| ' + str(dealer.cards[i].number) + ' |'
	table += '\n'
	for i in range(len(dealer.cards)):
		if i == 0:
			table +=  '|    |'
		else:
			table +=  '| ' + str(dealer.cards[i].suit) + '  |' 
	table += "\n\n\n"
	for card in player.cards:
		if card.number <= 9:
			n = str(card.number) + ' '
			table +=  '| ' + n + ' |'
		else:
			table +=  '| ' + str(card.number) + ' |'	
	table += '\n'
	for card in player.cards:
		table +=  '| ' + str(card.suit) + '  |'
	print(table)
	print('Total value of player: ' + str(player.value))
def show_all(player,dealer):
	table = ""
	for card in dealer.cards:
		if card.number <= 9:
			n = str(card.number) + ' '
			table +=  '| ' + n + ' |'
		else:
			table +=  '| ' + str(card.number) + ' |'
	table += '\n'
	for card in dealer.cards:
		table +=  '| ' + str(card.suit) + '  |'
	table += '\nTotal value of dealer: ' + str(dealer.value)
	table += "\n\n\n"
	for card in player.cards:
		if card.number <= 9:
			n = str(card.number) + ' '
			table +=  '| ' + n + ' |'
		else:
			table +=  '| ' + str(card.number) + ' |'
	table += '\n'
	for card in player.cards:
		table +=  '| ' + str(card.suit) + '  |'
	print(table)
	print('Total value of player: ' + str(player.value))
def player_busts(player, dealer, chips):
	print('Player Busted!')
	chips.loose_bet()
def player_wins(player, dealer, chips):
	print('Player Wins!')
	chips.win_bet()
def dealer_busts(player, dealer, chips):
	print('Dealer Busted!')
	chips.win_bet()
def dealer_wins(player, dealer, chips):
	print('Dealer Wins!')
	chips.loose_bet()
def push(player, dealer):
	chips 
	print('Tied!')

#The game starts
#Fisrt make a deck of cards and the shuffle it.
#Ask player if he is ready to play? If he is ready then we start.
player_chips = Chips()
play_again = True
while play_again == True:
	print ('Welcome to BlackJack game!')
	d = Deck()
	d.shuffle()
	ready = False
	while ready == False:
		print('Are you ready to play?')
		rea = input('If you are ready to play? Enter "y" if you are ready.')
		if rea.lower() == 'y':
			ready = True
			print("Great!The dealer will now deal the cards.")
	player_hand = Hand()
	dealer_hand = Hand()
	for i in range(2):
		card = d.deal_a_card()
		player_hand.add_card(card)
		card = d.deal_a_card()
		dealer_hand.add_card(card)
	#dealer_chips = Chips()
	take_bet(player_chips)
	print('\n' *100)
	show_some(player_hand, dealer_hand)
	hit_or_stand(d,player_hand)
	print('\n' *100)
	show_some(player_hand, dealer_hand)
	if player_hand.value > 21:
#			playing = False
		player_busts(player_hand,dealer_hand, player_chips)
	if player_hand.value <= 21:
		while dealer_hand.value < 17:
			hit(d, dealer_hand)
		print('\n' *100)
		show_all(player_hand,dealer_hand)
		if dealer_hand.value > 21:
			dealer_busts(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value > player_hand.value:
			dealer_wins(player_hand, dealer_hand, player_chips)
		elif dealer_hand.value < player_hand.value:
			player_wins(player_hand, dealer_hand, player_chips)
		else:
			push(player_hand, dealer_hand)
	print('You have %d chips left:' % player_chips.total)
	if player_chips.total <= 0:
		print('You lost all your chips.')
		print('Game Over')
		break
	next_round = input("Enter 'y' to play next round or any other key to quit game.")
	if next_round.lower() == 'y':
		continue
	else:
		break
print('You ended with %d chips left' %player_chips.total)
print ('Thank you for playing')

	
#play_game()

#print((card not in d.deck) == True)
# for card in dealer_hand.cards:
# 	print(card.__str__())
# for card in player_hand.cards:
# 		print(card.__str__())

#print (d)
#print(deck.deck)
#while True:
