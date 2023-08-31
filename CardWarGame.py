from random import shuffle
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}
no_of_players=2


class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return f'{self.suit} {self.value}.'

class Deck:
    def __init__(self):
        self.card_deck=[]
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.card_deck.append(card)

    def shuffle_deck(self):
        shuffle(self.card_deck)

    def deal_single_card(self):
        # deal means distributing card to a player
        try:
            return self.card_deck.pop(0)            
        except Exception as e:
            print(e)

class Player:
    def __init__(self,name):
        self.name=name
        self.my_cards = []

    def draw_card(self):
        return self.my_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards)== type([]):
            self.my_cards.extend(new_cards)
        else:
             self.my_cards.append(new_cards)   

deck = Deck()
deck.shuffle_deck()

player_one = Player('One')
player_two = Player('Two')

for i in range(26):
    player_one.add_cards(deck.deal_single_card())
    player_two.add_cards(deck.deal_single_card())

game_on=True
game_round=0
while game_on:
    game_round+=1
    print(f"Round - {game_round}")
    if len(player_one.my_cards)==0:
        print("!!!!Player one out of cards. Player two wins!!!!!")
        game_on=False
        break
    elif len(player_two.my_cards)==0:
        print("!!!!Player two out of cards. Player one wins!!!!!")
        game_on=False
        break

    player_one_table_cards=[]
    drawn_card = player_one.draw_card()
    player_one_table_cards.append(drawn_card)
    print(drawn_card)

    player_two_table_cards=[]
    drawn_card = player_two.draw_card()
    player_two_table_cards.append(drawn_card)
    print(drawn_card)

    at_war=False
    if player_one_table_cards[-1].value>player_two_table_cards[-1].value:
        player_one_table_cards.extend(player_two_table_cards)
        player_one.add_cards(player_one_table_cards)
    
    elif player_one_table_cards[-1].value<player_two_table_cards[-1].value:
        player_two_table_cards.extend(player_one_table_cards)
        player_two.add_cards(player_two_table_cards)
       
    elif player_one_table_cards[-1].value==player_two_table_cards[-1].value:
        print("WAR!")
        at_war=True
      
    while at_war:

        if len(player_one.my_cards)==0:
            print("!!!!Player one out of cards. Player two wins!!!!!")
            game_on=False
            at_war= False
            break
        elif len(player_two.my_cards)==0:
            print("!!!!Player two out of cards. Player one wins!!!!!")
            game_on=False
            at_war= False
            break

        drawn_card = player_one.draw_card()
        player_one_table_cards.append(drawn_card)
        print(drawn_card)    
        
        drawn_card = player_two.draw_card()
        player_two_table_cards.append(drawn_card)
        print(drawn_card)

        if player_one_table_cards[-1].value>player_two_table_cards[-1].value:
           player_one_table_cards.extend(player_two_table_cards)
           player_one.add_cards(player_one_table_cards)
           at_war=False
           break

        elif player_one_table_cards[-1].value<player_two_table_cards[-1].value:
           player_two_table_cards.extend(player_one_table_cards)
           player_two.add_cards(player_two_table_cards)
           at_war=False
           break    


