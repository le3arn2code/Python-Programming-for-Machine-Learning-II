# Interview Q&A (10)

1) What are Python's core data types used here?  
Integers, floats, strings, lists, tuples, dicts.

2) Difference between list and tuple?  
List is mutable; tuple is immutable.

3) When to use a virtual environment?  
When isolating dependencies per project to avoid system conflicts (PEP 668 safe).

4) How to install packages safely on Ubuntu?  
Use venv + `pip install`, or user scope with `--user`, or apt packages.

5) What is `if __name__ == "__main__":` used for?  
Entry‑point guard so code runs only when executed as a script, not on import.

6) What’s the benefit of f‑strings?  
Concise, readable string interpolation with expressions.

7) How does a `while` loop differ from a `for` loop?  
`while` repeats until a condition becomes false; `for` iterates over an iterable.

8) What is a dictionary good for?  
Key‑value mappings for fast lookups and structured data.

9) How to check versions of installed libs in Python quickly?  
`import pkg; print(pkg.__version__)` for each (NumPy, Pandas, Matplotlib).

10) Why avoid `sudo pip`?  
It can break system Python; prefer venv or `--user` installs.
