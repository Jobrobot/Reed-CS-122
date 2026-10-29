def down_up(num):
    
    if num == 1:
        return[1]
        
    return [num] + down_up(num - 1) + [num]