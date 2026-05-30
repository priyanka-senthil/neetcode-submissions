class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair each car's position with its speed
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        # Process cars from closest to target to farthest
        for p, s in sorted(pair)[::-1]:
            # Time taken for this car to reach the target
            stack.append((target - p) / s)

            # If the car behind reaches the target earlier or at the same time
            # as the car in front, it catches up and becomes part of the same fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # Each remaining time in stack represents one fleet
        return len(stack)