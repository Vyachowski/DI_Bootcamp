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
# (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, 
# p.currentPage should be set to 1).

# CODE

class Pagination:
    def __init__(self, items = None, pageSize = 10) -> None:
      self.items = items
      self.size = int(pageSize)
      self.current = 0

    def getVisibleItems(self):
      if self.items == None: return 'There is no data or data type is wrong. Should be a list.'
      return self.items[self.current:self.current + self.size]
      
    def prevPage(self):
      self.current -= self.size if self.current - self.size >= 0 else 0
    
    def nextPage(self):
      self.current += self.size if len(self.items) - (self.current) > self.size else 0
        
    def firstPage(self):
      self.current = 0

    def lastPage(self):
      self.current = len(self.items) - 1

    def goToPage(pageNum):
      pass

# OUTPUT

alphabetList = list('abcdefghijklmnopqrstuvwxyz')
p = Pagination(alphabetList)

print(p.getVisibleItems())

p.prevPage()
print(p.current)
print(p.getVisibleItems())

p.nextPage()
print(p.current)
p.nextPage()
print(p.current)
p.nextPage()
print(p.current)
p.nextPage()
print(p.current)
print(p.getVisibleItems())

