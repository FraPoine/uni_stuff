### Testing, metrics, and confidence when your code is a model

he want to start whit an old picture

classifier is a detector for the positive class

performing an experiment 
- test set 

risk of overfitting 

**never judge your performance on training data**
the only thing that matter is the size of the dataset

we need test set 
- what if we need to test many variants of the model?
- and what if each time we test a different model the best parameters change?
the best result we get in our test set may not be the best result in the wild

what we get from testing is different from what we get 

the error estimate is optimistic 

if i test multiple parameters on the same test date i will pic the best parameter for that test data, it can change for different test data

looking at ur test data


#### Pre-genAI
follow 4 points of eval
dont reusing your test data

idea
- separate in training validation and test
- walk-forward validation
----
## part 2

sem standard error of the mean 
it depends of the number of the test dataset

dream condition, still we get samples that 

the constrain is the samples 

bias, variance and irreducibility
ur model can be bias, it can consistently predict higher or lower delay 
u can have variations, 

