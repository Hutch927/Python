# Print five programming words and their definitions as neatly formatted outputs

programming_terms = {'IDE': 'A text editor with a number of other tools included, like an interactive debugger and code'
                            ' introspection.',
                     'Variable': 'A variable is a label that you can assign a value to.',
                     'String': 'A string is a series of characters. Anything inside quotes is considered a string.',
                     'List': 'A list is a collection of items in a particular order.',
                     'Slice': 'A slice is a specific group of items in a list.',
                     'Conditional Test': 'An expression that can be evaluated as TRUE or FALSE.',
                     'Tuple': 'A tuple is a list is immutable.',
                     'List Comprehensions': 'A List Comprehension allows you to generate a list in one line of code',
                     'Loop': 'A loop allows you to take the same action, or set of actions, with items in a list.',
                     'Constant': 'A constant is like a variable whose value stays the same throughout the life of a'
                                 'program.'}
for key, value in sorted(programming_terms.items()):
    print(f'{key}:\n\t{value}')