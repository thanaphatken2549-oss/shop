def add_score(subject_score, student, subject, score):
    # ถ้ายังไม่มี student ให้สร้าง dictionary ว่าง
    if isinstance(score, float) and score.is_integer():
        score = int(score)
    if student not in subject_score:
        subject_score[student] = {}
    # เพิ่มหรืออัปเดตคะแนน
    subject_score[student][subject] = score
    return subject_score


def calc_average_score(subject_score):
    avg_dict = {}
    for student, subjects in subject_score.items():
        avg = sum(subjects.values()) / len(subjects)
        avg_dict[student] = f"{avg:.2f}"
    return avg_dict



raw = input("Input : ")

# แยก input ด้วยเครื่องหมาย |
parts = [x.strip() for x in raw.split("|")]

# part[0] = dictionary ของข้อมูลเดิม (string → dict)
subject_score = eval(parts[0])

# ส่วนต่อไปแบ่งเป็นชุด ๆ ละ 3 ค่า: student, subject, score
i = 1
while i < len(parts):
    student = parts[i]
    subject = parts[i+1].strip().strip("'").strip('"')
    score = float(parts[i+2])
    subject_score = add_score(subject_score, student, subject, score)
    i += 3

avg_score = calc_average_score(subject_score)

print(subject_score, ", Average score:", avg_score)