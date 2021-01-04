class StandardBloomFilter:
    '''
    Implementation of a Standard Bloom Filter. (SBF)
    As a replacement of HashSet (set). In use cases where
    space is limited, SBF can be a very useful replacement
    of HashSet.
    '''
    CAP = 10 ** 6
    
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.hash_count = k
        self.bit_array = [ 0 for i in range(self.CAP) ]

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        # write your code here
        for i in range(self.hash_count): 
            # create digest for given item. 
            # i work as seed as self.makeHashhash() function 
            # With different seed, digest created is different 
            digest = self.make_hash(word, i)
  
            # set the bit True in bit_array 
            self.bit_array[digest] = 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        # write your code here
        for i in range(self.hash_count): 
            # create digest for given item. 
            # i work as seed as self.makeHashhash() function 
            # With different seed, digest created is different 
            digest = self.make_hash(word, i)
            if not self.bit_array[digest]:
                return False
        else:
            return True

    
    def make_hash(self, s, seed):
        res_hash = 0
        for char in s:
            res_hash = (res_hash * (seed * 2 + 3) + ord(char)) % self.CAP
        return res_hash