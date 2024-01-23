import numpy as np

class Person():
    """person object for Family Tree 
    -----------
    Attributes:
    ----------
    name : str
        The name of the person.
    birth_year : int
        The year the person was born.
    parent: Person
        parent of the person
    death_year : int
        The year the person died. None if the person is still alive.
    hashed_name : str
        Just saving the name in hashed form for security.
    children : List of 'Person' Object
        The person's children. None if no child. 
    """
    kind = 'person'
    all_persons = {}
    def __init__(self,name,birth_day,parent,death_day = None):
        self.name = name
        self.birth_day = birth_day
        self.death_day = death_day
        self.hashed_name = Person.Hash(name,birth_day)
        self.parent = parent
        if parent is not None:
            self.level = parent.level + 1
        else:
            self.level = 1
        self.children = []
        Person.all_persons[self.hashed_name] = self        
    def AddChild(self,child):
        """add a person to this person's children.
        input: 
            child : Person 
        return:
            None
        """
        self.children.append(child)
    
    def __del__(self):
        del Person.all_persons[self.hashed_name]
    
    @staticmethod      
    def Hash(name,birth_day):
        # Define the initial hash values
        h0 = 0x6a09e667
        h1 = 0xbb67ae85
        h2 = 0x3c6ef372
        h3 = 0xa54ff53a
        h4 = 0x510e527f
        h5 = 0x9b05688c
        h6 = 0x1f83d9ab
        h7 = 0x5be0cd19

        # Define the round constants
        k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

        # Define the logical functions
        def rotr(x, n):
            return (x >> n) | (x << (32 - n))

        def ch(x, y, z):
            return (x & y) ^ (~x & z)

        def maj(x, y, z):
            return (x & y) ^ (x & z) ^ (y & z)

        def sigma0(x):
            return rotr(x, 2) ^ rotr(x, 13) ^ rotr(x, 22)

        def sigma1(x):
            return rotr(x, 6) ^ rotr(x, 11) ^ rotr(x, 25)

        def gamma0(x):
            return rotr(x, 7) ^ rotr(x, 18) ^ (x >> 3)

        def gamma1(x):
            return rotr(x, 17) ^ rotr(x, 19) ^ (x >> 10)

        # Define the padding function
        def pad(msg):
            # Convert the message to binary
            msg_bin = ''.join(format(ord(c), '08b') for c in msg)
            # Append a 1 bit
            msg_bin += '1'
            # Append zeros until the length is a multiple of 448
            msg_bin += '0' * ((448 - len(msg_bin)) % 512)
            # Append the length of the original message in 64 bits
            msg_bin += format(len(msg) * 8, '064b')
            return msg_bin

        # Pad the input name
        msg = pad(name+' '+str(birth_day))

        # Divide the message into 512-bit chunks
        chunks = [msg[i:i + 512] for i in range(0, len(msg), 512)]

        # Process each chunk
        for chunk in chunks:
            # Create a 64-element array of 32-bit words
            w = [0] * 64
            for i in range(16):
                w[i] = int(chunk[i * 32:(i + 1) * 32], 2)
            for i in range(16, 64):
                w[i] = (gamma1(w[i - 2]) + w[i - 7] + gamma0(w[i - 15]) + w[i - 16]) % 2**32

            # Initialize the eight variables
            a = h0
            b = h1
            c = h2
            d = h3
            e = h4
            f = h5
            g = h6
            h = h7

            # Perform 64 rounds of compression
            for i in range(64):
                t1 = (h + sigma1(e) + ch(e, f, g) + k[i] + w[i]) % 2**32
                t2 = (sigma0(a) + maj(a, b, c)) % 2**32
                h = g
                g = f
                f = e
                e = (d + t1) % 2**32
                d = c
                c = b
                b = a
                a = (t1 + t2) % 2**32

            # Add the updated variables to the current hash values
            h0 = (h0 + a) % 2**32
            h1 = (h1 + b) % 2**32
            h2 = (h2 + c) % 2**32
            h3 = (h3 + d) % 2**32
            h4 = (h4 + e) % 2**32
            h5 = (h5 + f) % 2**32
            h6 = (h6 + g) % 2**32
            h7 = (h7 + h) % 2**32

        # Concatenate the final hash values to get the digest
        hash_name = format(h0, '08x') + format(h1, '08x') + format(h2, '08x') + format(h3, '08x') + \
            format(h4, '08x') + format(h5, '08x') + format(h6, '08x') + format(h7, '08x')

        return hash_name
