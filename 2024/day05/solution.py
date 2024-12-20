from collections import defaultdict

text = open('input.txt').read()
section1, section2 = text.split('\n\n')

rules = section1.splitlines()
updates = section2.splitlines()

rules = [rule.split('|') for rule in rules]

kvs = defaultdict(list)
for rule in rules: kvs[rule[0]].append(rule[1])

print(rules[:5], updates[:5])
for key, value in kvs.items():
    print(key, value)

correct_updates = []
incorrect_updates = []

# Part Two
def correct(update: list):
    local_rules = defaultdict(list)
    for number in update:
        if number not in local_rules:
            local_rules[number].append(0)
        for dep in kvs[number]:
            if dep in update:
                local_rules[number].append(dep)
            
    # print(local_rules)
    print(local_rules)
    print(update)
    corrected = sorted(local_rules.items(), reverse=True, key=lambda pair: len(pair[1]))
    return [pair[0] for pair in corrected]

# Part One
for update in updates:
    update = update.split(',')
    flag = True
    for i in range(len(update) - 1):
        for check in update[i+1:]:
            if check not in kvs[update[i]]:
                # print(check, update[i])
                # print(kvs[update[i]])
                flag = False
                incorrect_updates.append(correct(update))
                break
        if not flag: break
    else: correct_updates.append(update)


print(correct_updates)

print(sum([int(update[len(update)//2]) for update in correct_updates]))
print(sum([int(update[len(update)//2]) for update in incorrect_updates]))

print(len(correct_updates), len(incorrect_updates), len(updates))


    