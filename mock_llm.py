# mock_llm.py — 6~12주차용 모의 LLM 모듈
import random

# 불량 응답 유형별 발생 건수 집계 (과제 2: 복구 건수 보고용)
bad_stats = {"코드펜스": 0, "사족": 0, "잘림": 0}

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    """실제 API와 동일한 인터페이스를 갖는 모의 함수.
    13주차에 이 함수의 내부만 실제 Anthropic 호출로 교체한다."""

    # 키워드 → 사전 정의된 응답(JSON 문자열) 매핑
    reviews_keywords = {
        "배송": '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불": '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질": '{"category": "품질", "sentiment": "긍정", "score": 5}',
        "가격": '{"category": "가격", "sentiment": "긍정", "score": 5}',    # 실습: 추가 규칙 1
        "친절": '{"category": "서비스", "sentiment": "긍정", "score": 4}'   # 실습: 추가 규칙 2
    }

    # 기본 응답: 일치하는 키워드가 없을 경우 반환
    text = '{"category": "기타", "sentiment": "중립", "score": 3}'

    # 키워드 매칭: 딕셔너리 순서대로 검사하여 첫 번째로 일치한 응답을 사용
    for keyword, canned in reviews_keywords.items():
        if keyword in user_message:
            text = canned
            break

    # ===== 과제 2: 20% 확률로 불량 응답 반환 =====

    # 정상 종료 시 stop_reason
    stop_reason = "end_turn"

    # 20% 확률로 불량 응답 유형 3가지 중 1개를 무작위 선택
    if random.random() < 0.2:
        bad_type = random.choice(["코드펜스", "사족", "잘림"])
        bad_stats[bad_type] += 1   # 해당 유형의 발생 건수 1 증가


        if bad_type == "코드펜스":
            # 불량 유형 1: 마크다운 코드펜스(```json ... ```)로 감싼 응답
            text = "```json\n" + text + "\n```"

        elif bad_type == "사족":
            # 불량 유형 2: JSON 앞에 불필요한 설명 문장이 포함된 응답
            text = "물론입니다! 분석 결과는 다음과 같습니다.\n" + text

        else:
            # 불량 유형 3: max_tokens 도달로 중간에 잘린 JSON 응답
            text = text[:20]
            stop_reason = "max_tokens"

    # 실제 API 응답 형식(text, stop_reason, usage)으로 반환
    return {"text": text, "stop_reason": stop_reason,
            "usage": {"input_tokens": 120, "output_tokens": 35}}