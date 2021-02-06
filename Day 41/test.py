a, b, c = map(int, input().split())

largestDigitSum = int(max(str(a))) + int(max(str(b))) + int(max(str(c)))
smallestDigitSum = int(sorted(str(a))[0]) + int(sorted(str(b))[0]) + int(sorted(str(c))[0])

print(largestDigitSum+smallestDigitSum)