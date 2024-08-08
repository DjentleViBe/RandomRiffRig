from audiosynth import combineaudio, exportaduif, exportaudiocombi
import itertools
import shutil
import os

total_perm = 0
iteration = 290
elements = ['4', '4', '5', '5', '6', '8']

shutil.rmtree("./COMBI/")
os.makedirs("./COMBI/" + str(iteration), exist_ok=True)

permutations = itertools.permutations(elements)
for perm in permutations:
    total_perm += 1
    a = combineaudio(perm)
    exportaudiocombi(a + a + a + a, "290", str(total_perm))
    print(perm)
print(total_perm)


