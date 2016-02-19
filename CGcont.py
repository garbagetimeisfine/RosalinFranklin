def CGcontent(DNA):
    """ Return proportion of CG in sequence.
    Assumes that the DNA is uppercase containing
    ONLY A T G C
    =================================
    Unit testing with docstrings
    =================================
    Run the command in python3, (e.g., python3 -i
    CGcont.py) and copy the output below:
        
        >>> CGcontent("AAAAAA")
        0.0
        >>> CGcontent("AAATTT")
        0.0
        >>> CGcontent("AAATTTCCCC")
        0.4
        >>> CGcontent("AAATTTCCC") 
        0.3333333333333333
        """

    CG = DNA.count("C") + DNA.count("G")
    CG = CG / float(len(DNA))
    return CG

if __name__ == "__main__":
    import doctest
    doctest.testmod()