words = ["Python", "Java", "C++", "C", "C#", "Rust", "Go", "JavaScript", "Swift", "Kotlin", "R"]
#reversing the list
"""new=words[::-1]
print(new)
"""

#reversing the words in the list using map function
new =list(map(lambda word: word[::-1],words))
print(new)

#['nohtyP', 'avaJ', '++C', 'C', '#C', 'tsuR', 'oG', 'tpircSavaJ', 'tfiwS', 'niltoK', 'R']