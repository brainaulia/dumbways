# input: ccbabaccffpgkkklll
# output: cbafpgkl


def saring_duplikat(kata):
  nodupe=''
  for i in kata:
    if i not in nodupe:
      nodupe+=i

  return nodupe

kata='ccbabaccffpgkkklll'
print("input:",kata)
print("output:",saring_duplikat(kata))


