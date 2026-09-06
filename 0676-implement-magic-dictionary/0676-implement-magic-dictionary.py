import numpy as np

class MagicDictionary:

    def __init__(self):
        # The 'Vector Field' - grouped by word length L
        # Stores words as NumPy arrays of uint8 (0-255 ASCII)
        self.field = {}        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            L = len(word)
            if L not in self.field:
                self.field[L] = []
            # Convert string to numerical vector
            self.field[L].append(np.frombuffer(word.encode(), dtype=np.uint8))
        
        # Stack lists into matrices for vectorized operations
        for L in self.field:
            self.field[L] = np.stack(self.field[L])        

    def search(self, searchWord: str) -> bool:
        L = len(searchWord)
        if L not in self.field:
            return False
            
        # 1. Convert searchWord to a numerical vector
        query_vector = np.frombuffer(searchWord.encode(), dtype=np.uint8)
        
        # 2. Vectorized Matrix Subtraction
        # We subtract the query vector from every row in the dictionary matrix simultaneously.
        # dictionary_matrix (N x L) - query_vector (1 x L)
        diff_matrix = self.field[L] != query_vector
        
        # 3. Hamming Weight Calculation
        # Count non-zero entries across each row (the number of mismatches)
        mismatch_counts = np.sum(diff_matrix, axis=1)
        
        # 4. Search for a 'Unit Impulse' (exactly one mismatch)
        return bool(np.any(mismatch_counts == 1))        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)