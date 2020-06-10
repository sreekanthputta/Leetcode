class BrowserHistory:

    browsed = None
    currentPage = None
    def __init__(self, homepage: str):
        self.currentPage = 0
        self.browsed = [homepage]

    def visit(self, url: str) -> None:
        self.currentPage += 1
        del self.browsed[self.currentPage:]
        self.browsed.append(url)

    def back(self, steps: int) -> str:
        self.currentPage = (self.currentPage - steps) if self.currentPage>steps else 0
        return self.browsed[self.currentPage]

    def forward(self, steps: int) -> str:
        self.currentPage = (self.currentPage + steps) if len(self.browsed)-self.currentPage>steps else len(self.browsed)-1
        return self.browsed[self.currentPage]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)