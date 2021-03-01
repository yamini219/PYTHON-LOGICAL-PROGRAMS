class employee():
  def info(self):
    print("ravi","25k")
ravi=employee()
employee.info(ravi)
ravi.info()
print()

class employee():
  def __init__(self):
    print("ravi","25k")
ravi=employee()
print()

class employee():
  def __init__(self,e1,e2,e3):
    self.e1=e1
    self.e2=e2
    self.e3=e3
    print("information of employee:",self.e1,self.e2,self.e3)
e1=employee("ravi","25k","615")
e2=employee("sam","30k","616")
e3=employee("som","45k","617")
