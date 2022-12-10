import math

x = 10
y = 10
l1 = 10
l2 = 10

def findXandYInArray(x, y, array):
  for (x_,y_) in array:
    if(x_ - x == 0): return True
    if(y_ - y == 0): return True

  return False

def findEffortPoint(x, y, hasTheAngles=[], hasNoAngles=[]):
  
  q1 = 0
  q2 = 0

  for q1_ in range(181):
    for q2_ in range(181):  
      q1 = math.atan2(y, x) - math.atan2(l2 * math.sin(q2_),  l1 + l2 * math.cos(q2_))
      q2 = math.atan2(y - l1 * math.sin(q1_), x - l1 * math.cos(q1_)) - q1_
      
      x2 = x + l2 * math.cos(q1)
      y2 = y + math.sin(q2)
      
      if(int(x) == int(x2) and int(y) == int(y2)): 
        # Procura se nao os pontos
        if(findXandYInArray(q1, q2, hasNoAngles)): continue

        # Limitações do servo
        if(q1<0 or q1>180): continue
        if(q2<0 or q2>180): continue
        
        return q1, q2

  return 'Not found'

# hasNoAngles = [(1.524296863762312, 0.6846171643127805)]
hasNoAngles = []
print(findEffortPoint(500, 400, hasNoAngles=hasNoAngles))
