# 1. Two Sum

> **작성일**: 2025년 9월 26일

## 문제 설명
정수 배열 `nums`와 정수 `target`이 주어졌을 때, 두 수의 합이 `target`이 되는 두 수의 인덱스를 반환하는 문제입니다.

- 정확히 하나의 해답이 존재한다고 가정할 수 있습니다.
- 같은 원소를 두 번 사용할 수 없습니다.
- 답은 어떤 순서로든 반환할 수 있습니다.

## 제약사항
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- 유효한 답이 정확히 하나만 존재합니다.

## 해결 방법

### 방법 1: 브루트 포스 (Brute Force)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

**장점:**
- 직관적이고 이해하기 쉬운 접근법
- 추가 공간이 필요하지 않음

**단점:**
- **시간복잡도**: O(n²) - 이중 반복문으로 인한 비효율
- **공간복잡도**: O(1)

### 방법 2: 브루트 포스 변형 (in 연산자 사용)
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for idx, num in enumerate(nums):
        remain = target - num
        if remain in nums[idx+1:]:
            output = [idx, nums.index(remain, idx+1)]
            return output
```

**특징:**
- `in` 연산자와 슬라이싱을 활용
- 여전히 O(n²) 시간복잡도

### 방법 3: 해시 맵 (Hash Map) - 최적화된 해법
```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

**핵심 아이디어:**
- **해시 맵 활용**: 값을 키로, 인덱스를 값으로 저장
- **한 번의 순회**: 배열을 한 번만 순회하면서 해답 찾기
- **complement 검색**: `target - current_num`이 이미 본 값인지 확인

**시간복잡도**: O(n) - 배열을 한 번만 순회
**공간복잡도**: O(n) - 해시 맵에 최대 n개 원소 저장

## 알고리즘 동작 과정

### 예시: nums = [2,7,11,15], target = 9

**초기 상태:**
```
nums: [2, 7, 11, 15]
target: 9
num_map: {}
```

**Step 1:** i=0, num=2
- complement = 9 - 2 = 7
- 7이 num_map에 없음
- num_map[2] = 0 저장
```
num_map: {2: 0}
```

**Step 2:** i=1, num=7
- complement = 9 - 7 = 2
- 2가 num_map에 존재! (인덱스 0)
- 반환: [num_map[2], 1] = [0, 1]

**최종 결과:** `[0, 1]`

### 예시 2: nums = [3,2,4], target = 6

**Step 1:** i=0, num=3 → complement=3, num_map에 없음 → num_map={3: 0}
**Step 2:** i=1, num=2 → complement=4, num_map에 없음 → num_map={3: 0, 2: 1}  
**Step 3:** i=2, num=4 → complement=2, num_map에 존재! → 반환 [1, 2]

### 예시 3: nums = [3,3], target = 6

**Step 1:** i=0, num=3 → complement=3, num_map에 없음 → num_map={3: 0}
**Step 2:** i=1, num=3 → complement=3, num_map에 존재! → 반환 [0, 1]

## 에지 케이스 처리

### Case 1: 동일한 값이 여러 개 있는 경우
```python
nums = [3, 3], target = 6
# 첫 번째 3의 인덱스(0)와 두 번째 3의 인덱스(1) 반환
```

### Case 2: 최소 크기 배열
```python
nums = [1, 2], target = 3
# 항상 유효한 답이 하나 존재한다고 보장됨
```

### Case 3: 음수가 포함된 경우
```python
nums = [-1, -2, -3, -4, -5], target = -8
# complement 계산 시 음수 + 음수 = 더 작은 음수
```

## 시간/공간 복잡도 비교

| 방법 | 시간복잡도 | 공간복잡도 | 장점 | 단점 |
|------|------------|------------|------|------|
| 브루트 포스 | O(n²) | O(1) | 구현 단순, 공간 효율 | 느린 실행 시간 |
| 해시 맵 | O(n) | O(n) | 빠른 실행 시간 | 추가 메모리 필요 |

## 핵심 포인트

1. **해시 맵의 활용**: 
   - 값 → 인덱스 매핑으로 O(1) 검색
   - `complement = target - current_num` 패턴

2. **한 번의 순회로 해결**:
   - 과거에 본 값들을 해시 맵에 저장
   - 현재 값의 complement가 과거에 있었는지 확인

3. **인덱스 순서**:
   - 먼저 나온 값의 인덱스가 앞에 오도록 반환
   - `[num_map[complement], i]`

4. **중복값 처리**:
   - 같은 값이라도 인덱스가 다르면 다른 원소로 취급

## Follow-up 질문 분석

**"Can you come up with an algorithm that is less than O(n²) time complexity?"**

→ **해시 맵 방법이 정답**: O(n) 시간복잡도로 O(n²)보다 효율적

**다른 접근법들:**

### 정렬 + 투 포인터 (하지만 인덱스 보존 문제)
```python
def twoSum_sorted(self, nums, target):
    # 문제점: 정렬하면 원래 인덱스를 잃어버림
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

이 방법도 O(n log n)으로 해시 맵보다 느립니다.

## 최적해 구현 세부사항

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    num_map = {}  # 값 → 인덱스 매핑
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # complement가 이미 해시 맵에 있으면 답을 찾은 것
        if complement in num_map:
            return [num_map[complement], i]
        
        # 현재 값과 인덱스를 해시 맵에 저장
        num_map[num] = i
    
    # 문제에서 해답이 항상 존재한다고 했으므로 여기는 실행되지 않음
    return []
```

**왜 이 순서가 중요한가:**
1. 먼저 complement 검사 → 중복값 처리 가능
2. 나중에 현재 값 저장 → 같은 원소 두 번 사용 방지

## 결론

**해시 맵 방법이 최적의 해결책**:
- ✅ **시간복잡도**: O(n) - 선형 시간
- ✅ **공간복잡도**: O(n) - 허용 가능한 수준
- ✅ **직관적**: complement 패턴이 명확
- ✅ **확장성**: 배열 크기가 커져도 효율적

Two Sum은 해시 맵의 강력함을 보여주는 대표적인 문제로, **"검색을 O(1)으로 만들기 위해 추가 공간을 사용한다"**는 트레이드오프의 좋은 예시입니다.