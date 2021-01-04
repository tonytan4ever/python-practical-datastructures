class CountingBloomFilter:
    '''
    Implementation of a Counting Bloom Filter (CBF)
    As a replacement of HashMap (map). In use cases where
    space is limited, CBF can be a very useful replacement
    of HashMap. Its disadvantage is its count might actually be 
    larger than 
    '''
    CAP = 10 ** 6
    
    def __init__(self, k):
        # do intialization if necessary
        self.hash_count = k
        self.word_count_array = [ 0 for i in range(self.CAP + k) ]

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        # write your code here
        for i in range(self.hash_count): 
            # create digest for given item. 
            # i work as seed as self.makeHashhash() function 
            # With different seed, digest created is different 
            digest = self.make_hash(word, i)
  
            # set the bit True in bit_array 
            self.word_count_array[digest] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        # write your code here
        if self.contains(word):
            for i in range(self.hash_count): 
                # create digest for given item. 
                # i work as seed as self.makeHashhash() function 
                # With different seed, digest created is different 
                digest = self.make_hash(word, i)
                self.word_count_array[digest] -= 1
                

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        # write your code here
        for i in range(self.hash_count): 
            # create digest for given item. 
            # i work as seed as self.makeHashhash() function 
            # With different seed, digest created is different 
            digest = self.make_hash(word, i)
            if self.word_count_array[digest] == 0:
                return False
        else:
            return True
    
    """
    @param: word: A string
    @return: True if contains word
    """
    def get_count(self, word):
        # write your code here
        # for Counting Bloom Filter:
        # get the int value on k positions, and return 
        # the smallest count
        cnt = 0
        for i in range(self.hash_count): 
            # create digest for given item. 
            # i work as seed as self.makeHashhash() function 
            # With different seed, digest created is different 
            digest = self.make_hash(word, i)
            cnt = min(cnt, self.word_count_array[digest])
        return cnt
    
    
    def make_hash(self, s, seed):
        res_hash = 0
        for char in s:
            res_hash = (res_hash * (seed * 2 + 3) + ord(char)) % (self.CAP + self.hash_count)
        return res_hash