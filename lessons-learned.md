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

Fortunately, the results don't change when a virtual environment is activated and the steps above are repeated.