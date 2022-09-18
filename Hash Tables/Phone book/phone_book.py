# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def hash_function(x):
    p=1000003
    a=50
    b=4
    m=1000
    return (((a*x)+b)%p)%m

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    contacts = dict()
    for cur_query in queries:
        key=hash_function(cur_query.number)
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            if key in contacts:
                for contact in contacts[key]:
                    if contact.number == cur_query.number:
                        contact.name = cur_query.name
                        break
                else: # otherwise, just add it
                    contacts[key].append(cur_query)
            else:
                contacts[key]=[cur_query]
        elif cur_query.type == 'del':
            if key in contacts:
                for j in range(len(contacts[key])):
                    if contacts[key][j].number == cur_query.number:
                        contacts[key].pop(j)
                        break
        else:
            response = 'not found'
            if key in contacts:
                for contact in contacts[key]:
                    if contact.number == cur_query.number:
                        response = contact.name
                        break
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

