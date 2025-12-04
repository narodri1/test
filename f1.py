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

def bigram(random_bi):
    """
    This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
    Except for bigram we have to account for the start and end charater.
    """
    count={}
    for i in range(len(random_bi)-1):  # loops through the list
        bi=random_bi[i]+" "+random_bi[i+1]  # considering two words at a time
        if not(bi.endswith("</s> <s>")):  # skips over the combination of end and start character
            if bi in count:  # counting
                count[bi]+=1
            else:
                count[bi]=1
    return count

def trigram(random_tri):
    """
    This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
    Except for Trigram we have to account for two start and end charater.
    """
    count={}
    for i in range(len(random_tri)-2):
        tri=random_tri[i]+" "+random_tri[i+1]+" "+random_tri[i+2]  # count three words at a time
        if (not(tri.endswith(" </s> <s>"))) and (not(tri.endswith("</s> <s> <s>")) ):  # skips over the combination of end character followed by the star charaters
            if tri in count:  # counting
                count[tri]+=1
            else:
                count[tri]=1
    return count