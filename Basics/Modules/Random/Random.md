`import random`

## random.randint()
- generates a random integer between a and b (inclusive)
    - `random.randint(1, 10)`
      - will return random a number 1 - 10
## Semi Open Range
- an interval that includes its starting point but excludes its ending point
- fundamental to how Python handles sequences, particularly with the range() function and slicing operations
- `random.random()` is a semi open range

# Generate a random floating point number: random.random() and random.uniform()
- random.random() and random.uniform() both generate a random floating point number
- Difference between the two
  - random.random(): you will never get the end-point value
  - random.uniform(): you may get the upper bound(b) or you may not, depending on floating-point rounding
  - 
## random.random() 
- generates a random floating point number from 0 inclusive and up to 1 not inclusive
  - `0.0 <= random.random() < 1.0`
    - always includes 0 but will never include 1
- `random.random()` 
  - from 0.0(inclusive) to 1.0(exclusive)
- `random.random() * 30`
  - from 0(inclusive) to 30.0(exclusive)
  - you will never get 30

## random.uniform()
- generates a floating point number between a and b inclusive of a and b
  - `a<= random.uniform(a,b) <=b`
  - the number is <=(GT) lower bound and >=(LT) upper bound
- `random.uniform(1, 10)`
  - you may get 10.0, or you may not, depending on floating-point rounding

## random.choice()
- used to select a random element from a non-empty sequence
- selects an element with equal probability from the given sequence, meaning each element in the sequence has an equal probability of being chosen
- returns an element of the same type as the elements in the input sequence
- if sequence is empty, `random.choice()` will raise an IndexError
- List(Sequence): `my_list = ["green", "yellow", "red", "purple", "blue" ]`
  - `random.choice(my_list)`
- String(Sequence): `my_string = "Shannon"`
  - `random.choice(my_string)`