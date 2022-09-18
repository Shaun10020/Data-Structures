# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems=dict()

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            array=[]
            if query.ind in self.elems:
                for x in reversed(range(len(self.elems[query.ind]))):
                    array.append(self.elems[query.ind][x].s)
            self.write_chain(array)
        else:
            if query.type == 'find':
                flag=0
                if self._hash_func(query.s) in self.elems:
                    for obj in self.elems[self._hash_func(query.s)]:
                        if obj.s==query.s:
                            self.write_search_result(True)
                            flag=1
                if flag==0:
                    self.write_search_result(False)
            elif query.type == 'add':
                if self._hash_func(query.s) in self.elems:
                    for obj in self.elems[self._hash_func(query.s)]:
                        if obj.s==query.s:
                            break
                    else:
                        self.elems[self._hash_func(query.s)].append(query)
                else:
                    self.elems[self._hash_func(query.s)]=[query]
            else:
                if self._hash_func(query.s) in self.elems:
                    for j in range(len(self.elems[self._hash_func(query.s)])):
                        if self.elems[self._hash_func(query.s)][j].s==query.s:
                            self.elems[self._hash_func(query.s)].pop(j)
                            break

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
