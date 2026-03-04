subject_score = {}
original_avg = 0.00

def input_data():
    raw_data = input("Input : ").strip()
    if not raw_data:
        raise ValueError
        
    parts = [x.strip() for x in raw_data.split("|")]
    
    if (len(parts) - 1) % 3 != 0:
        raise ValueError
    return parts

def add_score(subject_score: dict, student: str, subject: str, score: int):
    if student not in subject_score:
        subject_score[student] = {}
    each_subject_dict = {subject: score}
    subject_score[student].update(each_subject_dict)
    return subject_score

def calc_average_score(result_subject_score: dict):
    if not result_subject_score:
        return {}
    result_avg_dict = {}
    for each_student_id, each_student_data in result_subject_score.items():
        sum_score = 0
        count = 0
        for each_course, each_score in each_student_data.items():
            sum_score += float(each_score)
            count += 1
        if count == 0:
            each_avg_score = 0.0
        else:
            each_avg_score = sum_score / count
        result_avg_dict[each_student_id] = f"{each_avg_score:.2f}"
    """
    for value in (result_subject_score.values()).values():
        if not isinstance(value, (int, float)):
             raise ValueError
        sum_score += float(value)
        count += 1 """
        
    return result_avg_dict

def main():
    global subject_score, original_avg
    parts = input_data()
    
    subject_score = eval(parts[0])
    result = subject_score
    if not isinstance(subject_score, dict):
        raise ValueError
        
    original_avg = calc_average_score(subject_score)
    
    #student_data = {}
    for i in range((len(parts) - 1) // 3):
        index_student = 1 + (i * 3)
        
        student_id = parts[index_student]
        subject = parts[index_student + 1].strip("'").strip('"')
        score_str = parts[index_student + 2]
        
        if subject == "" or student_id == "":
            raise ValueError
        if score_str in ["", "''", '""']:
            raise ValueError
        if '-' in score_str:
            raise ValueError
        
        score_float = float(score_str)

        if score_float.is_integer():
            real_score = int(score_float)
        else:
            real_score = score_float
        subject_score = add_score(subject_score, student_id, subject, real_score)
        #each_student_dict = {subject: real_score}
        #if student_id not in student_data:
         #   student_data[student_id] = {}
        #student_data[student_id].update(each_student_dict)

    """
    for each_student_id, each_student_data in student_data.items():
        for course_name, score_course in each_student_data.items():
            result = add_score(subject_score, each_student_id, course_name, score_course) """

        #result = add_score(subject_score, subject, real_score)
    new_avg = calc_average_score(result)

    print(f"{result}, Average score: {new_avg}")