import hashlib
import uuid

def even_up_hashlist(transaction_hash_list):

    transaction_hashes = []

    for m in transaction_hash_list:

        transaction_hashes.append(m)
        list_length = len(transaction_hashes)

    while list_length % 2 != 0:
        transaction_hashes.append('00000000000000000000000000000000')
        list_length = len(transaction_hashes)

    return transaction_hashes

def merkel_tree_calc(hash_list):

    if len(hash_list) % 2 != 0:
        hash_list=even_up_hashlist(hash_list)

    '''enabling hash'''
    hasher = hashlib.sha256()
    temp = []
    secondary = []
    i = 0
    while (i <= len(hash_list)-1):

        temp.append(hash_list[i])
        temp.append(hash_list[i+1])
        i = i + 2

        hasher.update(temp[0] + temp[1])
        secondary.append(hasher.hexdigest())
        temp.remove(temp[0])
        temp.remove(temp[0])

    if len(secondary) == 1:
        return str(secondary[0])
    else:
        merkel_tree_calc(secondary)

file_hashes = []

for i in range(0,13):
    file_hashes.append(str(uuid.uuid1().hex))
print 'Finding the merkel tree of {0} random hashes'.format(len(file_hashes))

mroot = merkel_tree_calc(file_hashes)

print(mroot)