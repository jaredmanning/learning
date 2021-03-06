the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# HEY CHECK THIS OUT!!
# DID YOU KNOW that when a for-loop uses a variable that hasn't been
# defined yet, it defines that variable and initializes (x = "blank")
# to the current element of the loop iteration every time it loops thorugh

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
# elements = []

#This is the new part from the Study Drill! Nice!
elements = range(0, 6)

# then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)

# now we can print them out too!!
for i in elements:
    print "Element was: %d" % i
