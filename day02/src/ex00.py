class key(object):

    def __init__(self):
        self.passphrase = "zax2rulez"
        
    def __len__(self):
        return 1337
        
    def __gt__(self, other):
        return other < 9001
        
    def __getitem__(self, index):
        if index == 404:
            return 3
        raise IndexError("404")
        
    def __str__(self):
        return "GeneralTsoKeycard"