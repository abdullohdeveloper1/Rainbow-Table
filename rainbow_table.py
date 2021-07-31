with open ('nist_10000.txt', newline = '') as bad_passwords:
  nist_bad = bad_passwords.read().split('\n')
print(nist_bad[1:10])

leaked_users_table = {
    'jamie': {
        'username': 'jamie',
        'role': 'subscriber',
        'md5': '203ad5ffa1d7c650ad681fdff3965cd2'
    }, 
    'amanda': {
        'username': 'amanda',
        'role': 'administrator',
        'md5': '315eb115d98fcbad39ffc5edebd669c9'
    }, 
    'chiaki': {
        'username': 'chiaki',
        'role': 'subscriber',
        'md5': '941c76b34f8687e46af0d94c167d1403'
    }, 
    'viraj': {
        'username': 'viraj',
        'role': 'employee',
        'md5': '319f4d26e3c536b5dd871bb2c52e3178'
    },
}

import hashlib
word = 'blueberry'
print(hashlib.md5(word.encode()).hexdigest())

rainbow_table = {}
for word in nist_bad:
  hashed_word = hashlib.md5(word.encode()).hexdigest()
  rainbow_table[hashed_word] = word

for user in leaked_users_table.keys():
  try:
    print(user + ":\t" + rainbow_table[leaked_users_table[user]['md5']])
  except:
    print(user + ":\t" + '******* hash not found in rainbow table')