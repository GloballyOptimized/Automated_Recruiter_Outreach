import smtplib
import dns.resolver
import os 
from dotenv import load_dotenv
#.........................................................................................................
load_dotenv() # load all environment variables ...
#.........................................................................................................

def get_mx_record(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = records[0].exchange.to_text()
        return mx_record
    except:
        return None
#..........................................................................................................

def verify_email(email:str):
    domain = email.split('@')[1]
    mx_record = get_mx_record(domain)
    
    if mx_record:
        try:
            server = smtplib.SMTP(timeout=10)
            server.set_debuglevel(0)  # To disable verbose output, set it to 0
            server.connect(mx_record)
            server.helo(mx_record)
            server.mail(os.getenv('YAHOO_EMAIL'))  # Replace with any valid email
            code, message = server.rcpt(email)  # The actual recipient email you're checking
            server.quit()

            if code == 250:
                return True
            else:
                return False, f"Invalid Email: {message.decode('utf-8')}"
        except Exception as e:
            return False, f"Error occurred: {str(e)}"
    else:
        return False
#............................................................................................................

def email_generator(full_name:str,domain:str):
    
    # Considering the full name to be Ayush Rai and domain to be abc.com here's examples : 
    name = full_name.split(' ')
    email_list = (   name[0]+'@'+domain #ayush@abc.com
                    ,name[0]+'.'+name[1]+'@'+domain #ayush.rai@abc.com 
                    ,name[0][0]+'.'+name[1]+'@'+domain #a.rai@abc.com
                    ,name[0]+name[1]+'@'+domain #ayushrai@abc.com
                    ,name[1]+name[0]+'@'+domain #raiayush@abc.com
                    ,name[0]+name[1][0]+'@'+domain #ayushs@abc.com
                    ,name[0]+'.'+name[1][0]+'@'+domain #ayush.s@abc.com
                    ,name[1][0]+'.'+name[0]+'@'+domain # rai.ayush@abc.com
                    ,name[0]+'_'+name[1]+'@'+domain #ayush_rai@abc.com
                    ,name[1]+'.'+name[0][0]+'@'+domain #rai.a@abc.com 
                    ,name[1]+'.'+name[0]+'@'+domain #rai.ayush@abc.com
                    ,name[0][0]+'.'+name[1][0]+'@'+domain #a.r@abc.com 
                )
    return email_list

#...........................................................................................................

 

    
    
