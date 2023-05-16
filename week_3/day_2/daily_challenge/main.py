# --- CHALLENGE 1 --- #
# Instructions :
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
#      * p.getVisibleItems() 
#        ["a", "b", "c", "d"]
# 4) You will have to implement various methods to go through the pages such as:
#    – prevPage()
#    – nextPage()
#    – firstPage()
#    – lastPage()
#    – goToPage(pageNum)
# Here’s a continuation of the example above using nextPage and lastPage:
# alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# p = Pagination(alphabetList, 4)
# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# p.nextPage()
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
# p.lastPage()
# p.getVisibleItems()
# # ["y", "z"]
# Notes
# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided 
# (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPagePage should be set to 5; if 0 or a negative number is given, 
# p.currentPagePage should be set to 1).

# CODE

class Pagination:
    def __init__(self, items = None, pageSize = 10):
      self.items =  items if items is not None else []
      self.pageSize = int(pageSize)
      self.totalPages = len(self.items)
      self.__current = 0
      
    @property
    def currentPage(self): 
      self.__current += 1
      return self.__current

    def getVisibleItems(self):
      return self.items[self.__current:self.__current + self.pageSize]

    def prevPage(self):
      if self.__current >= self.pageSize:
          self.__current -= self.pageSize
      else:
          self.__current = 0
    
    def nextPage(self):
      if self.totalPages - self.__current > self.pageSize:
          self.__current += self.pageSize
      else:
          self.__current += 0
        
    def firstPage(self):
      self.__current = 0

    def lastPage(self):
      self.__current = self.totalPages - 1

    def goToPage(self, pageNum):
      if 0 < pageNum <= self.totalPages:
        self.__current = pageNum - 1 
      else:
        return 'Such page does not exist, sorry'

# OUTPUT

alphabetList = list('abcdefghijklmnopqrstuvwxyz')
p = Pagination(alphabetList, 4)

print(p.getVisibleItems()) # -> ['a', 'b', 'c', 'd']

p.prevPage()
print(p.getVisibleItems()) # -> ['a', 'b', 'c', 'd']

p.nextPage()
print(p.currentPage) # -> 5
print(p.getVisibleItems()) # -> ['f', 'g', 'h', 'i']

p.nextPage()
print(p.currentPage) # -> 10
print(p.getVisibleItems()) # -> ['k', 'l', 'm', 'n']

p.nextPage()
print(p.currentPage) # -> 15
print(p.getVisibleItems()) # -> ['p', 'q', 'r', 's']