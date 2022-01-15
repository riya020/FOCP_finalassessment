class teamResult():
    
    def team_name(self, value: str):
        self.team_name=value

    def P(self, value: int):
        self.P=value
    def W(self, value: int):
        self.W=value
    def D(self, value: int):
        self.D=value
    def L(self, value: int):
        self.L=value
    def F(self, value: int):
        self.F=value
    def A(self, value: int):
        self.A=value
    def Diff(self, value: int):
        self.Diff=value
    def Pts(self, value: int):
        self.Pts=value


    """description of class"""
    def __init__(self):
        self.team_name=""
        self.P=0
        self.W=0
        self.D=0
        self.L=0
        self.F=0
        self.A=0
        self.Diff=0
        self.Pts=0


