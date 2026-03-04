subject_score = {}
original_avg = 0.00


def input_data():
    raw = input("Input : ").strip()
    if not raw:
        raise ValueError

    parts = [x.strip() for x in raw.split("|")]

    if (len(parts) - 1) % 3 != 0:
        raise ValueError

    return parts


def add_score(subject_score: dict, student: str, subject: str, score):
    if isinstance(score, float) and score.is_integer():
        score = int(score)

    if student not in subject_score:
        subject_score[student] = {}

    subject_score[student][subject] = score
    return subject_score


def calc_average_score(result_subject_score: dict):
    if not result_subject_score:
        return {}

    result_avg_dict = {}

    for student, subjects in result_subject_score.items():
        total = 0
        count = 0

        for score in subjects.values():
            total += float(score)
            count += 1

        avg = total / count if count > 0 else 0.0
        result_avg_dict[student] = f"{avg:.2f}"

    return result_avg_dict


def main():
    global subject_score, original_avg

    parts = input_data()

    subject_score = eval(parts[0])
    if not isinstance(subject_score, dict):
        raise ValueError

    original_avg = calc_average_score(subject_score)

    result = subject_score

    for i in range((len(parts) - 1) // 3):
        idx = 1 + (i * 3)

        student_id = parts[idx]
        subject = parts[idx + 1].strip("'").strip('"')
        score_str = parts[idx + 2]

        if student_id == "" or subject == "":
            raise ValueError
        if score_str in ["", "''", '""']:
            raise ValueError

        score_float = float(score_str)
        if score_float < 0:
            raise ValueError

        real_score = int(score_float) if score_float.is_integer() else score_float

        result = add_score(result, student_id, subject, real_score)

    new_avg = calc_average_score(result)
    print(f"{result}, Average score: {new_avg}")

if __name__ == "__main__":
    try:
        main()
    except:
        #print(f"{subject_score}, Average score: {original_avg}")
        print("Invalid")