import sys
from random import *
import tkinter as tk

class Card:
   symbol = ''
   value = 0
   
   def __init__(self, symbol, value):
      self.symbol = symbol
      self.value = value
   
   def getSymbol(self):
      return self.symbol
   
   def getValue(self):
      return self.value
   
   def getValueForShow(self):
      if self.value <= 10:
         return str(self.value)
      elif self.value == 12:
         return 'J'
      elif self.value == 13:
         return 'Q'
      elif self.value == 14:
         return 'k'
      else:
         return 'A'
   
   def printCard(self):
      print("Symbol:", self.getSymbol(), ", Value:", self.getValue())
      
class Player:
   cards = list()
   score = 0
   name = ''
   def __init__(self, cards, name):
      self.cards = cards
      self.name = name
      
   def getCards(self):
      return self.cards
   
   def getCards(self):
      return self.cards
   
   def getScore(self):
      return self.score
   
   def getName(self):
      return self.name
   
   def getCurrentStatusInGame(self):
      return self.getName() + " Cards: " + str(len(self.getCards())) + " Score: " + str(self.getScore())
   
   def addCard(self, card):
      self.cards.append(card)
   
   def addCards(self, cards):
      self.cards = self.cards + cards
   
   def removeFirstCard(self):
      self.cards.pop(0)
      
   def increaseScore(self):
      self.score = self.score + 1
   
   def setFirstCard(self, card):
      self.cards[0] = card
   
   def setCards(self, cards):
      self.cards = cards
      
