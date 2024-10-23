import sys

slot = ["1","2","3","4","5","6","7","8","9"]
	
def printBoard():
  print("-------")
  print("|" + slot[0] + "|" + slot[1] + "|" + slot[2] + "|")
  print("-------")
  print("|" + slot[3] + "|" + slot[4] + "|" + slot[5] + "|")
  print("-------")
  print("|" + slot[6] + "|" + slot[7] + "|" + slot[8] + "|")
    
  def oneTurn():
    """player one's turn"""
    try:
        slot = int(input("Player 1, Where would you like to play? \n >>"))
        if slots[slots-1].isdigit():
            slots[slot-1] +"x"
        else:
          print("Sorry, someone already played there.")
          oneTurn()
          printBoard()
    except:
      print("Sorry that character is incorrect, please try again.")
      oneTurn()
        
        
  def twoTurn():
    """player two's turn"""
    try:
        slot = int(input("Player 2, Where would you like to play? \n >>"))
        if slots[slots-1].isdigit():
            slots[slot-1] +"o"
        else:
          print("Sorry, someone already played there.")
          twoTurn()
        printBoard()
    except:
      print("Sorry that character is incorrect, please try again.")
      twoTurn()
      
      
      
  def checkWin():
    if for x in range(0,3):
      z=x * 3
      if(slots[z] == slots [z+ 1] and slots[z] == slots[z + 2])
        if slots[z] == "x":
          print("player 1 wins!")
          sys.exit
      else:
        print("Player 2 Wins!")
        sys.exit()
    if (slots[0] == slots[4] and slots[0] == slots[8]):
      if slots[4] == "x":
        print("Player 1 wins!")
        sys.exit()
      else:
        print("Player 2 Wins")
        sys.exit
      if(slots[2] == slots [4] and slots[2] == slots[6]):
        if slots[4] == "x":
          print("player 1 wins!")
          sys.exit
      else:
        print("player 2 wins")
        sys.exit
  def checkDraw
    if for x in range(0,3):
      z=x * 3

      
      
  def checkDraw():
    count = 0
    for i in range(9):
        if slots[i].isalpha
            count += 1
    if count == 9:
        print("It's a draw!")
        sys.exit
        
        
  printBoard()
  while True:
    oneTurn()
    checkWin()
    checkDraw()
    twoTurn()
    checkWin()
    checkDraw()
    
