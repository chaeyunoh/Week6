import json
from mock_llm import mock_llm_call   # 1차시에 만든 모듈 재사용

SYSTEM = """당신은 고객 리뷰 분류기입니다.
반드시 아래 JSON 형식으로만 응답하세요. 다른 텍스트를 절대 포함하지 마세요.
{"category": "배송|품질|가격|서비스|기타",
 "sentiment": "긍정|부정|중립",
 "score": 1~5 사이의 정수}"""

def classify_review(review_text):
    """리뷰 1건을 분류하여 딕셔너리로 반환. 실패 시 None."""
    result = mock_llm_call(SYSTEM, f"리뷰: {review_text}")
    raw = result["text"].strip() # 결과 텍스트의 앞뒤 불필요한 공백과 줄바꿈을 제거

    # 방어 1: 마크다운 코드 블록 제거 (포맷 정규화): ```json ... ``` 코드 제거
    if raw.startswith("```"):
        raw = raw.strip("`")  # 문자열의 시작과 끝에 붙은 백틱(`)만 모두 제거
        raw = raw.replace("json", "", 1).strip() # "json"을 한번만(1회) 지우고 strip()

    # 방어 2: 파싱 실패는 언제든 일어날 수 있다 → 예외 처리 필수
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        print(f"[경고] JSON 파싱 실패: {raw[:50]}...")
        return None

    # 방어 3: 필드 존재와 값의 유효성 검증
    if data.get("category") not in ["배송", "품질", "가격", "환불", "서비스", "기타"]:
        return None
    return data

# 비즈니스 로직에 바인딩: 리뷰 목록 자동 분류 및 집계
reviews = [
    "배송이 하루 만에 왔어요 최고",
    "품질이 사진과 너무 달라요",
    "환불 처리가 왜 이렇게 느린가요",
    "상담 직원이 친절하였어요",
]
# ===== 비즈니스 로직 바인딩: 리뷰 자동 분류 및 집계 =====
# 과제 2: 불량 응답을 만나도 파이프라인이 중단되지 않고, 실패 건수를 집계하여 출력

stats = {}        # 카테고리별 분류 건수 집계
ok_count = 0      # 처리(분류 성공) 건수
fail_count = 0    # 실패 건수 (classify_review가 None을 반환한 경우)

for r in reviews:
    result = classify_review(r)      # 리뷰 1건 분류 → 성공 시 dict, 실패 시 None

    # 실패 건: 프로그램을 중단하지 않고 건수만 기록한 뒤 다음 리뷰로 진행
    if result is None:
        fail_count += 1
        print(f"[실패] {r}")
        continue

    # 성공 건: 처리 건수 증가 및 카테고리별 집계
    ok_count += 1
    cat = result["category"]
    stats[cat] = stats.get(cat, 0) + 1
    print(f"[성공] {r} → {result}")   # 건별 분류 결과 출력

# 파이프라인 종료 후 최종 집계 출력
print(stats)
print(f"처리 {ok_count}건 / 실패 {fail_count}건 (전체 {len(reviews)}건)")