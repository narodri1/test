import json
import sys

def text(path):
    """
    This function takes the path for the training.txt file and intializes all the BOS and EOS characters for the three models.
    Returns: Three seperate lists for Unigram, Bigram and Trigram respectively. 
    """
    random=[]
    random_bi=[]
    random_tri= []
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        lines=file.readlines()
        for i in lines:
            if not i.isspace():   # skips over the empty lines
                uni=i.strip().split()
                for n in uni:  
                    random.append(n)  # each occurance of the token is added to the list
                bi=i.strip()
                bi= "<s> "+bi+" </s>"  # for the bigram it adds one beginning and end charcter
                bi=bi.split()
                for n in bi:
                    random_bi.append(n)
                tri=i.strip()
                tri= "<s> <s> "+tri+" </s>"  # for the trigram add two beginning and one end
                tri=tri.split()
                for n in tri:
                    random_tri.append(n)

    return random, random_bi, random_tri

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

def main():
    # taking two user arguments and passes it to the text function
    command_input = sys.argv[1]
    command_output = sys.argv[2]
    random, random_bi, random_tri = text(command_input)

    uni = unigram(random)
    bi = bigram(random_bi)
    tri = trigram(random_tri)

    print("Writing to json file.")
    # for the json file
    data = {
        "unigram": uni,
        "bigram": bi,
        "trigram": tri
    }

    # output it as a json file 
    with open(command_output, "w", encoding="utf-8") as file:
        json.dump(data, file ,ensure_ascii=False, indent=2)
    
    print("Done :)")

if __name__ == "__main__":
    main()