class Game:
   player1 = Player([], '')
   player2 = Player([], '')
   window = tk.Tk()
   spadeImg = tk.PhotoImage(file = 'spade.png')
   diamondImg = tk.PhotoImage(file = 'diamond.png')
   clubImg = tk.PhotoImage(file = 'club.png')
   heartImg = tk.PhotoImage(file = 'heart.png')
   nextCardButton = tk.Button('')
   war = False
   cardsForWinner = list()
   winner = Player([], '')
   draw = False
   nrCartiDeDat = 0
   bgImg = tk.PhotoImage(file='bg.png')
   
   def __init__(self, player1, player2):
      self.player1 = player1
      self.player2 = player2
      self.start()
   
   def start(self):
      self.setWindowSettings()
      self.setDefaultBg()
      self.setPlayersLables()
      self.setNextCardButton()
      self.setWarButton()
      self.window.mainloop()
   
   def setWindowSettings(self):
      self.window.geometry('900x400')
      self.window.title("War")
   
   def setNextCardButton(self):
      self.nextCardButton = tk.Button(self.window, text="Next Card", width = 20, command = self.giveNextCard)
      self.nextCardButton.place(x = 400, y = 300)
   
   def setWarButton(self):
      self.nextCardButton = tk.Button(self.window, text="War", width = 20, command = self.warCase)
      self.nextCardButton.place(x = 400, y = 270)
         
   def setPlayersLables(self):
      labelPlayer1 = tk.Label(self.window, 
                     text = self.player1.getCurrentStatusInGame(),
                     bd = '1', relief = 'sunken').place(x = 20, y = 20)
      
      labelPlayer2 = tk.Label(self.window, 
                     text = self.player2.getCurrentStatusInGame(),
                     bd = '1', relief = 'sunken').place(x = 725, y = 20)

   def setWinner(self, player):
      self.winner = player
      
   def setCardsLabels(self, cardPlayer1, cardPlayer2):
      cardPlayer1Value = cardPlayer1.getValueForShow()
      cardPlayer2Value = cardPlayer2.getValueForShow()
      
      cardPlayer1Symbol = self.getSymbolForShow(cardPlayer1.getSymbol())
      cardPlayer2Symbol = self.getSymbolForShow(cardPlayer2.getSymbol())
      
      labelCardPlayer1 = tk.Label(self.window,
                                 text = cardPlayer1Value,
                                 bd = '1', relief = 'sunken',
                                 height = 400, width = 140, 
                                 image =  cardPlayer1Symbol, compound = 'top',
                                 font = ('Ariel', 100)).place(x = 20, y = 40)
      
      labelCardPlayer2 = tk.Label(self.window,
                                 text = cardPlayer2Value,
                                 bd = '1', relief = 'sunken',
                                 height = 400, width = 140, 
                                 image =  cardPlayer2Symbol, compound = 'top',
                                 font = ('Ariel', 100)).place(x = 725, y = 40)
   
   def setNrDeCartiDeDat(self):
      if self.cardsForWinner[-1].getValue() != 100:
         self.nrDeCartiDeDat = min(self.cardsForWinner[-1].getValue(), min(len(self.player1.getCards()), len(self.player2.getCards())))
      else:
         self.nrDeCartiDeDat = min(11, min(len(self.player1.getCards()), len(self.player2.getCards())))
           
   def setDefaultBg(self):
      labelBg = tk.Label(self.window, image = self.bgImg)
      labelBg.place(x = 0, y = 0)
      #labelBg2 = tk.Label(self.window, image = self.bgImg)
      #labelBg2.place(x = 481, y = 0)
         
   def getSymbolForShow(self, symbol):
      if symbol == 'diamond':
         return self.diamondImg
      elif symbol == 'heart':
         return self.heartImg
      elif symbol == 'club':
         return self.clubImg
      else:
         return self.spadeImg
      
   def giveNextCard(self):
      if self.war == False:
         if len(self.player1.getCards()) == 0 and len(self.player2.getCards()) == 0:
            self.draw = True
            self.showWinner()
            
         if len(self.player1.getCards()) > 0 or len(self.player2.getCards()) > 0:
            if len(self.player1.getCards()) == 0:
               self.setWinner(self.player2)
               self.showWinner()
            elif len(self.player2.getCards()) == 0:
               self.setWinner(self.player1)
               self.showWinner()
         
         player1Card = self.player1.getCards()[0]
         player2Card = self.player2.getCards()[0]
         self.setCardsLabels(player1Card, player2Card)
         self.player1.removeFirstCard()
         self.player2.removeFirstCard()
         
         self.cardsForWinner = [player1Card, player2Card]

         if player1Card.getValue() > player2Card.getValue():
            self.player1.addCards(self.cardsForWinner)
            self.cardsForWinner = list()
            self.player1.increaseScore()
         elif player1Card.getValue() < player2Card.getValue():
            self.player2.addCards(self.cardsForWinner)
            self.cardsForWinner = list()
            self.player2.increaseScore()
         else:
            self.setNrDeCartiDeDat()
            self.war = True
            
         self.setPlayersLables()
            
   def warCase(self):
      if self.war == True:
         if len(self.player1.getCards()) == 0 and len(self.player2.getCards()) == 0:
            self.draw = True
            self.showWinner()
            
         if self.nrDeCartiDeDat > 0:
               lastCardPlayer1 = self.player1.getCards()[0]
               lastCardPlayer2 = self.player2.getCards()[0]
               self.cardsForWinner.append(lastCardPlayer1)
               self.cardsForWinner.append(lastCardPlayer2)
               self.player1.removeFirstCard()
               self.player2.removeFirstCard()
               self.setCardsLabels(lastCardPlayer1, lastCardPlayer2)
               self.nrDeCartiDeDat = self.nrDeCartiDeDat - 1

               self.setPlayersLables()
         else:
            lastCardPlayer2 = self.cardsForWinner[len(self.cardsForWinner) - 1]
            lastCardPlayer1 = self.cardsForWinner[len(self.cardsForWinner) - 2]
            
            if(lastCardPlayer1.getValue() == lastCardPlayer2.getValue()):
               self.setNrDeCartiDeDat()   
            else:   
               if lastCardPlayer1.getValue() > lastCardPlayer2.getValue():
                  self.player1.addCards(self.cardsForWinner)
                  self.cardsForWinner = list()
                  self.player1.increaseScore()
               elif lastCardPlayer1.getValue() < lastCardPlayer2.getValue():
                  self.player2.addCards(self.cardsForWinner)
                  self.cardsForWinner = list()
                  self.player2.increaseScore()
               self.war = False

            self.setPlayersLables()
         
            if len(self.player1.getCards()) == 0:
               self.setWinner(self.player1)
               self.showWinner()
            elif len(self.player2.getCards()) == 0:
               self.setWinner(self.player2)
               self.showWinner()
      
   def showWinner(self):
      for widget in self.window.winfo_children():
         widget.destroy()
      self.setDefaultBg()
      if self.draw == False:
         labelWinner= tk.Label(self.window, 
                              text = "Congrat " + self.winner.getName() + " you are the winner!",
                              bd = '1', relief = 'sunken',
                              font = ('Ariel', 30)).pack()
      else:
         labelWinner= tk.Label(self.window, 
                              text = "Draw",
                              bd = '1', relief = 'sunken',
                              font = ('Ariel', 50)).pack()
 
