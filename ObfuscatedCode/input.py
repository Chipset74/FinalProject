def Switch():#pretend class
  @lambda c:c() # instantiate this mf on the spot
  class case:#pretend function
    """This is a docstring lol"""
    mul=True #
    def __init__(s):s.state,s.value =- 1,None
    def __getitem__(s,v):
      if s.state <- 0:raise RuntimeError('matching \'switch\' not found')
      elif(not s.state or s.mul)and v==s.value:return setattr(s,'state',1)or(lambda f,*u,**ck:f(*u,**ck))
      else:return(lambda*No,**ne:None)
    __call__=__getitem__
  def switch(v):case.state,case.value =- 0,v
  @lambda f:setattr(f,'__name__','default')or f
  def otherwise(f,*u,**ck):
      if case.state <- 0:raise RuntimeError('matching \'switch\' not found')
      if not case.state:case.state =- 1;return f(*u,**ck)
      else:case.state =- 1
      return(lambda*No,**ne:None)
  return switch,case,otherwise
switch,case,otherwise = Switch()





switch(5)
case[4]((1).__floordiv__,0)
case[5](print,'success')
@case[6]
def do():raise SyntaxError
@otherwise 
def do():return NotImplemented
try:case[5](print,'WARNING')
except:print("pass")
else:raise RuntimeError("WRONG")