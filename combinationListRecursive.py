def combinationListRecursive(data, r):
  if r == 0 or r > len(data):
    return []

  result = []
  _combinationListRecursive(data, r, 0, [], result)
  return result


def _combinationListRecursive(data, r, start, progress, result):
  if r == 0:
    result.append(progress)
    return

  for i in range(start, len(data)):
    #別解 _combinationListRecursive(listExcludedIndices(data, [i]), r - 1, i, progress + [data[i]], result)
    _combinationListRecursive(data, r - 1, i + 1, progress + [data[i]], result)

combinationListRecursive([2,1,3,5],2)
