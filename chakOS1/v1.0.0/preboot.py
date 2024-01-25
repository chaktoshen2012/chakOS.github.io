class Preboot:
    def __init__(self):
        self.corrupted = False
        self.chakOS_version = 'NaN'
        self.list = ['v1.0.0']

    def check(self):
        if self.chakOS_version in self.list:
            self.corrupted = False
        elif self.chakOS_version not in self.list:
            self.corrupted = True
