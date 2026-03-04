subject_score = {}
original_avg = 0.00

def add_score(subject_score, subject, score):
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    if not subject_score:
        return 0.00

    total = 0
    count = 0
    for v in subject_score.values():
        if not isinstance(v, (int, float)):
            raise ValueError
        total += float(v)
        count += 1

    if count == 0:
        return 0.00

    return total / count

raw = input("Input : ")

try:
    parts = [x.strip() for x in raw.split("|")]

    
    if len(parts) != 3:
        raise ValueError

    subject_score = eval(parts[0])
    if not isinstance(subject_score, dict):
        raise ValueError

    original_avg = calc_average_score(subject_score)
    
    subject = parts[1].strip().strip("'").strip('"')
    if subject == "":
        raise ValueError

    score_str = parts[2]
    if score_str in ["", "''", '""']:
        raise ValueError

    score_float = float(score_str)
    if score_float < 0:
        raise ValueError

    if score_float.is_integer():
        real_score = int(score_float)
    else:
        real_score = score_float
        
    result = add_score(subject_score, subject, real_score)
    new_avg = calc_average_score(result)

    print(f"{result}, Average score: {new_avg:.2f}")

except:
    print(f"{subject_score}, Average score: {original_avg:.2f}")
