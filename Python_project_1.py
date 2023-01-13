import clearbit, requests



clearbit.key = 'sk_9cb166128ddf1593de2821da3ae15756' #your api key goes here
 
#print(requests.get(url).json())


#Define your company here
company= input("Enter company name with .com/.in: ")


try:
    response = clearbit.Company.find(domain=company,stream=True)
except:
    print('Company not found')
    
 
url= "https://prospector.clearbit.com/v1/people/search&domain={}".format(company)

try:
    people = clearbit.Prospector.search(domain=company)['results']
except:
    print('Key_people not found')
    
   
 
def scrapper(): 
    Keypeople= []
    try:
        Name= response['name']
    except:
        Name= 'NA'
        
    try:
        Address= response['location']
    except:
        Address= 'NA'
        
    try:
        Phoneno= response['phone']
    except:
        Phoneno= 'NA'
        
    try:    
        for person in people:
            Keypeople.append(person['name']['fullName'])

    except:
        Keypeople= 'NA'
    
    return {'Name': Name, 'Address':Address,'Phone no':Phoneno, 'Key people':Keypeople }
 
datas= scrapper()
print(datas)
