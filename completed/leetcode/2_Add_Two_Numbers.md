# 2. Add Two Numbers

> **작성일**: 2025년 9월 26일

## 문제 설명
두 개의 비어있지 않은 연결 리스트가 주어지며, 이들은 두 개의 음이 아닌 정수를 나타냅니다. 숫자들은 **역순**으로 저장되어 있고, 각 노드는 하나의 숫자를 포함합니다. 두 수를 더해서 합을 연결 리스트로 반환하는 문제입니다.

- 두 수는 0을 제외하고는 leading zero를 포함하지 않는다고 가정할 수 있습니다.
- 숫자가 역순으로 저장되어 있어 덧셈이 쉽게 수행됩니다.

## 제약사항
- 각 연결 리스트의 노드 수는 `[1, 100]` 범위입니다.
- `0 <= Node.val <= 9`
- 리스트가 나타내는 수는 leading zero가 없음이 보장됩니다.

## 해결 방법

### 핵심 아이디어: 자리수별 덧셈 + 캐리 처리
```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    output_l = ListNode(0)  # 더미 노드
    curr = output_l
    
    while l1 or l2 or carry:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        n_sum = l1_val + l2_val + carry
        
        carry = n_sum // 10  # 다음 자리로 올림
        curr.next = ListNode(n_sum % 10)  # 현재 자리 숫자
        curr = curr.next
        
        # 다음 노드로 이동
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return output_l.next  # 더미 노드 제외하고 반환
```

**핵심 개념:**
- **더미 노드 활용**: 결과 리스트의 시작점을 쉽게 관리
- **캐리(Carry) 처리**: 두 자리수 합이 10 이상일 때 다음 자리로 전달
- **동시 순회**: 두 리스트를 동시에 순회하면서 처리
- **길이 차이 처리**: 한 리스트가 끝나도 다른 리스트와 캐리가 남아있으면 계속 진행

**시간복잡도**: O(max(m, n)) - 더 긴 리스트의 길이만큼
**공간복잡도**: O(max(m, n)) - 결과 리스트의 크기

## 알고리즘 동작 과정

### 예시 1: l1 = [2,4,3], l2 = [5,6,4] (342 + 465 = 807)

**초기 상태:**
```
l1: 2 -> 4 -> 3 -> None  (represents 342)
l2: 5 -> 6 -> 4 -> None  (represents 465)
carry: 0
result: 0 (더미)
```

**Step 1:** 첫 번째 자리 (2 + 5 + 0)
```
l1_val = 2, l2_val = 5, carry = 0
n_sum = 2 + 5 + 0 = 7
carry = 7 // 10 = 0
result: 0 -> 7
```

**Step 2:** 두 번째 자리 (4 + 6 + 0)
```
l1_val = 4, l2_val = 6, carry = 0
n_sum = 4 + 6 + 0 = 10
carry = 10 // 10 = 1
result: 0 -> 7 -> 0
```

**Step 3:** 세 번째 자리 (3 + 4 + 1)
```
l1_val = 3, l2_val = 4, carry = 1
n_sum = 3 + 4 + 1 = 8
carry = 8 // 10 = 0
result: 0 -> 7 -> 0 -> 8
```

**최종 결과:** `[7,0,8]` (represents 807)

### 예시 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] (9999999 + 9999 = 10009998)

이 예시는 **캐리 전파**의 좋은 예시입니다:

**Step 1-4:** 각 자리에서 9 + 9 = 18, carry = 1 발생
```
9 + 9 + 0 = 18 → digit = 8, carry = 1
9 + 9 + 1 = 19 → digit = 9, carry = 1
9 + 9 + 1 = 19 → digit = 9, carry = 1
9 + 9 + 1 = 19 → digit = 9, carry = 1
```

**Step 5-7:** l2가 끝났지만 l1과 carry가 남음
```
9 + 0 + 1 = 10 → digit = 0, carry = 1
9 + 0 + 1 = 10 → digit = 0, carry = 1
9 + 0 + 1 = 10 → digit = 0, carry = 1
```

**Step 8:** l1도 끝났지만 carry가 남음
```
0 + 0 + 1 = 1 → digit = 1, carry = 0
```

**최종 결과:** `[8,9,9,9,0,0,0,1]` (represents 10009998)

## 에지 케이스 처리

### Case 1: 한 리스트가 다른 리스트보다 짧은 경우
```python
l1 = [9,9], l2 = [1]  # 99 + 1 = 100
# l2가 먼저 끝나지만 l1과 carry 처리 계속
```

