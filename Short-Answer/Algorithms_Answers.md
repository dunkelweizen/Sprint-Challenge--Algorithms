#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This would have a time complexity of O(n) because the time complexity 
of a while loop depends on the number of iterations of the loop control variable,
which in this case is a. The loop would repeat n^3 times except that the equation
inside the loop increases a by n^2 each time. This is n^3 / n^2, which becomes
n^(3-2), or just n.

b) This block of code is complexity O(n*logn) because it is a nested loop. The outer
loop has a time complexity of O(n) because it repeats an O(1) process n times. For
each of those n times, it runs a second loop log(n) times; j is the loop control 
variable and j is incremented to the square of itself each time. Since it's a nested
loop, the two loops are multiplied together to get the final complexity - O(n) *
 O(logn) = O(n*logn).


c) This has an O(n) runtime. Since the base case is if bunnies == 0, the loop control
variable is the number of bunnies (n). Each time the recursion runs, this number 
decrements by one. The addition of the constant each loop has no effect on runtime.

## Exercise II
for a building of n floors:
    travel to middle floor
    drop egg
    if egg breaks:
        travel to floor halfway between current and 0th floor
    if egg does not break:
        travel to floor halfway between current and nth floor
    repeat this loop until x and x+1 are found, such that on floor x the egg breaks
        and on floor x+1 it does not break. 
        f == floor x + 1
        
        
This solution should have a runtime complexity of O(logn) since each time the 
loop is run, half of the remaining n values can be discarded (move up or down the
building to half of what's left).
    

