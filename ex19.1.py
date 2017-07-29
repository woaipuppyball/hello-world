def booklist(bookname, author, publishdate):
    print "The bookname is %s" % bookname
    print "The author is %s" % author
    print "It's published on %r" % publishdate

print "Here is the info of book1:"
booklist ("Jane", "Eye", 1867/5/5)

print "Here is the info of book2:"
bookname = "Jane2"
author = "author2"
publishdate = 1867/5/5
booklist (bookname,author,publishdate)

print "Here is the info of book3:"
booklist (bookname+'s',author+'author3', publishdate+2)

print "Here is the info of book4:"
author = "author4"
booklist ("Jane4",author,1867/5/5)

print "Here is the info of book 5:"
bookname = "book5"
author = "author5"
booklist (bookname, author, 1867/5/5)
