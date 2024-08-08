import os
import shutil
from fractions import Fraction
from audiosynth import combineaudio, exportaduif

count = None

def subset_sum(numbers, target, index, index_print = [], files_print = [], partial=[]):
    global total
    global count
    if count is None:
        count = {num: 0 for num in set(numbers)} 
    
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target: 
        total = total + 1
        print ("%s : %s : %s" % (target, total, index_print))
        # print ("%s : (%s)" % (target, files_print))
        a = combineaudio(index_print)
        print("exporting : ", str(total))
        exportaduif(a + a + a + a, str(target), str(total))
    if s >= target:
        return  # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i:]

        n_i = index[i]
        remaining_index = index[i:]

        f_i = "./Mixdown/" + index[i] + "Open.wav"

        # Update count for the current element
        if count[n] < 3:
            count[n] += 1
            subset_sum(remaining, target, remaining_index, index_print + [n_i], files_print + [f_i], partial + [n])
            # Backtrack: remove the element count after recursive call
            count[n] -= 1

if __name__ == "__main__":
    # 1 : Triplet-16th
    # 2 : 16th
    # 3 : Triplet-8th
    # 4 : Dotted-16th
    # 5 : 8th
    # 6 : Triplet-Quarter
    # 7 : Dotted-8th
    # 8 : Quarter
    # 9 : Dotted-Quarter
    #subset_sum([0.167, 0.25, 0.334, 0.375, 0.5, 0.667, 0.75, 1, 1.5],2)
    numbers = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 3), Fraction(3, 8), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(3, 2)]
    names = ["Triplet-16th", "16th", "Triplet-8th", "Dotted-16th", "8th", "Triplet-Quarter", "Dotted-8th", "Quarter", "Dotted-Quarter"]
    index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    target = [4]

    shutil.rmtree("./RESULTS/")
    os.makedirs("./RESULTS/", exist_ok=True)

    shutil.rmtree("./COMBI/")
    os.makedirs("./COMBI/", exist_ok=True)
    
    for f in range(0, len(target)):
        os.makedirs("./RESULTS/" + str(target[f]), exist_ok=True)
    
    total_sum = 0
    for j in range(len(target)):
        total = 0
        subset_sum(numbers, target[j], index)
        print("Riffs for 2 : " + str(total))
        total_sum += total

print("Total Riffs : " + str(total_sum))