### Case 2: 마지막에 캐리가 발생하는 경우
```python
l1 = [5], l2 = [5]  # 5 + 5 = 10
# 두 리스트가 모두 끝났지만 carry = 1이 남아서 추가 노드 생성
```

### Case 3: 한 리스트만 있는 경우 (이론상)
```python
l1 = [1,2,3], l2 = []  # 하지만 문제에서 두 리스트 모두 비어있지 않다고 보장
```

### Case 4: 최소 케이스
```python
l1 = [0], l2 = [0]  # 0 + 0 = 0
# carry 없이 간단하게 처리
```

## 핵심 구현 포인트

### 1. 더미 노드 패턴
```python
output_l = ListNode(0)  # 더미 노드 생성
curr = output_l         # 현재 위치 포인터

# 처리 과정...

return output_l.next    # 더미 노드 제외하고 반환
```

**장점:**
- 첫 번째 노드를 특별 처리할 필요 없음
- 코드 일관성 유지
- 빈 결과 처리 용이

### 2. 조건부 값 할당
```python
l1_val = l1.val if l1 else 0
l2_val = l2.val if l2 else 0
```

**대신 사용 가능한 방법:**
```python
# 방법 1: try-except
try:
    l1_val = l1.val
except AttributeError:
    l1_val = 0

# 방법 2: and 연산자
l1_val = l1 and l1.val or 0
```

### 3. 루프 조건의 중요성
```python
while l1 or l2 or carry:
```

- `l1 or l2`: 둘 중 하나라도 남아있으면 계속
- `carry`: 마지막 캐리 처리까지 완료

## 연결 리스트 기본 개념

### ListNode 클래스 구조
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 연결 리스트 순회 패턴
```python
# 기본 순회
current = head
while current:
    print(current.val)
    current = current.next

# 조건부 순회 (None 체크)
while l1 or l2:
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    l1 = l1.next if l1 else None
    l2 = l2.next if l2 else None
```

## 다른 접근법들

### 방법 1: 재귀적 접근
```python
def addTwoNumbers(self, l1, l2, carry=0):
    if not l1 and not l2 and not carry:
        return None
    
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    
    node = ListNode(total % 10)
    node.next = self.addTwoNumbers(
        l1.next if l1 else None,
        l2.next if l2 else None,
        total // 10
    )
    return node
```

**장단점:**
- ✅ 코드가 간결하고 직관적
- ❌ 리스트가 길면 스택 오버플로우 위험

### 방법 2: 숫자 변환 후 계산 (비권장)
```python
def addTwoNumbers(self, l1, l2):
    # 연결 리스트를 숫자로 변환
    num1 = self.listToNumber(l1)
    num2 = self.listToNumber(l2)
    
    # 더한 후 다시 연결 리스트로 변환
    result = num1 + num2
    return self.numberToList(result)
```

**문제점:**
- 매우 큰 수의 경우 정수 오버플로우
- 연결 리스트의 장점을 활용하지 못함

## 시간/공간 복잡도 분석

| 접근법 | 시간복잡도 | 공간복잡도 | 장점 | 단점 |
|--------|------------|------------|------|------|
| 반복적 | O(max(m,n)) | O(max(m,n)) | 안정적, 직관적 | - |
| 재귀적 | O(max(m,n)) | O(max(m,n)) | 코드 간결 | 스택 오버플로우 위험 |
| 숫자 변환 | O(m+n) | O(max(m,n)) | 이해 쉬움 | 큰 수 처리 불가 |

## 실제 응용 사례

1. **큰 수 연산 라이브러리**: Python의 `decimal` 모듈과 유사한 원리
2. **암호학**: RSA 암호화에서 매우 큰 소수 연산
3. **금융 시스템**: 정확한 소수점 계산이 필요한 경우
4. **과학 계산**: 임의 정밀도 연산이 필요한 경우

## 결론

**Add Two Numbers는 연결 리스트와 수학적 사고를 결합한 문제**:
- ✅ **자료구조 활용**: 연결 리스트의 특성을 잘 활용
- ✅ **수학적 사고**: 자릿수별 덧셈과 캐리 처리
- ✅ **에지 케이스**: 길이 차이, 마지막 캐리 등 꼼꼼한 처리
- ✅ **실용성**: 실제 큰 수 연산 라이브러리의 기본 원리

이 문제는 **"간단해 보이지만 세심한 주의가 필요한"** 전형적인 예시로, 연결 리스트 조작과 수학적 로직을 동시에 다루는 능력을 평가합니다.