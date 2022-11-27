import json

with open('files//kids_quiz.json') as fo:
    content = fo.read()

data = json.loads(content)

score = 0

for question in data:
    print(question['question'])
    for index, variant in enumerate(question['variants'],start=1):
        print(f'{index} - {variant}')
    question['user_answer'] = int(input('Enter number of your answer: '))
    if question['variants'][question['user_answer'] - 1] == question['correct']:
        score += 1
    print()
    
print(f'Your score is: {score}')