"""
Generates a permutation of list values
"""
import shutil
import os
import itertools
from audiosynth import combineaudio, exportaudiocombi


TOTALPERM = 0
ITERATION = 290
elements = ['4', '4', '5', '5', '7', '9']


if __name__ == "__main__":
    try:
        shutil.rmtree("./COMBI/")
    except:
        os.makedirs("./COMBI/" + str(ITERATION), exist_ok=True)

    permutations = itertools.permutations(elements)
    for perm in permutations:
        TOTALPERM += 1
        a = combineaudio(perm)
        exportaudiocombi(a + a + a + a, "290", str(TOTALPERM))
        print(perm)
    print(TOTALPERM)
