### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #missing '='
      return True
    else #missing ':'
      return False
   

  #function not defined. def not dif
  dif highest_card(self, card1 card2): #missing "," between card1 & card2
  if card1.value > card2.value: 
    return card #card parameter doesn't exist. card1.
  else:
    return card2

# if else needs indented above.
  

#function not part of class. Indentation. 
def cards_total(self, cards):
  #total not been assigned any value
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total 
    # missing space between of and end of string.
    #indentation, loop will exit after first iteration.
  
```
