from atlassian import Confluence

class ConfluenceClient:
    def __init__(self, url, token):
        self.confluence = Confluence(url=url, token=token)
 
    def get_old_pages(self, space, created_before, limit=100):
        cql = f"space = '{space}' AND type = 'page' AND created < '{created_before}'"
        return self.confluence.cql(cql, limit=limit) 