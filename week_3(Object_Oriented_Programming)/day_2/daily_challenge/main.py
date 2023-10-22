# --- CHALLENGE 1 --- #
# Instructions:
# 1) Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.
# 2) The Pagination class will accept 2 parameters:
#    – items (default: None): It will contain a list of contents to paginate.
#    – pageSize (default: 10): The amount of items to show in each page.
#    So for example we could initialize our pagination like this:
#    * alphabetList = list("abcdefghijklmnopqrstuvwxyz")
#    * p = Pagination(alphabetList, 4)
# 3) The Pagination class will have a few methods:
#    – getVisibleItems() : returns a list of items visible depending on the pageSize
#    – So for example we could use this method like this:
#      p.getVisibleItems() 
#      # ["a", "b", "c", "d"]
# 4) You will have to implement various methods to go through the pages such as:
#    – prevPage()
#    – nextPage()
#    – firstPage()
#    – lastPage()
#    – goToPage(pageNum)
# 5) Here’s a continuation of the example above using nextPage and lastPage:
#    – alphabetList = list("abcdefghijklmnopqrstuvwxyz")
#    – p = Pagination(alphabetList, 4)
#    – p.getVisibleItems() 
#      # ["a", "b", "c", "d"]
#      p.nextPage()
#      p.getVisibleItems()
#      # ["e", "f", "g", "h"]
#      p.lastPage()
#      p.getVisibleItems()
#      # ["y", "z"]
# Notes:
# – The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# – The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# – Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# – If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided 
#   (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, 
#    p.currentPage should be set to 1).

# CODE

class Pagination:
    def __init__(self, items = None, pageSize = 10):
      self.items =  list(items) if items is not None else []
      self.pageSize = int(pageSize)
      # eg. [1, 2, 3, 4, 5, 6, 7] => [[1, 2, 3],[4, 5, 6],[7]] – Group content in pages
      self.__pagesList = [self.items[start_point:start_point + pageSize] for start_point in range(0, len(self.items), pageSize)]
      self.totalPages = len(self.__pagesList)
      self.__currentIndex = 0
      self.__lastIndex = self.totalPages - 1

    @property
    def currentPage(self): 
      current_page = self.__currentIndex + 1
      return current_page
    
    def getVisibleItems(self):
      return self.__pagesList[self.__currentIndex]

    def prevPage(self):
      self.__currentIndex -= 1 if self.__currentIndex > 0 else 0

    def nextPage(self):
      self.__currentIndex += 1 if  self.__currentIndex < self.__lastIndex else 0
        
    def firstPage(self):
      self.__currentIndex = 0

    def lastPage(self):
      self.__currentIndex = self.__lastIndex

    def goToPage(self, pageNum):
      if 0 < int(pageNum) <= self.totalPages:
        self.__currentIndex = pageNum - 1 
      elif int(pageNum) > self.totalPages:
        self.__currentIndex = self.__lastIndex
      else:
        self.__currentIndex = 0
      
# OUTPUT

alphabetList = 'abcdefghijklmnopqrstuvwxyz'
p = Pagination(alphabetList, 4)

print('\nTEST #1:')
print(p.getVisibleItems())   # -> ['a', 'b', 'c', 'd']
print(p.totalPages)          # -> 7
print(p.currentPage)         # -> 1

print('\nTEST #2:')
p.prevPage()               
print(p.currentPage)         # -> 1
print(p.getVisibleItems())   # -> ['a', 'b', 'c', 'd']

p.nextPage()
print(p.currentPage)         # -> 2
print(p.getVisibleItems())   # -> ['e', 'f', 'g', 'h']

p.prevPage()
print(p.currentPage)         # -> 1
print(p.getVisibleItems())   # -> ['a', 'b', 'c', 'd']


print('\nTEST #3:')
p.nextPage()
p.nextPage()
p.nextPage()
p.nextPage()
p.nextPage()                 
print(p.currentPage)         # -> 6
print(p.getVisibleItems())   # -> ['u', 'v', 'w', 'x']

p.nextPage()
p.nextPage()
p.nextPage()                 # -> Some extra .nextPage method to check "Out of Range"
print(p.currentPage)         # -> 7
print(p.getVisibleItems())   # -> ['y', 'z']

print('\nTEST #4:')
p.goToPage(1)
print(p.getVisibleItems())   # -> ['a', 'b', 'c', 'd']
p.lastPage()
print(p.getVisibleItems())   # -> ['y', 'z']
p.goToPage(-100)
print(p.getVisibleItems())   # -> ['a', 'b', 'c', 'd']
p.goToPage(100)
print(p.getVisibleItems())   # -> ['y', 'z']