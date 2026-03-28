import psycopg2
import psycopg2.extras



class Client:
    def __init__(self,firstname,lastname):
        assert firstname,"first name shoudn t be none "
        assert isinstance(lastname,str),"firsrt name must be string"

        self.firstname=firstname
        self.lastname=lastname
        # print("welcome ")


        #variable readonly (property)
       
    def add_user_in_db(self):
        conn = psycopg2.connect(
            dbname="bankapp", 
            user="bankappuser",
            password="1234",
            host="localhost"
        )

        with conn:
            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                try:
                    cur.execute("INSERT INTO clients (firstName, lastName) VALUES(%s, %s)", (self.firstname, self.lastname))
                except Exception as e:
                    print("fama mochkla jareb ba3ed")
                    print(e)    


 
   
    
    
                   
    def get_full_name(self):
        return self.firstname + "/" +self.lastname
    def __repr__(self):
        return self.firstname +" / "+ self.lastname + "  id =" +(str)(self.id)

# create instance of class client 

# client2=Client("ali","t1")
# client2.add_user_in_db()
# client=Client.get_clientby_id(1)


