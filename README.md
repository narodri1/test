## Most similar functionality

### Your code

```Python
Answer:
counting n-grams functionality 
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
```

### LLM code

```Python
Answer:
def count_ngrams(
    utterances: List[List[str]]
) -> Tuple[
    Counter[str],
    Counter[Tuple[str, str]],
    Counter[Tuple[str, str, str]]
]:
    uni: Counter[str] = Counter()
    bi: Counter[Tuple[str, str]] = Counter()
    tri: Counter[Tuple[str, str, str]] = Counter()

    for utt in utterances:
        seq = [START] + utt + [END]

        uni.update(seq)

        for i in range(len(seq) - 1):
            bi[(seq[i], seq[i + 1])] += 1

        for i in range(len(seq) - 2):
            tri[(seq[i], seq[i + 1], seq[i + 2])] += 1

    return uni, bi, tri
```

### Output of `diff`

```
Answer:
def unigram(random):
<     """
<     This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
<     """
<     count={}
<     for uni in random:
<         if uni in count:  # if more than one
<             count[uni]+=1
<         else:
<             count[uni]=1  # just one occurance
<     return count
---
> def count_ngrams(
>     utterances: List[List[str]]
> ) -> Tuple[
>     Counter[str],
>     Counter[Tuple[str, str]],
>     Counter[Tuple[str, str, str]]
> ]:
>     uni: Counter[str] = Counter()
>     bi: Counter[Tuple[str, str]] = Counter()
>     tri: Counter[Tuple[str, str, str]] = Counter()
13,26c12,13
< def bigram(random_bi):
<     """
<     This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
<     Except for bigram we have to account for the start and end charater.
<     """
<     count={}
<     for i in range(len(random_bi)-1):  # loops through the list
<         bi=random_bi[i]+" "+random_bi[i+1]  # considering two words at a time
<         if not(bi.endswith("</s> <s>")):  # skips over the combination of end and start character
<             if bi in count:  # counting
<                 count[bi]+=1
<             else:
<                 count[bi]=1
<     return count
---
>     for utt in utterances:
>         seq = [START] + utt + [END]
28,41c15,23
< def trigram(random_tri):
<     """
<     This functions takes the list of tokens and counts how many there are of each word and returning it as a dictionary.
<     Except for Trigram we have to account for two start and end charater.
<     """
<     count={}
<     for i in range(len(random_tri)-2):
<         tri=random_tri[i]+" "+random_tri[i+1]+" "+random_tri[i+2]  # count three words at a time
<         if (not(tri.endswith(" </s> <s>"))) and (not(tri.endswith("</s> <s> <s>")) ):  # skips over the combination of end character followed by the star charaters
<             if tri in count:  # counting
<                 count[tri]+=1
<             else:
<                 count[tri]=1
<     return count
---
>         uni.update(seq)
> 
>         for i in range(len(seq) - 1):
>             bi[(seq[i], seq[i + 1])] += 1
> 
>         for i in range(len(seq) - 2):
>             tri[(seq[i], seq[i + 1], seq[i + 2])] += 1
> 
>     return uni, bi, tri
\ No newline at end of file
```

## Discussion

### What is most similar?

```
Answer here.
The logic? The order of steps? The style? Variable names? What could explain the similarity?
there is virtually nothing similar maby only the logic is similar but thats cause the logic is pretty consistent and there is only few ways that i can think of doing it. But also we dont use any kind of Counter python function we just manually count it. the order of steps is also similar but thats cause that is the main order of steps and we can't really change the order of steps.
```

### What is most different?

```
Answer here.
The logic? The order of steps? The style? Variable names?
the logic and the order of steps is pretty similar but the style is pretty different as ours is very short and easier to understand and we use simple and direct methods to calculate the counts where as the LLM uses more precise code that is the Counter function. and since the style is different hence most of the variable names are different our variable is not the best variable names and can be a bit confusing while the LLMs variable name is much more descriptive.  
```
