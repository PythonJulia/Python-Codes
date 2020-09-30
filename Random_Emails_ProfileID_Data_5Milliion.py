import random
import time
import pandas as pd
import pickle as save
domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]

def get_one_random_domain(domains):
        return domains[random.randint( 0, len(domains)-1)]


def get_one_random_name(letters):
    email_name = ""
    for i in range(7):
        email_name = email_name + letters[random.randint(0,11)]
    return email_name


emails = []
prof_ids = []
def generate_random_emails():

    for i in range(0,5000000):
         one_name = str(get_one_random_name(letters))
         one_domain = str(get_one_random_domain(domains))         
         emails.append(one_name  + "@" + one_domain)
         prof_ids.append(one_name[0:5] + '_0' + str(i)[0:4] )


generate_random_emails()
#Email_Data = pd.Series({"Email_ID": emails})
Email_Data = pd.DataFrame({'Email_ID':emails, 'Profile_IDs':prof_ids})

Email_Data.to_csv("Email_Data.csv")

data = pd.read_csv("Email_Data.csv")

print (data.head())