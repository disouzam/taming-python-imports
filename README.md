# About
As projects grow, I get stuck in import errors in Python, limiting my way to organize files in semantic folders and wasting precious time. It could be as easy as in C#

This repository appeared as a response to an issue that happens to me all the time: working with single files in Python is awesome and straightforward but as I have a need to organize files in a different way, adding folders by themes or technical reasons, I start getting lots of errors, either in IntelliSense provided by Pylint or during execution. So far I either managed to solve it somehow or surrendered and give up on my initial organizational needs.

Then, I started looking back at this topic again as I was breaking large pieces of code from a Streamlit app (closed source project) in several pages and different files. Then, the pain emerged again!

I found these two reference articles that I started exploring today (October 16th, 2024) and decided that the practice is what makes my muscle memory to work better and could help me to solve this problem for current projects and future ones, adopting the Pythonic way of dealing with imports, files, packages and so on.

The cited articles are:
- [The Definitive Guide to Python import Statements](https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#using-objects-from-the-imported-module-or-package)
- [Python import: Advanced Techniques and Tips](https://realpython.com/python-import/)

Other references might be added here later as I try to reproduce in toy examples the ideas from these references and Python documentation