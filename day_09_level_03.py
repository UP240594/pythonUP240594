
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
'''*1'''
if 'skills' in person:
    skillz=person['skills']
    middle=len(skillz) //2
    print('Middle skills: ',skillz[middle])
else:
    print('nothing')
'''*2'''
if 'skills' in person:
    is_so= 'Python' in person['skills']
    if is_so == True:
        print('Yes he news python')
    else:
        print('No he donsent knew python')
else:
    print('the person dosent have skills')
'''*3'''
skills1=person['skills']
if 'Javascript' and 'React' in skills1:
    print('He is a front end developer')
elif 'Node' and 'Python' and 'MongoDB' in skills1: 
    print('He is a backend developer')
elif 'React' and 'Node' and 'MongoDB' in skills1: 
    print('He is a fullstack developer')
else:
    print('unknown title')

'''*4'''
status=person['is_marred']
country=person['country']

if person['is_marred'] and person['country'] == 'Finland':
    status='married'
    print('\t', person['first_name'],'\n',person['last_name'],' lives \n in ',person['country'], '\n He is ', status)
else:
    print('The information is not correct') 