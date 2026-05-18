def find_connecting_routes(routes, target_layover):
    # routes is an sorted list
    left = 0
    right = len(routes) - 1
    
    while left < right:
        current_layover = routes[left] + routes[right]
        
        if current_layover == target_layover:
            return (routes[left], routes[right]) # ಸೂಕ್ತವಾದ ರೂಟ್ ಜೋಡಿ
        elif current_layover < target_layover:
            left += 1 # we need more time, hence move the pointer right
        else:
            right -= 1 # we need less time, hence move the pointer left
            
    return None