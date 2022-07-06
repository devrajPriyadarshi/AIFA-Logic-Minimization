# Obtaining Reduced Expression of Boolean Functions

Course Assignment for Artificial Intelligence: Foundation and Application.

Made by Piyush Kumar, Devraj Priyadarshi and Azim Sohel.

---

Obtaining Reduced form of SOP(Sum of Product) / POS(Product of Sum) form of a function from its given truth table i.e. writing boolean expressions in minimized form.
We take minterms/maxterms/Karnaugh maps as inputs, use searching methods to reach to the output with optimized boolean expression.

### AI Mapping & Approach
#### State Space Searching. 
The action may be taken out by forming minterm/maxterms using a Karnaugh map as an input and the result is the number of terms in the output . A goal state can be where the number of terms is coming minimum. There may be many goal states to one problem, we’ll consider one of them as our final output.

```
State Space : Every variable considered in the expression and their combinations.

State : [ combination of variables in SOP or POS form ]

Goal State : the state where the expression gives the same result as our input function for all values of variables.
Heuristics & Cost : based on addition of each combination, with bigger expressions having bigger cost.
```