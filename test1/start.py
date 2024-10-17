import pkgutil
search_path = ['.']  # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print("Available modules to import: ")
print(all_modules)
