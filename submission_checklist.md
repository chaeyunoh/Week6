# 6주차 제출 체크리스트

- 작성자: 오채윤 (20210809)
- 개인 저장소: https://github.com/chaeyunoh/Week6
- 팀 저장소: https://github.com/benebeau214/Team_Decoders

| 번호 | 확인 항목 | 확인 | 근거 위치 |
|---|---|---|---|
| 1 | 과제 1: 프롬프트 3종 전문과 15개 조합 실행 기록 포함 | ■ | `report.md` 2장(프롬프트 전문), 3.1절(15개 조합 결과 표), `captures/task1_*` |
| 2 | 과제 1: 반복 실행 3회의 일관성 관찰 결과 포함 | ■ | `report.md` 3.3절(사례 5, 기법별 3회), 4.4절 분석 |
| 3 | 과제 1: 테스트 입력에 PII가 없는지 확인 (5주차 보안 체크리스트 첨부) | □ | `security_checklist.md` S1, `report.md` 6장 |
| 4 | 과제 2: 불량 응답 시에도 파이프라인이 정상 종료됨을 캡처로 증명 | ■ | `captures/task2_pipeline_v2.png` (경고 줄, 처리·실패 건수, 불량·복구 건수), `README.md` |
| 5 | 과제 2: 의미 단위 3커밋 이상, 커밋 메시지 규칙 준수 | ■ | 아래 커밋 목록 참고 |
| 6 | 과제 3: 팀 가주제 후보 2~3개와 리스크 분석 표 포함 | ■ | 팀 저장소 `team_brainstorm.md` (후보 A·B·C, 후보 비교 표의 최대 리스크 항목) |
| 7 | AI 사용 기록(프롬프트·채택 내역) 첨부 | □ | `usage_log.md` |
| 8 | GitHub 저장소 링크 제출 (커밋 히스토리 공개 상태 확인) | □ | 위 저장소 링크 2개, 두 저장소 모두 공개 상태 |

## 과제 2 커밋 목록

| 순서 | 커밋 메시지 | 내용 |
|---|---|---|
| 1 | `feat: add random bad responses to mock llm call` | 20% 확률 불량 응답(코드펜스·사족·잘림) 생성 |
| 2 | `feat: count processed and failed reviews in pipeline` | 처리·실패 건수 집계 및 출력 |
| 3 | `feat: add stop_reason check and preamble removal to classify_review` | 잘림 사전 감지, 사족 복구 |
| 4 | `feat: load reviews from csv and run full pipeline` | 리뷰 36건 전체 실행 |
| 5 | `feat: report bad response counts by type and recovery` | 불량 유형별 건수와 복구 건수 출력, README 설명 |
