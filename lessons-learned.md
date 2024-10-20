# About

A short recording of the lessons learned through experimentation

# Code Snippet 1

```python
import pkgutil
search_path = ['.']  # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print(all_modules)
```

# Effect on `start.py` only

After inserting Code Snippet 1 on `start.py`, and running it without any virtual environment activated, from the root folder, the output is as follows:

```bash
python test1/start.py
```

```bash
[]
```

When directory is changed to `test1`, a significant change happens as follows:

```bash
cd test1
python start.py
```

```bash
['math', 'other', 'packA', 'random', 'start']
```

Fortunately, the results don't change when a virtual environment is activated and the steps above are repeated. It is worth noting that packB was not imported due to the fact that there is no `__init__.py` inside this folder.

After adding this file to packB folder the result of the following command was updated to:

```bash
echo > test1/packB/__init__.py
cd test1
python start.py
```

```bash
['math', 'other', 'packA', 'packB', 'random', 'start']
```

## Takeaway #1
So, the takeaway #1 is that __init__.py, even when empty of content, helps somehow with the import resolution

## Continuation of tests
Tests were repeated calling `start.py` as a module rather than a script ([Running Modules With the -m Option](https://realpython.com/run-python-scripts/#running-modules-with-the-m-option)) and the results were similar to what presented above.

For completeness, the commands are reproduced below:

From root folder:
```bash
python -m test1.start
```

```bash
[]
```

Setting current working directory (cwd) to `test1`:
```bash
cd test1
python -m start
```

```bash
['math', 'other', 'packA', 'random', 'start']
```

## Takeaway #2

The second takeaway is that the option -m doesn't change the behavior of imports at current setup of experiments.

## Takeawy #3

 The third takeaway, and the more serious so far, is that while it is possible to call a script or module from wherever you are in the command-line (your cwd), if you call it outside of the directory where it is saved, no import relative to that file will be imported or available to be used (in current case, modules math, other, packA, random will not be available to be imported).


# Code Snippet 2

The second code snippet is helpful to inspect the content of sys.path variables.

```python
import sys

print("Paths in sys.path:")
npaths=0
for pathitem in sys.path:
    npaths+=1
    print(f"{npaths}: Path: {pathitem}")
```

When running start.py from root folder (```python test1/start.py```) and from `test1` folder (```python start.py```), the only difference is the modules imported. The paths are the same so far.


```text
1: Path: {root-folder}\test1
2: Path: {Python installation directory}\python.zip
3: Path: {Python installation directory}\DLLs
4: Path: {Python installation directory}\Lib
5: Path: {Python installation directory}
6: Path: {root-folder}\.venv
7: Path: {root-folder}\.venv\Lib\site-packages
```

## Takeaway #4

Looking at the combination of modules made available and paths added to sys.path between the call to `start.py` made from root folder and the call made from `test1`, it is noted that paths are the same in both cases while modules are only available when the call is made from inside `test1`.