# The GRIM test 
_An implementation of the GRIM test, in python_

## Introduction
This package is based on the GRIM (Granularity-Related Inconsistency of Means) test first highlighted by Heathers & Brown in their 2016 paper.

The test makes use of a simple numerical property to identify if the mean of integer values has been correctly calculated.

You don't need the original integer values. You just need the _mean_ and the number (_n_) of items.

## What about rounding?

Often the _mean_ you are testing has previously been rounded. You can check if the _mean_ is consistent with a particular rounding type by including that as an argument.

This implementation supports all the rounding types currently found in Python 3.8's `decimal` [implementation](https://docs.python.org/3/library/decimal.html).

(They are: ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP, ROUND_UP, ROUND_05UP)

If no rounding type is included then the test assumes ROUND_HALF_UP.


### How do I install it?

On the command line:
```bash
pip install grim
```

In a google Colab/iPython notebook:
```bash
!pip install grim
```

### Example: Is this _mean_, _n_ and rounding type consistent?
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.consistency_check('11.09', '21', decimal.ROUND_HALF_UP))
```
This will return `False` as the mean could not be correct given a list of 21 integers (and using ROUND_HALF_UP rounding.)

### Example: Is this _mean_ & _n_ consistent using any rounding type?
```python
from grim import mean_tester
import decimal

# mean is 11.09 and n is 21
print(mean_tester.summary_consistency_check('11.09', '21'))
```
This will return:
```python
{'ROUND_CEILING': False, 'ROUND_DOWN': True, 'ROUND_FLOOR': True, 'ROUND_HALF_DOWN': False, 'ROUND_HALF_EVEN': False, 'ROUND_HALF_UP': False, 'ROUND_UP': False, 'ROUND_05UP': True}
```
As you can see, a given mean and n might be consistent using one form of rounding but not others.

You can pass in the numbers as Strings or Decimals, this avoids floating point accuracy issues that are more likely to occur when using a 'float'.

# How do I see some logging about how the possible matches the algorithm has considered?

Add an extra argument,  `True`.
```python
print(mean_tester.summary_consistency_check('11.09', '21', True))
```

## A warning about floating point numbers & computers:

1. Beware of creating Decimals from floating point numbers as these may have floating point inaccuracies.
e.g.:
```python
import decimal

print(decimal.Decimal(1.1))
1.100000000000000088817841970012523233890533447265625
```
Notice how the inaccurate representation of 1.1 from the floating point number has been preserved in the Decimal. Its better to create a decimal from a String E.g.:
```python
import decimal

print(decimal.Decimal('1.1'))
1.1
```
Many tools can be configured to read in text [that might be a number] as a string with out parsing. Some tools, such as Webdriver, only return a string (Which is useful!)

For more information on the origins of these issues in modern computer languages [read this](http://effbot.org/pyfaq/why-am-i-getting-strange-results-with-simple-arithmetic-operations.htm).

## How can I find out more about the GRIM test?
James Heathers has published [articles](https://medium.com/@jamesheathers/the-grim-test-a-method-for-evaluating-published-research-9a4e5f05e870) that explain how the technique works and how he used it to expose inconsistencies in scientific papers.

## Citation file

There is a [citation file](https://github.com/phoughton/grim_test/blob/master/CITATION.cff) included in the code repo.
