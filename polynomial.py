class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
      
    def evaluate(self, x):
      return x
    


class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)
      
    def evaluate(self, i):
      return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
          if isinstance(self.p1, Div or Sub or Mul):
            #If p1 is an add
              if isinstance(self.p2, Div or Sub or Mul):
                #Both p1 p2 are add
                  return "( " + repr(self.p1) + " ) + ( " + repr(self.p2) + " )"
                #return (p1) * (p2)
              return "( " + repr(self.p1) + " ) + " + repr(self.p2)
              #only p1 is add, return (p1) * p2
          if isinstance(self.p2, Div or Sub or Mul):
              return repr(self.p1) + " + ( " + repr(self.p2) + " )"
            #return p1 * (p2)
          return repr(self.p1) + " + " + repr(self.p2)
        #else return p1 * p2
      
    def evaluate(self, x):
      return self.p1.evaluate(x) + self.p2.evaluate(x)
      
class Div:
  def __init__(self, p1, p2) :
      self.p1 = p1
      self.p2 = p2
  def __repr__(self):
          if isinstance(self.p1, Add or Sub or Mul):
            #If p1 is an add
              if isinstance(self.p2, Add or Sub or Mul):
                #Both p1 p2 are add
                  return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
                #return (p1) * (p2)
              return "( " + repr(self.p1) + " ) / " + repr(self.p2)
              #only p1 is add, return (p1) * p2
          if isinstance(self.p2, Add or Sub or Mul):
              return repr(self.p1) + " / ( " + repr(self.p2) + " )"
            #return p1 * (p2)
          return repr(self.p1) + " / " + repr(self.p2)
        #else return p1 * p2
        
  def evaluate(self, x):
      if self.p2.evaluate(x) == 0:
          return "divide by zero error"
      return self.p1.evaluate(x) / self.p2.evaluate(x)
    
class Sub:
  def __init__(self, p1, p2) :
      self.p1 = p1
      self.p2 = p2
      
  def __repr__(self):
          if isinstance(self.p1, Add or Div or Mul):
            #If p1 is an add
              if isinstance(self.p2, Add or Div or Mul):
                #Both p1 p2 are add
                  return "( " + repr(self.p1) + " ) - ( " + repr(self.p2) + " )"
                #return (p1) * (p2)
              return "( " + repr(self.p1) + " ) - " + repr(self.p2)
              #only p1 is add, return (p1) * p2
          if isinstance(self.p2, Add or Div or Mul):
              return repr(self.p1) + " - ( " + repr(self.p2) + " )"
            #return p1 * (p2)
          return repr(self.p1) + " - " + repr(self.p2)
        #else return p1 * p2
  
  def evaluate(self, x):
    return self.p1.evaluate(x) - self.p2.evaluate(x)
      

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add or Sub or Div):
          #If p1 is an add
            if isinstance(self.p2, Add or Sub or Div):
              #Both p1 p2 are add
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
               #return (p1) * (p2)
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
            #only p1 is add, return (p1) * p2
        if isinstance(self.p2, Add or Sub or Div):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
          #return p1 * (p2)
        return repr(self.p1) + " * " + repr(self.p2)
      #else return p1 * p2
      
    def evaluate(self, x):
      return self.p1.evaluate(x) * self.p2.evaluate(x)  


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(3))