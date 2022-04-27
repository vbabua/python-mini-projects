import random
when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago','On 20th Jan']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle','a cat']
name = ['Josie', 'Lizzie','Hope', 'Landon', 'Rafael', 'MG', 'Kaleb', 'Cleo']
residence = ['USA','India', 'Germany', 'Venice', 'England']
went = ['cinema', 'park','seminar', 'school', 'aquarium']
happened = ['read a book', 'solved a problem', 'coded for a problem', 'learned to sing']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
