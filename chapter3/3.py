def add_score(subject_score, subject, score):
    if not str(subject).strip():
        return subject_score
    if isinstance(score, float) and score.is_integer():
        score = int(score)
    if score <= 0:
        return subject_score
    subject_score[subject] = score
    return subject_score

def calc_average_score(subject_score):
    if len(subject_score) == 0:
        return "0.00"
    avg = sum(subject_score.values()) / len(subject_score)
    return f"{avg:.2f}"

raw = input("Input : ")
try:

    parts= raw.split("|")
    dict_part = eval(parts[0].strip())
    subject_part = eval(parts[1].strip())
    score_part = float(parts[2].strip())

    subject_score = add_score(dict_part, subject_part, score_part)
    avg = calc_average_score(subject_score)

    print(f"{subject_score}, Average score: {avg}")
except Exception:
    # ถ้า error ให้ใช้ dict_part เดิม (แต่ต้องเช็คว่าถูก parse หรือยัง)
    #try:
        dict_part = eval(raw.split("|")[0].strip())
    #except:
        dict_part = {}  # ถ้าพังจริง ๆ ให้เป็น {} ไปเลย

        print(f"{dict_part}, Average score: {calc_average_score(dict_part)}")