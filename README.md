# SIMPLE  CALCULATOR

## Description
SRIKANTH CALCULATOR is a modern, feature-rich web-based calculator built using Flask for the backend and JavaScript for the frontend. It provides basic arithmetic operations, trigonometric functions, logarithmic calculations, and a history feature. The UI is designed with a sleek, animated background and draggable functionality for ease of use.

## Features
- Basic arithmetic operations: Addition, Subtraction, Multiplication, Division
- Advanced operations: Square root, Logarithm (log, ln), Percentage, Exponentiation
- Trigonometric functions: sin, cos, tan (degrees)
- Keyboard input support
- Draggable and resizable calculator UI
- Calculation history tracking
- Error handling for invalid expressions

## Controls
### Mouse:
- Click buttons to input numbers/operations

### Keyboard:
- Numbers (0-9) and operators (+, -, *, /)
- Special functions:
  - `s` → sin(
  - `c` → cos(
  - `t` → tan(
  - `q` → sqrt(
  - `l` → log(
  - `n` → ln(
- `Enter` = Calculate
- `Esc` = Clear
- `Backspace` = Delete last character

## Installation and Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Flask

### Steps to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/srikanth-calculator.git
   ```
2. Navigate to the project directory:
   ```sh
   cd srikanth-calculator
   ```
3. Install dependencies:
   ```sh
   pip install flask
   ```
4. Run the Flask server:
   ```sh
   python app.py
   ```
5. Open a browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
### `GET /`
- Loads the calculator UI.

### `POST /calculate`
- Accepts a mathematical expression as input and returns the evaluated result.
- **Request Format:**
  ```json
  {
    "expression": "sin(30) + log(10)"
  }
  ```
- **Response Format:**
  ```json
  {
    "result": "1.301"
  }
  ```

## Technologies Used
- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3 (with animations and gradients), Vanilla JavaScript
- **Math Operations:** Python math module

## Future Enhancements
- Add more scientific functions
- Implement dark/light mode toggle
- Improve error messages for better clarity

## Contributing
Contributions are welcome! If you find bugs or have feature requests, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Author
Developed by Srikanth.

