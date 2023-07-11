import tkinter as tk
import time
import random


class AlgorithmVisualizer:
    def __init__(self, window):
        self.window = window
        self.window.title("Algorithm Visualizer")

        # Create buttons for user interaction
        self.start_button = tk.Button(
            self.window, text="Start", command=self.start_visualization)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button = tk.Button(
            self.window, text="Stop", command=self.stop_visualization, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the canvas for drawing the visualization
        self.canvas = tk.Canvas(self.window, width=800, height=400)
        self.canvas.pack()

        self.rectangles = []
        self.is_visualizing = False

    def generate_rectangles(self):
        self.rectangles = []
        for i in range(20):
            height = random.randint(50, 300)
            x = i * 40 + 50
            y = 400 - height
            rectangle = self.canvas.create_rectangle(
                x, y, x + 30, 400, fill="blue")
            self.rectangles.append(rectangle)

    def start_visualization(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_visualizing = True
        self.generate_rectangles()
        self.bubble_sort()
        self.selection_sort()
        self.insertion_sort()
        self.merge_sort(0, len(self.rectangles) - 1)
        self.quick_sort(0, len(self.rectangles) - 1)
        self.shell_sort()
        self.linear_search(100)
        self.binary_search_recursive(100, 0, len(self.rectangles) - 1)
        self.jump_search(100)
        self.interpolation_search(100)
        self.exponential_search(100)
        self.stop_visualization()

    def stop_visualization(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_visualizing = False

    def bubble_sort(self):
        n = len(self.rectangles)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if not self.is_visualizing:
                    return
                self.canvas.itemconfig(self.rectangles[j], fill="red")
                self.canvas.itemconfig(self.rectangles[j + 1], fill="red")
                self.window.update()
                time.sleep(0.5)
                height1 = self.canvas.coords(self.rectangles[j])[
                    3] - self.canvas.coords(self.rectangles[j])[1]
                height2 = self.canvas.coords(
                    self.rectangles[j + 1])[3] - self.canvas.coords(self.rectangles[j + 1])[1]
                if height1 > height2:
                    self.canvas.move(self.rectangles[j], 40, 0)
                    self.canvas.move(self.rectangles[j + 1], -40, 0)
                    self.rectangles[j], self.rectangles[j +
                                                        1] = self.rectangles[j + 1], self.rectangles[j]
                self.canvas.itemconfig(self.rectangles[j], fill="blue")
                self.canvas.itemconfig(self.rectangles[j + 1], fill="blue")
                self.window.update()
                time.sleep(0.5)

    def selection_sort(self):
        n = len(self.rectangles)
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                if not self.is_visualizing:
                    return
                self.canvas.itemconfig(self.rectangles[j], fill="red")
                self.window.update()
                time.sleep(0.5)
                height1 = self.canvas.coords(self.rectangles[j])[
                    3] - self.canvas.coords(self.rectangles[j])[1]
                height2 = self.canvas.coords(self.rectangles[min_index])[
                    3] - self.canvas.coords(self.rectangles[min_index])[1]
                if height1 < height2:
                    min_index = j
                self.canvas.itemconfig(self.rectangles[j], fill="blue")
                self.window.update()
                time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[i], fill="red")
            self.canvas.itemconfig(self.rectangles[min_index], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.move(self.rectangles[i], min_index * 40 - i * 40, 0)
            self.canvas.move(
                self.rectangles[min_index], i * 40 - min_index * 40, 0)
            self.rectangles[i], self.rectangles[min_index] = self.rectangles[min_index], self.rectangles[i]
            self.canvas.itemconfig(self.rectangles[i], fill="blue")
            self.canvas.itemconfig(self.rectangles[min_index], fill="blue")
            self.window.update()
            time.sleep(0.5)

    def insertion_sort(self):
        n = len(self.rectangles)
        for i in range(1, n):
            key = self.canvas.coords(self.rectangles[i])[
                3] - self.canvas.coords(self.rectangles[i])[1]
            j = i - 1
            while j >= 0 and (self.canvas.coords(self.rectangles[j])[3] - self.canvas.coords(self.rectangles[j])[1]) > key:
                if not self.is_visualizing:
                    return
                self.canvas.itemconfig(self.rectangles[j], fill="red")
                self.window.update()
                time.sleep(0.5)
                self.canvas.move(self.rectangles[j], 40, 0)
                self.rectangles[j + 1] = self.rectangles[j]
                self.canvas.itemconfig(self.rectangles[j], fill="blue")
                j -= 1
            self.canvas.move(self.rectangles[j + 1], 40 * (i - (j + 1)), 0)
            self.rectangles[j + 1] = self.rectangles[i]
            self.window.update()
            time.sleep(0.5)
        for i in range(n):
            self.canvas.itemconfig(self.rectangles[i], fill="blue")
            self.window.update()
            time.sleep(0.5)

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        left = self.rectangles[low:mid + 1]
        right = self.rectangles[mid + 1:high + 1]
        i = j = 0
        k = low
        while i < len(left) and j < len(right):
            if not self.is_visualizing:
                return
            height1 = self.canvas.coords(
                left[i])[3] - self.canvas.coords(left[i])[1]
            height2 = self.canvas.coords(
                right[j])[3] - self.canvas.coords(right[j])[1]
            if height1 < height2:
                self.canvas.move(left[i], (k - low) *
                                 40 - self.canvas.coords(left[i])[0], 0)
                self.rectangles[k] = left[i]
                i += 1
            else:
                self.canvas.move(right[j], (k - low) *
                                 40 - self.canvas.coords(right[j])[0], 0)
                self.rectangles[k] = right[j]
                j += 1
            self.canvas.itemconfig(self.rectangles[k], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[k], fill="blue")
            self.window.update()
            time.sleep(0.5)
            k += 1

        while i < len(left):
            if not self.is_visualizing:
                return
            self.canvas.move(left[i], (k - low) * 40 -
                             self.canvas.coords(left[i])[0], 0)
            self.rectangles[k] = left[i]
            self.canvas.itemconfig(self.rectangles[k], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[k], fill="blue")
            self.window.update()
            time.sleep(0.5)
            i += 1
            k += 1

        while j < len(right):
            if not self.is_visualizing:
                return
            self.canvas.move(right[j], (k - low) * 40 -
                             self.canvas.coords(right[j])[0], 0)
            self.rectangles[k] = right[j]
            self.canvas.itemconfig(self.rectangles[k], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[k], fill="blue")
            self.window.update()
            time.sleep(0.5)
            j += 1
            k += 1

    def quick_sort(self, low, high):
        if low < high:
            pivot_index = self.partition(low, high)
            self.quick_sort(low, pivot_index - 1)
            self.quick_sort(pivot_index + 1, high)

    def partition(self, low, high):
        pivot = self.canvas.coords(self.rectangles[high])[
            3] - self.canvas.coords(self.rectangles[high])[1]
        i = low - 1
        for j in range(low, high):
            if not self.is_visualizing:
                return
            if (self.canvas.coords(self.rectangles[j])[3] - self.canvas.coords(self.rectangles[j])[1]) < pivot:
                i += 1
                self.canvas.move(
                    self.rectangles[i], (j - i) * 40 - self.canvas.coords(self.rectangles[i])[0], 0)
                self.canvas.move(
                    self.rectangles[j], (i - j) * 40 - self.canvas.coords(self.rectangles[j])[0], 0)
                self.rectangles[i], self.rectangles[j] = self.rectangles[j], self.rectangles[i]
                self.canvas.itemconfig(self.rectangles[i], fill="red")
                self.canvas.itemconfig(self.rectangles[j], fill="red")
                self.window.update()
                time.sleep(0.5)
                self.canvas.itemconfig(self.rectangles[i], fill="blue")
                self.canvas.itemconfig(self.rectangles[j], fill="blue")
                self.window.update()
                time.sleep(0.5)
        self.canvas.move(self.rectangles[i + 1], (high - (i + 1))
                         * 40 - self.canvas.coords(self.rectangles[i + 1])[0], 0)
        self.canvas.move(self.rectangles[high], ((
            i + 1) - high) * 40 - self.canvas.coords(self.rectangles[high])[0], 0)
        self.rectangles[i +
                        1], self.rectangles[high] = self.rectangles[high], self.rectangles[i + 1]
        self.canvas.itemconfig(self.rectangles[i + 1], fill="red")
        self.canvas.itemconfig(self.rectangles[high], fill="red")
        self.window.update()
        time.sleep(0.5)
        self.canvas.itemconfig(self.rectangles[i + 1], fill="blue")
        self.canvas.itemconfig(self.rectangles[high], fill="blue")
        self.window.update()
        time.sleep(0.5)
        return i + 1

    def shell_sort(self):
        n = len(self.rectangles)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.canvas.coords(self.rectangles[i])[
                    3] - self.canvas.coords(self.rectangles[i])[1]
                j = i
                while j >= gap and (self.canvas.coords(self.rectangles[j - gap])[3] - self.canvas.coords(self.rectangles[j - gap])[1]) > temp:
                    if not self.is_visualizing:
                        return
                    self.canvas.itemconfig(self.rectangles[j], fill="red")
                    self.window.update()
                    time.sleep(0.5)
                    self.canvas.move(self.rectangles[j - gap], 40, 0)
                    self.rectangles[j] = self.rectangles[j - gap]
                    self.canvas.itemconfig(self.rectangles[j], fill="blue")
                    self.window.update()
                    time.sleep(0.5)
                    j -= gap
                self.canvas.move(self.rectangles[j], 40 * (i - j), 0)
                self.rectangles[j] = i
                self.window.update()
                time.sleep(0.5)
            gap //= 2

    def binary_search(self, target):
        low = 0
        high = len(self.rectangles) - 1
        while low <= high:
            if not self.is_visualizing:
                return
            mid = (low + high) // 2
            mid_value = self.canvas.coords(self.rectangles[mid])[
                3] - self.canvas.coords(self.rectangles[mid])[1]
            if mid_value == target:
                self.canvas.itemconfig(self.rectangles[mid], fill="green")
                self.window.update()
                return
            elif mid_value < target:
                self.canvas.itemconfig(self.rectangles[mid], fill="red")
                low = mid + 1
            else:
                self.canvas.itemconfig(self.rectangles[mid], fill="red")
                high = mid - 1
            self.window.update()
            time.sleep(0.5)

    def linear_search(self, target):
        for i in range(len(self.rectangles)):
            if not self.is_visualizing:
                return
            height = self.canvas.coords(self.rectangles[i])[
                3] - self.canvas.coords(self.rectangles[i])[1]
            if height == target:
                self.canvas.itemconfig(self.rectangles[i], fill="green")
                self.window.update()
                return
            self.canvas.itemconfig(self.rectangles[i], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[i], fill="blue")
            self.window.update()
            time.sleep(0.5)

    def binary_search_recursive(self, target, low, high):
        if low <= high:
            mid = (low + high) // 2
            mid_value = self.canvas.coords(self.rectangles[mid])[
                3] - self.canvas.coords(self.rectangles[mid])[1]
            if mid_value == target:
                self.canvas.itemconfig(self.rectangles[mid], fill="green")
                self.window.update()
                return
            elif mid_value < target:
                return self.binary_search_recursive(target, mid + 1, high)
            else:
                return self.binary_search_recursive(target, low, mid - 1)
        return

    def jump_search(self, target):
        n = len(self.rectangles)
        step = int(n ** 0.5)
        prev = 0
        while prev < n:
            if not self.is_visualizing:
                return
            height = self.canvas.coords(self.rectangles[prev])[
                3] - self.canvas.coords(self.rectangles[prev])[1]
            if height == target:
                self.canvas.itemconfig(self.rectangles[prev], fill="green")
                self.window.update()
                return
            elif height < target:
                prev += step
                if prev >= n:
                    prev = n - 1
            else:
                break
            self.canvas.itemconfig(self.rectangles[prev], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[prev], fill="blue")
            self.window.update()
            time.sleep(0.5)
        for i in range(prev, -1, -1):
            if not self.is_visualizing:
                return
            height = self.canvas.coords(self.rectangles[i])[
                3] - self.canvas.coords(self.rectangles[i])[1]
            if height == target:
                self.canvas.itemconfig(self.rectangles[i], fill="green")
                self.window.update()
                return
            self.canvas.itemconfig(self.rectangles[i], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[i], fill="blue")
            self.window.update()
            time.sleep(0.5)

    def interpolation_search(self, target):
        low = 0
        high = len(self.rectangles) - 1
        while low <= high:
            if not self.is_visualizing:
                return
            low_value = self.canvas.coords(self.rectangles[low])[
                3] - self.canvas.coords(self.rectangles[low])[1]
            high_value = self.canvas.coords(self.rectangles[high])[
                3] - self.canvas.coords(self.rectangles[high])[1]
            if low_value == high_value:
                if low_value == target:
                    self.canvas.itemconfig(self.rectangles[low], fill="green")
                    self.window.update()
                    return
                else:
                    self.canvas.itemconfig(self.rectangles[low], fill="red")
                    self.window.update()
                    time.sleep(0.5)
                    self.canvas.itemconfig(self.rectangles[low], fill="blue")
                    self.window.update()
                    time.sleep(0.5)
                    low += 1
                    high -= 1
            else:
                pos = int(low + ((target - low_value) *
                          (high - low)) / (high_value - low_value))
                if pos < low or pos > high:
                    break
                pos_value = self.canvas.coords(self.rectangles[pos])[
                    3] - self.canvas.coords(self.rectangles[pos])[1]
                if pos_value == target:
                    self.canvas.itemconfig(self.rectangles[pos], fill="green")
                    self.window.update()
                    return
                elif pos_value < target:
                    low = pos + 1
                else:
                    high = pos - 1
                self.canvas.itemconfig(self.rectangles[pos], fill="red")
                self.window.update()
                time.sleep(0.5)
                self.canvas.itemconfig(self.rectangles[pos], fill="blue")
                self.window.update()
                time.sleep(0.5)

    def exponential_search(self, target):
        n = len(self.rectangles)
        if self.canvas.coords(self.rectangles[0])[3] - self.canvas.coords(self.rectangles[0])[1] == target:
            self.canvas.itemconfig(self.rectangles[0], fill="green")
            self.window.update()
            return
        i = 1
        while i < n and (self.canvas.coords(self.rectangles[i])[3] - self.canvas.coords(self.rectangles[i])[1]) <= target:
            if not self.is_visualizing:
                return
            i *= 2
        low = i // 2
        high = min(i, n - 1)
        while low <= high:
            if not self.is_visualizing:
                return
            mid = (low + high) // 2
            mid_value = self.canvas.coords(self.rectangles[mid])[
                3] - self.canvas.coords(self.rectangles[mid])[1]
            if mid_value == target:
                self.canvas.itemconfig(self.rectangles[mid], fill="green")
                self.window.update()
                return
            elif mid_value < target:
                low = mid + 1
            else:
                high = mid - 1
            self.canvas.itemconfig(self.rectangles[mid], fill="red")
            self.window.update()
            time.sleep(0.5)
            self.canvas.itemconfig(self.rectangles[mid], fill="blue")
            self.window.update()
            time.sleep(0.5)

    # ... Existing methods omitted for brevity ...


# Create the Tkinter window
window = tk.Tk()

# Create the AlgorithmVisualizer instance
visualizer = AlgorithmVisualizer(window)

# Start the Tkinter event loop
window.mainloop()
