# May 2025 Temperature Tracker
 
A menu-driven Python application that reads, analyzes, and summarizes daily temperature data recorded by the National Weather Service for the Dulles/Sterling, VA area during May 2025.
 
---
 
## Features
 
- Reads tab-delimited temperature data from a `.txt` file using Python's `csv` module
- Calculates the **average temperature** for each day
- Finds the **lowest recorded temperature** and the date it occurred
- Finds the **highest recorded temperature** and the date it occurred
- Calculates the **average of all daily average temperatures**
- Saves descriptive statistics to a structured **JSON file**
- Interactive **menu-driven CLI** interface
---
 
## Project Structure
 
```
├── may_2025_temps.py       # Main application script
├── may2025temps.txt        # Input data file (tab-delimited)
└── temps_stats.json        # Output file generated on save
```
 
---
 
## 🖥️ Usage
 
When launched, the program automatically reads and processes the data file, then presents an interactive menu:
 
```
--------------------------------------------------------------------
Please choose from the following menu:
Enter 1 to print the May 2025 temps_list list.
Enter 2 to find lowest temperature and its date.
Enter 3 to find highest temperature and its date.
Enter 4 to display average of average daily temperature.
Enter 5 to save the statistics.
Enter 99 to Quit.
--------------------------------------------------------------------
```
 
### Sample Output
 
```
Dates          Low Temp     High Temp     Average Temp
05/01/2025           48            72            60.0
05/02/2025           52            78            65.0
...
 
Lowest Low                              Date
48                                  05/01/2025
 
Highest High                            Date
91                                  05/28/2025
 
Average of Average Temps
70.3
```
 
---
 
## 💾 Output — `temps_stats.json`
 
Selecting option 5 saves the computed statistics to a JSON file:
 
```json
{
    "Lowest Low": 48,
    "Lowest Low Date": "05/01/2025",
    "Highest High": 91,
    "Highest High Date": "05/28/2025",
    "Average of Average Temps": 70.3
}
```
 
---
 
## 🛡️ Error Handling
 
The application handles the following exceptions gracefully across all functions:
 
| Exception | Where It's Handled |
|---|---|
| `FileNotFoundError` | File reading |
| `PermissionError` | File reading & saving |
| `IndexError` | Data conversion & display |
| `ZeroDivisionError` | Average calculation |
| `ValueError` | Menu input validation |
| `OSError` | JSON file saving |
| `Exception` | All functions (broad fallback) |
 
---
 
## 🛠️ Built With
 
- **Python 3** — Core language
- **csv** — Parsing tab-delimited input data
- **json** — Serializing statistics to file
---
