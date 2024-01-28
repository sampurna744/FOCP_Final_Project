import sys

def process_line(line):
    """
    Process a line by splitting it into parts and returning specific values.

    Parameters:
    line (str): The input line to be processed.

    Returns:
    tuple: If the line contains 3 parts, return a tuple containing the category type,
           entry time (as int), and exit time (as int). Otherwise, return None.
    """

    parts = line.split(",") # Splits the line into a list of parts using commas as separators
    if len(parts) == 3: # Checks if the line has three parts.
        try:
            cat_type, entry_time, exit_time = parts
            return cat_type, int(entry_time), int(exit_time) # returns a tuple with integer value.
        except ValueError:
            return None

def analyze_log(file_path):
    """
   Analyze_log:
   Analyzes the log file and prints a summary of cat activity.

   Args:
        file_path: The path to the log file to be analyzed.
   """
    with open(file_path, "r") as f:
        cat_visits = other_cats = total_time = 0 # Initializing variables for counting and storing data.
        durations = [] # Creates an empty list to store visit durations for later calculations.

        for line in f:  # Loops through each line in the file.
            data = process_line(line.strip()) # removes the white spacing form the line
            if data:
                cat_type, entry, exit = data  #Assign value to individual variable
                if cat_type == "OURS":        #checks if the cats type is ours
                    cat_visits += 1
                    total_time += exit - entry
                    durations.append(exit - entry) #add duration to the list of duration.
                else:
                    other_cats += 1

        hours, minutes = divmod(total_time, 60) # Converts time in minutes to hours and minutes.
        average_duration = sum(durations) // len(durations) if durations else 0 # Calculates the average visit duration.
        longest_visit = max(durations) if durations else 0 #calculates the longest duration.
        shortest_visit = min(durations) if durations else 0 #calculates the shortest duration.

        print("Log File Analysis")
        print("==================")
        print("Cat Visits:", cat_visits)
        print("Other Cats:", other_cats)
        print("Total Time in House:", hours , "Hours,", minutes , "Minutes")
        print("Average Visit Length:", average_duration, "Minutes")
        print("Longest Visit:", longest_visit, "Minutes")
        print("Shortest Visit:", shortest_visit, "Minutes")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cat_shelter.py <log_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]   #extract file from command line arguement
    analyze_log(file_path)    # Perform log file analysis using the provided file path
