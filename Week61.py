# main.py — 호출하는 쪽 (13주차에도 이 코드는 그대로 유지된다)
from mock_llm import mock_llm_call

SYSTEM = "당신은 고객 리뷰 분류기입니다."
# review = "배송이 정말 빨라서 만족합니다"
# review = "제품이 파손되었습니다. 환불해주세요"
# review = "제품 품질이 좋아 만족합니다"
# review = "이 가격이면 정말 가성비 최고예요"
review = "상담원이 친절하게 안내해 주셨어요"
# review = "배송은 빨랐는데 품질이 별로라 환불할게요"
result = mock_llm_call(SYSTEM, f"다음 리뷰를 분류하세요: {review}")
print(result["text"])                    # 모델 답변 (JSON 문자열)
print(result["usage"]["output_tokens"])  # 토큰 사용량 확인 습관
