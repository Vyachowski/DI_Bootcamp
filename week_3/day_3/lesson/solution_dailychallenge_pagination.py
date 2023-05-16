import math

class Pagination:

    def __init__(self, items=None, page = 10):
        self.items = items
        self.page_size = int(page)
        self.current_page = 1
        self.total_pages = math.ceil(len(self.items)/self.page_size)

    def get_visible_items(self):
           return self.items[self.page_size*(self.current_page-1):self.page_size*(self.current_page)]

    def next_page(self):
        print(f"you are in the {self.current_page} page")
        if self.current_page < self.total_pages :
            self.current_page += 1
            print(f"you moved to {self.current_page} page")
        elif self.current_page == self.total_pages :
            print("you came back to the first page")
            self.current_page = 1
        return self

    def prev_page(self):
        print(f"you are in the {self.current_page} page")
        if self.current_page > 1 :
            self.current_page -= 1
            print(f"you moved to {self.current_page} page")
        else :
            print(f"you requested a wrong page")
            self.current_page = self.total_pages
            print(f"you moved to {self.current_page} page")
        return self
    
    def go_to_page(self,page_num) :            
        if page_num <= 0 :
            print(f"you requested a wrong page, you moved to the first page")
            self.current_page = 1
        else :
            if page_num <= self.total_pages:
                self.current_page = page_num
            else :
                print(f"you requested a wrong page, you moved to the last page")
                self.current_page = self.total_pages


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(p.get_visible_items())
p.next_page()
print(p.get_visible_items())