# 등차수열과 참인 값
- 링크: (https://school.programmers.co.kr/learn/courses/30/lessons/181931)
- 난이도: Lv.0

## 왜 어려웠나 (헷갈렸던 부분)

- boolean 값(`True`/`False`)과 문자열(`"true"`/`"false"`)을 헷갈려서 `if sol == "true":`라고 씀
  → `included`는 문제에서 "boolean 배열"이라고 했으니 원소는 실제로 파이썬의 `True`, `False`(따옴표 없는 특별한 값)임. 그런데 `"true"`(따옴표 붙은 문자열)와 비교해버려서, `sol`이 진짜 `True`여도 `sol == "true"`는 항상 `False`로 판정됨
- 에러가 안 나서 원인을 못 찾음
  → `sol == "true"`는 문법적으로 완전히 멀쩡한 코드라서 실행은 잘 됨. 그냥 조건이 항상 거짓으로 판정돼서 `if` 블록이 한 번도 실행 안 되고, `answer`가 초기값 0 그대로 반환됨

## 배운 점

- 파이썬의 boolean 값(`True`, `False`)은 문자열(`"true"`, `"false"`)과 완전히 다른 자료형이다. 따옴표가 붙어있으면 문자열, 안 붙어있고 첫 글자가 대문자면 boolean
- boolean 값은 `if sol:`처럼 조건 자리에 그냥 바로 써도 된다 (`sol`이 이미 True/False 값 자체이기 때문에 `== True`라고 비교할 필요도 없음)
- 자료형을 잘못 비교하면(boolean vs 문자열) 에러 없이 조용히 항상 틀린 결과를 낼 수 있다 — 결과가 이상하게 나오면 "비교 대상의 자료형이 맞는지"부터 의심해보기
- `print(sol, type(sol))`처럼 실제 값과 타입을 같이 찍어보면, 이런 자료형 불일치 버그를 훨씬 빨리 잡을 수 있다

## 최종 풀이
```python
def solution(a, d, included):
    answer = 0
    cnt = 0
    
    for sol in included:
        if sol:
            answer = answer + a + cnt*d
        cnt = cnt + 1
    return answer
```
