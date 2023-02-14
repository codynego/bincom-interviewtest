from collections import Counter

# Define the colors for each day
Monday_color = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
Tuesday_color = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
Wednesday_color = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
Thursday_color = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
Friday_color = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

# Combine all colors into a single list
colors = Monday_color + Tuesday_color + Wednesday_color + Thursday_color + Friday_color

def most_common_color(colors):
    # Find the most common color
    most_common_color = Counter(colors).most_common(1)[0][0]
    return most_common_color

# Find the median color
def median_color(colors=colors):
    median_index = len(colors) // 2
    colors = sorted(colors)
    median_color = colors[median_index]
    return median_color

# Find the mean color
def mean_color(colors):
    mean_color_index = len(colors) / len(set(colors))
    mean_color = colors[int(mean_color_index)]
    return mean_color


# Find the variance of colors
def colors_frequency(colors=colors):
    colors_frequency = Counter(colors)
    colors_frequency_mean = sum(colors_frequency.values()) / len(colors_frequency)
    variance = sum((frequency - colors_frequency_mean) ** 2 for frequency in colors_frequency.values()) / len(colors_frequency)
    return variance

# Find the probability that a color chosen at random is red
probability_red = colors.count('BLUE') / len(colors)


# Print the results
print("Most common color:", most_common_color(colors))
print("Median color:", median_color())
print("Mean color:", mean_color(colors))
print("Variance of colors:", colors_frequency(colors))
print("Probability that a color chosen at random is red:", probability_red)
