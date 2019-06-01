#!/usr/bin/python
 
import random,sys,copy
from optparse import OptionParser
try:
  import psyco
  psyco.full()
except ImportError:
  pass
 
"""
cowboy code, but seems to work
USAGE: python prog <numberruns=1> <verbocity=False>
"""
 
class board:
  def __init__(self, list=None):
    if list == None:
      self.board = [[0 for i in range(0,8)] for j in range(0,8)]
      #initialize queens at random places
      for i in range(0,8):
        while 1:
          rand_row = random.randint(0,7)
          rand_col = random.randint(0,7)
          if self.board[rand_row][rand_col] == 0:
            self.board[rand_row][rand_col] = "Q"
            break
    #TODO raise errors if board is not right format or dimension
  #define how to print the board
  def __repr__(self):
    mstr = ""
    for i in range(0,8):
      for j in range(0,8):
        mstr = mstr + str(self.board[i][j]) + " "
      mstr = mstr + "\n"
    return (mstr)
 
class queens:
  def __init__(self, numruns, verbocity, passedboard=None):
    #TODO check options
    self.totalruns = numruns
    self.totalsucc = 0
    self.totalnumsteps = 0
    self.verbocity = verbocity
    for i in range(0,numruns):
      if self.verbocity == True:
        print ("====================")
        print ("BOARD",i)
        print ("====================")
      self.mboard = board(passedboard)
      self.cost = self.calc_cost(self.mboard)
      self.hill_solution()
 
  def hill_solution(self):
    while 1:
      currViolations = self.cost
      self.getlowercostboard()
      if currViolations == self.cost:
        break
      self.totalnumsteps += 1
      if self.verbocity == True:
        print ("Board Violations", str(self.calc_cost(self.mboard)))
        print (self.mboard)
    if self.cost != 0:
      if self.verbocity == True:
        print ("NO SOLUTION FOUND")
    else:
      if self.verbocity == True:
        print ("SOLUTION FOUND")
      self.totalsucc += 1
    return self.cost
 
  def printstats(self):
    print ("Total Runs: ", str(self.totalruns))
    print ("Total Success: ", str(self.totalsucc))
    print ("Success Percentage: ", str(float(self.totalsucc)/float(self.totalruns)))
    print ("Average number of steps: ", str(float(self.totalnumsteps)/float(self.totalruns)))
 
  def calc_cost(self, tboard):
    #these are separate for easier debugging
    totalhcost = 0
    totaldcost = 0
    for i in range(0,8):
      for j in range(0,8):
        #if this node is a queen, calculate all violations
        if tboard.board[i][j] == "Q":
          #subtract 2 so don't count self
          #sideways and vertical
          totalhcost -= 2
          for k in range(0,8):
            if tboard.board[i][k] == "Q":
              totalhcost += 1
            if tboard.board[k][j] == "Q":
              totalhcost += 1
          #calculate diagonal violations
          k, l = i+1, j+1
          while k < 8 and l < 8:
            if tboard.board[k][l] == "Q":
              totaldcost += 1
            k +=1
            l +=1
          k, l = i+1, j-1
          while k < 8 and l >= 0:
            if tboard.board[k][l] == "Q":
              totaldcost += 1
            k +=1
            l -=1
          k, l = i-1, j+1
          while k >= 0 and l < 8:
            if tboard.board[k][l] == "Q":
              totaldcost += 1
            k -=1
            l +=1
          k, l = i-1, j-1
          while k >= 0 and l >= 0:
            if tboard.board[k][l] == "Q":
              totaldcost += 1
            k -=1
            l -=1
    return ((totaldcost + totalhcost)/2)
 
  #this function tries moving every queen to every spot, with only one move
  #and returns the move that has the leas number of violations
  def getlowercostboard(self):
    lowcost = self.calc_cost(self.mboard)
    lowestavailable = self.mboard
    #move one queen at a time, the optimal single move by brute force
    for q_row in range(0,8):
      for q_col in range(0,8):
        if self.mboard.board[q_row][q_col] == "Q":
          #get the lowest cost by moving this queen
          for m_row in range(0,8):
            for m_col in range(0,8):
              if self.mboard.board[m_row][m_col] != "Q":
                #try placing the queen here and see if it's any better
                tryboard = copy.deepcopy(self.mboard)
                tryboard.board[q_row][q_col] = 0
                tryboard.board[m_row][m_col] = "Q"
                thiscost = self.calc_cost(tryboard)
                if thiscost < lowcost:
                  lowcost = thiscost
                  lowestavailable = tryboard
    self.mboard = lowestavailable
    self.cost = lowcost
 
if __name__ == "__main__":
 
  parser = OptionParser()
  parser.add_option("-q", "--quiet", dest="verbose",
                   action="store_false", default=True,
                   help="Don't print all the moves... wise option if using large numbers")
 
  parser.add_option("--numrun", dest="numrun", help="Number of random Boards", default=4,
                   type="int")
 
  (options, args) = parser.parse_args()
 
  mboard = queens(verbocity=options.verbose, numruns=options.numrun)
  mboard.printstats()