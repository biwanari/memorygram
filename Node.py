class Node:
    
    def __init__(self, profileTarget, username = None, password = None):
        self.profileTarget = profileTarget
        self.username = username
        self.password = password
        
    
    
    def getProfileTarget(self):
        return self.profileTarget

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password
    


