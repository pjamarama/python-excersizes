def queue_time(customers, n):
    tills = [0] * n # создаем список с n прилавков
    
    # повторяем для каждого покупателя
    for k in range(len(customers)):
        # выбираем элемент из tills с наименьшим значением, 
        # прибавляем к нему покупателя
        tills[tills.index(min(tills))] += customers[k]
    
    return max(tills)

print(queue_time([5,3,4], 1))
print(queue_time([10,2,3,3], 2))
print(queue_time([2,3,10], 2))