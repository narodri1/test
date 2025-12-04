print("nathan was here")
def unigram(random):
    """
    This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
    """
    count={}
    for uni in random:
        if uni in count:  # if more than one
            count[uni]+=1
        else:
            count[uni]=1  # just one occurance
    return count
