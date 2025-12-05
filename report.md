## Correctness
### do LLMs write code with fewer errors than you? Why or why not?
```
Answer:
LLM's don't necessarily write code with fewer number of errors in the count of errors. Both the LLM and our code is not without errors it jus differs in where we made them. In our code we didn't include the proper amount of BOS and EOS tokens but it was only in one model whereas the LLM purposely had only 1 BOS and EOS token for each of the model and cause of that its word pairs are also be wrong. this could likely be because of the data that it was trained on or it could be because of the propmt the user gave the LLM.
```


## Style
### is the style of LLM coding better than yours? Why or why not?
```
Answer:
The code style might definitely be better than ours cause it definitely seems more easier but its not simpler than ours. Ours is more direct while also giving the user some understanding as to where the program might be although the LLM code doesnt offer anything like that. but it does definitely give simpler and more easier solutions for developers to use, an example of this would be the Counter function it used. This is dues to the way that an LLM is trained as mentioned in the earlier answers the LLM are trained on huge amounts of code data and most of those are obtained from high level repositries and code bases. 
```
## Similarity
### if a random person looks at your code, would they be able to tell it was not written by an LLM?

```
Answer:
Yes, if an average person who never touched coding in thier life were to read our code, they would be able to tell it was not written by an LLM. This would mainly be due to how we structured the code and how we write comments and how we handel some of the calculation in what might be a dumber but more easier to read way. 
If a random person who has knowledge of how to code were to read our code they would definitely be able to tell it was not written by an LLM.
Again an LLM is able to write that high and beautiful pieces of code cause it was trained on those high level coding styles and  
```
### Should computing assignments like assignment 3 be given for marks? Base your answer on how easy it is to obtain answers from an LLM and assume that students will use LLMs to help them code in the future.
```
Answer:
Yes I think that computing assignments like 3 should be given for marks cause as seen in training.md and evaluation.md although LLM writes good code it can still be wrong and if a student were to blindly take it they would:
1. Not be able to understand it properly cause they didnt write so if they were asked to explain something they wouldnt be able. (maby force all the students to randomly explain thier code and if they can't dock thier marks)
2. lose lot of marks if they can't identify the mistakes the LLM has.
So yes assignmenst like 3 should be given for marks but the grading and evalution process should focus rather on the student or group understanding of the code and the process rather than just on the final code. 
grading should take into considertion students reasoning (just like how we have the justification process in the previous assignmets)
```