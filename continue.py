#continue is used to skip the current iteration of the loop and continue with the next iteration.
#example
#
# #continue to the next iteration if i is 3
i = 0
while i < 10:
    i += 1
    if i == 8:
        continue
    print(i)