def createDeck():
   deck = list()
   symbols = ['club', 'diamond', 'heart', 'spade']
   for a in symbols:
      for i in range(2, 11):
         deck.append(Card(a, i))
      for i in range(12, 15):
         deck.append(Card(a, i))
      deck.append(Card(a, 100))
   return deck

def shuffleDeck(deck):
   shuffledDeck = list()
   for i in range(1, 53):
      randomNr = randint(1, 53-i)
      shuffledDeck.append(deck[randomNr - 1])
      deck.pop(randomNr - 1)
   return shuffledDeck

def caseDoubleWar(player1, player2):
   cardsForPlayer1[0] = Card('diamond', 2)
   cardsForPlayer2[0] = Card('heart', 2)
   
   cardsForPlayer1[2] = Card('diamond', 4)
   cardsForPlayer2[2] = Card('heart', 4)
   
   return [player1, player2]

def caseDraw(player1, player2):
   player1.setCards([Card('diamond', 2)])
   player2.setCards([Card('heart', 2)])

   return [player1, player2]

def caseP1Wins(player1, player2):
   player1.setCards([Card('diamond', 3)])
   player2.setCards([Card('heart', 2)])

   return [player1, player2]

def caseWarWithNotEnoughCards(player1, player2):
   player1.setCards([Card('diamond', 4)])
   player2.setCards([Card('heart', 4)])
   
   player1.addCard(Card("heart" , 2))
   player1.addCard(Card("diamond", 13))
   player1.addCard(Card("diamond", 9))
   player1.addCard(Card("diamond", 5))
   player1.addCard(Card("diamond", 6))
   
   player2.addCard(Card("heart" , 5))
   player2.addCard(Card("heart" , 6))
   player2.addCard(Card("heart" , 100))
   
   return [player1, player2]
   
def startGame(player1, player2):
   #player1 = caseDoubleWar(player1, player2)[0]
   #player2 = caseDoubleWar(player1, player2)[1]
   
   #player1 = caseDraw(player1, player2)[0]
   #player2 = caseDraw(player1, player2)[1]
   
   player1 = caseP1Wins(player1, player2)[0]
   player2 = caseP1Wins(player1, player2)[1]
   
   #player1 = caseWarWithNotEnoughCards(player1, player2)[0]
   #player2 = caseWarWithNotEnoughCards(player1, player2)[1]
   
   game = Game(player1, player2)
   
if __name__ == '__main__':
   deck = shuffleDeck(createDeck())
   cardsForPlayer1 = list()
   cardsForPlayer2 = list()
   for i in range(0, 26):
      cardsForPlayer1.append(deck[i])
      cardsForPlayer2.append(deck[51 - i])
      
   player1 = Player(cardsForPlayer1, "Player")
   player2 = Player(cardsForPlayer2, "Computer")
   startGame(player1, player2)
   

   
   
