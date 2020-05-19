# We are given an array asteroids of integers representing asteroids in a row.
# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


def asteroidCollision(asteroids):
    stack = []
    i = 0

    while i < len(asteroids):
        current_asteroid = asteroids[i]
        # if stack is empty
        # or last item in stack is negative
        # or last item in stack is positive and current item is positive
        if len(stack) == 0 or stack[-1] < 0 or (stack[-1] >= 0 and current_asteroids >= 0):
            # if so, add the item to the stack
            stack.append(current_asteroid)
        else:
            # if current is equal to last item in stack
            if abs(current_asteroid) == abs(stack[-1]):
                # remove last item from stack
                stack.pop()
            # if current is greater than last item
            elif abs(current_asteroid) > abs(stack[-1]):
                # also remove and decrease i
                # i is decrease because we want the current asteroid to still current for the next check
                stack.pop()
                i -= 1
        i += 1

    return stack


print(asteroidCollision([5, 10, -5]))
