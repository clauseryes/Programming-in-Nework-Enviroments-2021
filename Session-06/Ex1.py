import P0.Seq0

class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence():
        #if Seq.is_valid_sequence_2(strbases):
            print("New sequence created!")
        else:
            self.strbases = 'Error'
            print('Incorrect sequence!')

    @staticmethod
    def is_valid_sequence_2(bases):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def is_valid_sequence(self):
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'G' and c != 'T':
                return False
        return True

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("ERHJAOR")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")