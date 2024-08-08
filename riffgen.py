"""
Generates subset sum
"""
import os
import shutil
from fractions import Fraction
from audiosynth import combineaudio, exportaduif

COUNT = None

def subset_sum(numbers, target, index, index_print = [], partial = []):
    """Subset sum function
    """
    global TOTAL
    global TOTAL_NOTES_COUNT
    global COUNT
    if COUNT is None:
        COUNT = {num: 0 for num in set(numbers)}

    s_sum = sum(partial)

    # check if the partial sum is equals to target
    if s_sum == target:
        TOTAL = TOTAL + 1
        if(len(index_print) == total_notes):
            TOTAL_NOTES_COUNT = TOTAL_NOTES_COUNT + 1
            print(f"{target} : {TOTAL} : {index_print}")
            # print ("%s : (%s)" % (target, files_print))
            aname = combineaudio(index_print)
            # print("exporting : ", str(TOTAL))
            exportaduif(aname + aname + aname + aname, str(target), str(TOTAL))
    if s_sum >= target:
        return  # if we reach the number why bother to continue

    for i, _ in enumerate(numbers):
        n_num = numbers[i]
        remaining = numbers[i:]

        n_i = index[i]
        remaining_index = index[i:]

        # f_i = "./Mixdown/" + index[i] + "Open.wav"

        # Update COUNT for the current element
        if COUNT[n_num] < 3:
            COUNT[n_num] += 1
            subset_sum(remaining, target, remaining_index, index_print + [n_i],
                    partial + [n_num])
            # Backtrack: remove the element COUNT after recursive call
            COUNT[n_num] -= 1

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
    numbers = [Fraction(1, 6), Fraction(1, 4), Fraction(1, 3), Fraction(3, 8),
               Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(3, 2)]
    names = ["Triplet-16th", "16th", "Triplet-8th", "Dotted-16th", "8th",
             "Triplet-Quarter", "Dotted-8th", "Quarter", "Dotted-Quarter"]
    index = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    target = [4]
    total_notes = 6

    try:
        shutil.rmtree("./RESULTS/")
        shutil.rmtree("./COMBI/")
    except:
        os.makedirs("./RESULTS/", exist_ok=True)
        os.makedirs("./COMBI/", exist_ok=True)

    for f, item in enumerate(target):
        os.makedirs("./RESULTS/" + str(item), exist_ok=True)

    TOTAL_SUM = 0
    TOTAL_NOTES_COUNT = 0
    for j, item in enumerate(target):
        TOTAL = 0
        subset_sum(numbers, item, index)
        print("Riffs for 2 : " + str(TOTAL))
        TOTAL_SUM += TOTAL

print("TOTAL Riffs : " + str(TOTAL_SUM))
print("TOTAL Riffs with target note count : " + str(TOTAL_NOTES_COUNT))
