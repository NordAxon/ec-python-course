# Code review list


## Step 1.
Read the README and create an environment. Install the dependencies.

- [ ] Is the README understandable?
- [ ] Is there a requirements.txt file?
- [ ] Are the version numbers specified in the requirements file?
- [ ] Is the python version specified?


## Step 2.
Try to start the program according to the instructions in the README, to see if the program is understandable and gives helpful output

- [ ] Can you start the program without looking in the code to understand it?
- [ ] If you test different inputs, does the program still work?
- [ ] Does the program give valuable feedback if you enter faulty values?
- [ ] Do you understand what it does (on a high level)

## Step 3.
Now, let's open the code and look inside! Does the code look like it should?

### 3.1 A quick overview
- [ ] Looking through the file / files quickly, do you get an overview of how the program is built?
- [ ] Is the functionality adequately split up into functions with explainable names?

### 3.2 Python conventions
- [ ] Does the code follow PEP-8?
	- [ ] Is there a main method?
	- [ ] How are the names of the functions, classes, methods and variables?
- [ ] Are there any docstrings present?
- [ ] Is the code self-explanatory? Is it documented well where it is not?
- [ ] What is the pylinter score?


### 3.3 Error handling
- [ ] Is every caught error specified?
- [ ] Is every possible error caught and handled? (That you can find)


### 3.4 Possible logical bugs
- [ ] Can you find any possible logical bugs?



