def calculate_stats(numbers):
    total_sum =sum(numbers)
    average = total_sum / len(numbers)
    maximun = max(numbers)
    minimun = min(numbers)
    return total_sum,average,maximun,minimun
numbers = [5,10,15,20,25]
total,avg,max_num,min_num = calculate_stats(numbers)

print(f"total_sum: {total}")
print(f"Average: {avg}")
print(f"Maximun: {max_num}")
print(f"Minimun: {min_num}")