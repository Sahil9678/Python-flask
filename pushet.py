from pushetta import Pushetta
                 
API_KEY="019c881997e32c0fe1919ea546e851c4ad453508"
CHANNEL_NAME="MyArduino9678"
p=Pushetta(API_KEY)
p.pushMessage(CHANNEL_NAME, "Hello World")