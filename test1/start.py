import sys
import pkgutil

search_path = ['.']  # set to None to see all modules importable from sys.path
all_modules = [x[1] for x in pkgutil.iter_modules(path=search_path)]
print("Available modules to import: ")
nmodules = 0
for module in all_modules:
    nmodules += 1
    print(f"{nmodules}: Module name: {module}")


print("Paths in sys.path:")
npaths = 0
for pathitem in sys.path:
    npaths += 1
    print(f"{npaths}: Path: {pathitem}")
