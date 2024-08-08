"""
Generates a permutation of list values
"""
import shutil
import os
import itertools
from audiosynth import combineaudio, exportaudiocombi


TOTALPERM = 0
ITERATION = 413
elements = ['1', '1', '6', '8', '9', '9']


if __name__ == "__main__":
    try:
        shutil.rmtree("./COMBI/")
    except:
        os.makedirs("./COMBI/" + str(ITERATION), exist_ok=True)

    permutations = itertools.permutations(elements)
    for perm in permutations:
        TOTALPERM += 1
        a = combineaudio(perm)
        exportaudiocombi(a + a + a + a, str(ITERATION), str(TOTALPERM))
        print(perm)
    print(TOTALPERM)
