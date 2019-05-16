# README
## Usage
This program take a csv file like `sample.csv` as a input.
That is like:

|id|...|step|
|--|--|--|
|id1|...|100|
|id2|...|250|
|id3|...|550|
|id4|...|1050|

Write a file name `sample.csv` in the following manner in `shape_step_for_point.py`

```python
  df = pd.read_csv('sample.csv', encoding='SHIFT-JIS')
```

Then run in your bash
```bash
 python shape_step_for_point.py
```

Consequently, this program's output is:
- a excel file composed of two sheet:
    - 1st sheet: monthly step data
    - 2nd sheet: left justified step data
