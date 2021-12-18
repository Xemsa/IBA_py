import configparser
from pzz_lib import workname

class pzzconfig:
    def __init__(self, name='pzz_config.ini'):  
        self.config = configparser.ConfigParser()
        self.configname = workname( name)
        self.config.read(self.configname)
        self.DB = workname(self.config["DB"]['Name'])
        self.csv= workname(self.config["New_File"]['Name'])
    


if __name__ == '__main__':
    con=pzzconfig()
    print(con.DB)
    print(con.csv)
