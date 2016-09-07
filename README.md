
#### Basic concepts
First, data in functional programs should be immutable, which sounds serious but just means that it should never change. At first, this might seem odd (after all, who needs a program that never changes anything?), but in practice, you would simply create new data structures instead of modifying ones that already exist. For example, if you need to manipulate some data in an array, then you’d make a new array with the updated values, rather than revise the original array. Easy!

Secondly, functional programs should be stateless, which basically means they should perform every task as if for the first time, with no knowledge of what may or may not have happened earlier in the program’s execution (you might say that a stateless program is ignorant of the past). Combined with immutability, this helps us think of each function as if it were operating in a vacuum, blissfully ignorant of anything else in the application besides other functions. In more concrete terms, this means that your functions will operate only on data passed in as arguments and will never rely on outside values to perform their calculations.

#### Rules
* All of your functions must accept at least one argument.
* All of your functions must return data or another function.
* No loops!

#### References
 - http://www.smashingmagazine.com/2014/07/dont-be-scared-of-functional-programming/
 - https://gist.github.com/giovaneliberato/c1c6b3f733a05f3b5953
