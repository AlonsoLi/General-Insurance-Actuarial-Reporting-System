# import packages

# Define Class Process
class Process:
    def __int__(self, VY, VQ):
        self.VY = VY #valuation year
        self.VQ = VQ #valuation quarter
    
    def read_data(self):
        print('reading data from data base')
        self.df_main = get_data() # another function to get data from data base
        print('data ready')

    def calculate(self):
    
    def save_results(self):
    
    def export():


if __name__ == "__main__"
    process = Process (VY,VQ)
    process.read_data()
    process.calculate()
    process.save_results()
    process.export()
