# mock_llm.py — 6~12주차용 모의 LLM 모듈
import random

def mock_llm_call(system, user_message, temperature=0.2, max_tokens=500):
    """실제 API와 동일한 인터페이스를 갖는 모의 함수.
    13주차에 이 함수의 내부만 실제 Anthropic 호출로 교체한다."""
    reviews_keywords = {
        "배송": '{"category": "배송", "sentiment": "긍정", "score": 4}',
        "환불": '{"category": "환불", "sentiment": "부정", "score": 2}',
        "품질": '{"category": "품질", "sentiment": "긍정", "score": 5}', 
        "가격": '{"category": "가격", "sentiment": "긍정", "score": 5}', # 수업 실습: 추가한 규칙 1
        "친절": '{"category": "서비스", "sentiment": "긍정", "score": 4}' # 수업 실습: 추가한 규칙 2
    }
     # ① 기본값: 키워드를 못 찾으면 이게 그대로 나감
    text = '{"category": "기타", "sentiment": "중립", "score": 3}'
     # ② 키워드를 찾으면 text를 덮어쓰고 반복 멈추기
    for keyword, canned in reviews_keywords.items():
        if keyword in user_message:
            text = canned
            break
# ===== 과제 2: 20% 확률로 불량 응답 만들기 =====

    # 메모지 2(stop_reason)에 평소 값 "정상 종료"를 적어둠
    stop_reason = "end_turn"

     # 20% 확률로 불량 응답 만들기
    if random.random() < 0.2: # 불량 종류 세 개 중 하나를 랜덤으로 뽑음
        bad_type = random.choice(["코드펜스", "사족", "잘림"])

        if bad_type == "코드펜스":
            # 불량 ①: 답 앞뒤에 ```json ... ``` 을 씌움 (\n = 줄바꿈)
            text = "```json\n" + text + "\n```"
        elif bad_type == "사족":
            # 불량 ②: 답 앞에 쓸데없는 인사말을 붙임
            text = "물론입니다! 분석 결과는 다음과 같습니다.\n" + text
        else:
            # 불량 ③: 답을 앞에서 20글자만 남기고 잘라버림 (말하다 끊긴 것처럼)
            text = text[:20]
            # 진짜 API는 잘렸을 때 "글자 수 한도에 걸렸다"고 알려주니까 그것도 흉내 냄
            stop_reason = "max_tokens"

 # 메모지 1, 2에 적힌 값을 담아서 건네주고 함수 끝 (실제 API 응답 모양 흉내)
    return {"text": text, "stop_reason": stop_reason,
                    "usage": {"input_tokens": 120, "output_tokens": 35}}
  
