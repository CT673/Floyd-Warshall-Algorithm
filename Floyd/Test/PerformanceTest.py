# Timeit Test
import timeit
from Floyd import paths

print("Recursion timeit timing for recursive version: "
      + str(timeit.timeit(setup="from Floyd import paths",
                          stmt="paths()",
                          number=10000)))

print("Timing for iterative version"
      + str(timeit.timeit(setup="from Floyd import floydmain",
                          stmt="floydmain()",
                          number=10000)))
print("\n")
print("\n")
print("cProfile testing results for recursive version")
# cProfile Test
import cProfile
import Floyd

cProfile.run("Floyd.paths")

print("\n")
print("cProfile testing results for iterative version")
import cProfile
from Floyd import floydmain
cProfile.run("floydmain")
