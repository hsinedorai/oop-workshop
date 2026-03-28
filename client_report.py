import psycopg2
import psycopg2.extras
from client import Client
from clientOut import ClientOut



class ClientReport (ClientOut):
    def __init__(self,firstname,lastname, total_balance,id):
        
        #heritage de la class client 
        super().__init__(firstname,lastname,id)
        
        self.total_balance = total_balance
    
    # m andha hata relation mel class 
    @staticmethod
    def __connect (): 
        return psycopg2.connect(
            dbname="bankapp",
            user="myuser",
            password="mypass",
            host="localhost")
        print("welcome ")
  
    @classmethod                
    def get_clientby_id(cls,id):
         conn =cls.connect() 
            
         with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    # cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR);")
                    cur.execute(""" SELECT c.id AS id,
                                c.firstname AS firstname,
                                c.lastname AS lastname,
                                SUM(a.balance) AS total_balance
                                FROM clients AS c
                                JOIN accounts AS a
                                ON c.id=a.client_id
                                WHERE c.id= %s
                                GROUP BY c.id , c.firstname,c.lastname;
                                """, (id,))
                    client=cur.fetchone()
                    if not client:
                        return None
                    return ClientReport(**client)
                except Exception as e  :
                    print(f"try again : {e}")   
                   

    
    
    
   
    def __repr__(self):
        return super().__repr__() +"******"+ (str)(self.total_balance)

    def ab(self):
        print("hellooo")
# create instance of class client 
a=ClientReport("hass","dor",23,5)
print(a)
print(a.ab())
#print(a.__connect())

# client2=Client("ali","t1")
# client2.add_user_in_db()
# client=ClientReport.get_clientby_id(3)
# print(client.id)
# print(client)

