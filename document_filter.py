from datetime import datetime, timedelta

class DocumentFilter:
    def __init__(self, days=365):
        self.days = days

    def get_created_before(self):
        return (datetime.now() - timedelta(days=self.days)).strftime('%Y-%m-%d')

    def filter_results(self, results):
        # Confluence CQL 결과에서 필요한 정보만 추출
        filtered = []
        for result in results.get('results', []):
            filtered.append({
                'id': result.get('id'),
                'title': result.get('title'),
                'created': result.get('history', {}).get('createdDate'),
                'url': result.get('_links', {}).get('base') + result.get('_links', {}).get('webui') if result.get('_links') else None
            })
        return filtered 