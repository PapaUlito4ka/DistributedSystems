from typing import Dict, List


class SearchService:

    @staticmethod
    def search(posts: List[Dict], query: str):
        return list(filter(lambda post: query in post['title'] or query in post['body'], posts))
