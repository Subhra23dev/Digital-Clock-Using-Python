# 🕒 Digital Clock (Python Tkinter)

A simple **Digital Clock** application built using **Python** and **Tkinter**. The clock displays the current time and date in real-time with a clean graphical user interface.

## 📌 Features

- ⏰ Live digital clock
- 📅 Displays current date
- 🔄 Updates automatically every second
- 🎨 Simple and colorful GUI using Tkinter
- 💻 Lightweight and beginner-friendly project

## 🛠️ Technologies Used

- Python 3
- Tkinter (GUI)
- time module (`strftime`)

## 📂 Project Structure

```
Digital-Clock/
│── main.py
│── README.md
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Clone this repository:

```bash
git clone https://github.com/your-username/Digital-Clock.git
```

3. Navigate to the project folder:

```bash
cd Digital-Clock
```

4. Run the program:

```bash
python digital_clock.py
```

## 🖥️ Preview

The application displays:

- Current Time (Hours : Minutes : Seconds)
- AM/PM Indicator
- Current Date (DD-MM-YYYY)

Example:

```
08:35:41 PM
22-07-2026
```

## 📖 How It Works

- `strftime()` retrieves the current system time and date.
- The `after()` method updates the displayed time every **1000 milliseconds (1 second)**.
- Tkinter's `Label` widget displays the formatted time and date.

## 📚 Learning Objectives

This project helps beginners understand:

- Tkinter GUI development
- Functions in Python
- Event-driven programming
- Real-time updates using `after()`
- Date and time formatting with `strftime()`

## 🚀 Future Improvements

- 🌙 Dark Mode
- 🌍 Multiple Time Zones
- 📆 Day of the Week
- ⏲️ Stopwatch
- ⏰ Alarm Clock
- 🎨 Custom Themes

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

## 📄 License

This project is open-source and available under the **MIT License**.

---

### 👨‍💻 Author

**Subhradeep Das**

GitHub: https://github.com/Subhra23dev