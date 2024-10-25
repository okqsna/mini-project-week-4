def analyze_student_scores(input_file, output_file):
    file = open(input_file, 'r')
    results = []


    for line in file:
        name, scores = line.split(':')
        scores = scores.split(',')
        
        total = 0
        highest = 0
        failed = False
        for score in scores:
            total += int(score)
            if int(score) > highest:
                highest = int(score)
            if int(score) < 75:
                failed = True


        average = total / len(scores)


        results[name] = {
            'average': average,
            'highest': highest,
            'failed': failed
        }
    
    input_file.close()
    
    output_file = open(output_file, 'w')


    output_file.write(results)
    
    output_file.close()
    
    return results
analyze_student_scores('student_scores.txt', '1.txt')