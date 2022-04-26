def powerset_helper(pointer, choices_made, inputSet, result):
    if (pointer < 0):
        result.append(choices_made.copy())
        return

    choices_made.append(inputSet[pointer])
    powerset_helper(pointer - 1, choices_made, inputSet, result)

    choices_made.pop()
    powerset_helper(pointer - 1, choices_made, inputSet, result)


def powerset(inputSet):
    result = []
    powerset_helper(len(inputSet)-1, [], inputSet, result)
    return result

inputSet = [1,2,3]
print(powerset(inputSet))
