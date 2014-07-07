def is_reverse(word1, word2):
  wd1len = len(word1)
  wd2len = len(word2)
  j = wd2len-1
  i = 0

  if(wd1len != wd2len) :
    print ("a length of word1 not equals worda2's that")
    return

  while(j > 0) :
    if word1[i] != word2[j]:
      print ("word is not match")
      return
    i = i + 1
    j = j - 1
  print ("ok")

is_reverse("test", "tset")