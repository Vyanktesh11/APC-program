def total_marks(marks): return sum(marks)
def percentage(marks): return total_marks(marks) / (len(marks) * 100) * 100
def grade(percent):
    if percent >= 90: return "A"
    if percent >= 75: return "B"
    if percent >= 60: return "C"
    if percent >= 40: return "D"
    return "F"
