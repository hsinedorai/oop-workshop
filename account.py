import psycopg2
import psycopg2.extras
from client import Client

class Account:
    def __init__(self, client_id: int, balance: float, id: int = None):
        assert isinstance(client_id, int), 'client_id should be int'
        assert isinstance(balance, float), 'balance should be float'
        client=Client.get_clientby_id(client_id)
        
        self.client_id = client_id
        assert client, 'client id is not present in table clientss'
        #self.balance = balance 
        self.__balance =float(balance)
        self.id = id
        
      
        
        
        conn = psycopg2.connect(
        dbname="bankapp",
        user="myuser",
        password="mypass",
        host="localhost")

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                  cur.execute("INSERT INTO   accounts (client_id, balance) VALUES(%s, %s)", (self.client_id, self.balance))
                except Exception as e  :
                    print(f"error try again : {e}")  
                   
       
       
       
    #getter
    @property
    def balance(self):
        return self.__balance
    
    #setter
    @balance.setter
    def balance(self,value):
        self.__balance=value
            
a=Account(3,14.3)
print(a.balance)
a.balance=80
print(a.balance)
