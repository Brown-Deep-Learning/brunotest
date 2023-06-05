# brunotest
A coursework templating and testing engine to consolidate assignment code and ensure robust assignment quality.

The idea behind this framework is that it woul allow us to write only _one_ solution code, and then carefully work out stencil around it (in fact, have the stencil _generated automatically_ from the solution code).

The idea on how to do this is to use __Region__ tags in the code, and 

All of the templating will be done in a `__brunotest__` hidden folder (that could be gitignored). The general use case is as follows (we'll say with the `fibonacci` example given in `examples`):

1. Define our stencil/chaff/solution code
2. Run `brunotest` to run the solution code against the `tests`
3. Run `brunotest stencil` to run the compiled stencil code against the `tests` 
4. Run `brunotest [chaff name]` to run the compiled chaff code against the `tests`.
5. Run `brunotest all` to run all of the code (solution, stencil, chaffs) against the `tests`.

Ideally, this would also be enhanced by a VSCode extension that could allow you to more easily see the different chaffs/stencil alongside the current document you are editing (maybe similar to how Markdown preview works). 

Some other considerations/definitions for now:

1. The chaff implementations will be stored in `.chaff` files, and:
    1. Do not require all of the regions defined in the solution to be overwritten, but regions that are not specified will remain the same.
    2. Can (somehow?) define which tests should fail and with what values, likely at the top?
        1. This may be somewhat challenging because we have to incorporate failing partial tests, test names, etc. 
2. The stencil code will be in a _single_ `.stencil` file in the root directory (error on multiple found). 
    1. The stencil also does not have to specify every distinct region to overwrite, but those which are not specified will be __left blank__. 

## Gradescope Autograder Specifications

The gradescope autograder, with the configuration that we use it in, has the following directory structure:

```
/autograder/ # Base Directory
/autograder/student # Student submission
/autograder/solution # Solution code 
```