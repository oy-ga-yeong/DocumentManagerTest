from config import Config
from confluence_client import ConfluenceClient
from document_filter import DocumentFilter


def main():
    # 설정 로드
    config = Config()
    # Confluence API 클라이언트 생성
    client = ConfluenceClient(config.url, config.token)
    # 문서 필터 객체 생성
    doc_filter = DocumentFilter(days=365)
    # 1년 전 날짜 계산
    created_before = doc_filter.get_created_before()
    # 1년 초과 문서 조회
    results = client.get_old_pages(config.space, created_before, limit=100)
    print(results)  # 원본 응답 출력
    # 결과 필터링
    filtered = doc_filter.filter_results(results)
    if not filtered:
        print("조건에 맞는 1년 초과 문서가 없습니다.")
    else:
        for doc in filtered:
            print(f"제목: {doc['title']}")
            print(f"생성일: {doc['created']}")
            print(f"URL: {doc['url']}")
            print('-' * 40)

if __name__ == "__main__":
    main() 