from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

HTML_TEMPLATE = """
!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Calculator</title>
    <style>
        /* Background with animated gradient and calculator name */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            height: 100vh;
            overflow: hidden;
            background: linear-gradient(135deg, #2c3e50, #4ca1af);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            position: relative;
        }
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        /* Calculator name in the background */
       body::before {
    content: ' SRIKANTH CALCULATOR ';
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 6rem;
    font-weight: bold;
    font-family: 'Arial', sans-serif;
    color: transparent; /* Make text color transparent */
    background: linear-gradient(45deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee, #84fab0); /* Gradient background */
    -webkit-background-clip: text; /* Clip background to text */
    background-clip: text;
    text-transform: uppercase;
    letter-spacing: 5px;
    text-shadow: 2px 2px 10px rgba(255, 255, 255, 0.5);
    pointer-events: none;
    z-index: -1;
    white-space: nowrap;
    animation: glow 5s infinite alternate; /* Add glowing animation */
}

@keyframes glow {
    0% {
        opacity: 0.8;
        filter: brightness(1);
    }
    50% {
        opacity: 1;
        filter: brightness(1.5);
    }
    100% {
        opacity: 0.8;
        filter: brightness(1);
    }
}

        /* Draggable Calculator Box */
        .calculator {
            background-color: rgba(0, 0, 0, 0.85);
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.3);
            color: white;
            width: 300px; /* Adjusted width */
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            cursor: move;
            user-select: none;
        }
        /* Display Screen */
        .display {
            width: 100%;
            height: 50px; /* Reduced height */
            background-color: #222;
            color: #fff;
            text-align: right;
            padding: 10px;
            font-size: 24px;
            border: none;
            border-radius: 10px;
            margin-bottom: 10px; /* Reduced margin */
            box-shadow: inset 0px 0px 10px rgba(255, 255, 255, 0.1);
            cursor: text; /* Allow cursor movement */
            caret-color: white; /* Make cursor visible */
        }
        /* Grid Buttons */
        .buttons {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px; /* Reduced gap */
        }
        /* Buttons */
        .button {
            background-color: #444;
            color: #fff;
            border: none;
            padding: 15px; /* Reduced padding */
            font-size: 16px; /* Reduced font size */
            border-radius: 10px;
            cursor: pointer;
            transition: 0.2s;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        /* Hover Effects */
        .button:hover {
            background-color: #555;
            transform: translateY(-2px);
        }
        /* Operator Buttons */
        .button.operator {
            background-color: #ff9500;
        }
        .button.operator:hover {
            background-color: #ffaa33;
        }
        /* Clear Button */
        .button.clear {
            background-color: #ff3b30;
        }
        .button.clear:hover {
            background-color: #ff5c50;
        }
        /* Back Button */
        .button.back {
            background-color: #0057e7;
        }
        .button.back:hover {
            background-color: #007bff;
        }
        /* History Section */
        .history {
            margin-top: 15px; /* Reduced margin */
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
            max-height: 100px; /* Reduced height */
            overflow-y: auto;
            font-size: 14px; /* Reduced font size */
        }
        .history h3 {
            margin: 0 0 8px 0; /* Reduced margin */
            font-size: 14px; /* Reduced font size */
        }
        .history div {
            font-size: 12px; /* Reduced font size */
            margin-bottom: 4px; /* Reduced margin */
        }
    </style>
</head>
<body>
    <div class="calculator" id="calculator">
        <input type="text" id="display" class="display" oninput="moveCursor()">
        <div class="buttons">
            <button class="button operator" onclick="appendToDisplay('(')">(</button>
            <button class="button operator" onclick="appendToDisplay(')')">)</button>
            <button class="button back" onclick="backspace()">←</button>
            <button class="button clear" onclick="clearDisplay()">C</button>
            <button class="button operator" onclick="appendToDisplay('/')">/</button>
            <button class="button operator" onclick="appendToDisplay('*')">*</button>
            <button class="button operator" onclick="appendToDisplay('-')">-</button>
            <button class="button operator" onclick="appendToDisplay('+')">+</button>
            <button class="button operator" onclick="appendToDisplay('sqrt(')">√</button>
            <button class="button operator" onclick="appendToDisplay('log(')">log</button>
            <button class="button operator" onclick="appendToDisplay('ln(')">ln</button>
            <button class="button operator" onclick="appendToDisplay('%')">%</button>
            <button class="button operator" onclick="appendToDisplay('2^')">2ⁿ</button>
            <button class="button operator" onclick="appendToDisplay('10^')">10ˣ</button>
            <button class="button operator" onclick="appendToDisplay('sin(')">sin</button>
            <button class="button operator" onclick="appendToDisplay('cos(')">cos</button>
            <button class="button operator" onclick="appendToDisplay('tan(')">tan</button>
            <button class="button" onclick="appendToDisplay('1')">1</button>
            <button class="button" onclick="appendToDisplay('2')">2</button>
            <button class="button" onclick="appendToDisplay('3')">3</button>
            <button class="button" onclick="appendToDisplay('4')">4</button>
            <button class="button" onclick="appendToDisplay('5')">5</button>
            <button class="button" onclick="appendToDisplay('6')">6</button>
            <button class="button" onclick="appendToDisplay('7')">7</button>
            <button class="button" onclick="appendToDisplay('8')">8</button>
            <button class="button" onclick="appendToDisplay('9')">9</button>
            <button class="button" onclick="appendToDisplay('0')">0</button>
            <button class="button" onclick="appendToDisplay('.')">.</button>
            <button class="button operator" onclick="calculateResult()">=</button>
        </div>
        <div class="history">
            <h3>History</h3>
            <div id="history"></div>
        </div>
    </div>

    <script>
        let history = []; // Array to store calculation history

        function appendToDisplay(value) {
            const display = document.getElementById('display');
            display.value += value;
        }

        function clearDisplay() {
            document.getElementById('display').value = '';
        }

        function backspace() {
            let current = document.getElementById('display').value;
            document.getElementById('display').value = current.slice(0, -1);
        }

        function calculateResult() {
            const expression = document.getElementById('display').value;
            let result;

            try {
                // Replace functions with their JavaScript equivalents
                const modifiedExpression = expression
                    .replace(/sin\(/g, 'Math.sin(Math.PI/180 *')
                    .replace(/cos\(/g, 'Math.cos(Math.PI/180 *')
                    .replace(/tan\(/g, 'Math.tan(Math.PI/180 *')
                    .replace(/sqrt\(/g, 'Math.sqrt(')
                    .replace(/log\(/g, 'Math.log10(')
                    .replace(/ln\(/g, 'Math.log(')
                    .replace(/(\d+)\^(\d+)/g, 'Math.pow($1,$2)'); // Fixing exponentiation issue

                // Evaluate the expression
                result = eval(modifiedExpression);

                // Handle edge cases
                if (expression.includes('tan(90)')) {
                    result = Infinity;
                }
                if (expression.includes('/0')) {
                    result = 'Error: Division by zero';
                }

                // Add to history
                history.push(`${expression} = ${result}`);
                updateHistory();
            } catch (error) {
                result = 'Error: Invalid expression';
            }

            document.getElementById('display').value = result;
        }

        function updateHistory() {
            const historyElement = document.getElementById('history');
            historyElement.innerHTML = history.map(entry => `<div>${entry}</div>`).join('');
        }

        // Draggable Calculator
        const calculator = document.getElementById('calculator');
        let isDragging = false;
        let offsetX, offsetY;

        calculator.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.clientX - calculator.getBoundingClientRect().left;
            offsetY = e.clientY - calculator.getBoundingClientRect().top;
        });

        document.addEventListener('mousemove', (e) => {
            if (isDragging) {
                calculator.style.left = `${e.clientX - offsetX}px`;
                calculator.style.top = `${e.clientY - offsetY}px`;
            }
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
        });

        // Cursor movement in display
        function moveCursor() {
            const display = document.getElementById('display');
            display.focus(); // Ensure the display is focused
        }

        // Keyboard input handling
        document.addEventListener('keydown', function(event) {
            const key = event.key;
            const display = document.getElementById('display');

            if (key >= '0' && key <= '9') {
                appendToDisplay(key);
            } else if (key === '.') {
                appendToDisplay('.');
            } else if (key === '+' || key === '-' || key === '*' || key === '/') {
                appendToDisplay(key);
            } else if (key === 'Enter') {
                calculateResult();
            } else if (key === 'Backspace') {
                backspace();
            } else if (key === 'Escape') {
                clearDisplay();
            } else if (key === '%') {
                appendToDisplay('%');
            } else if (key === '^') {
                appendToDisplay('^');
            } else if (key === '(' || key === ')') {
                appendToDisplay(key);
            } else if (key === 's') {
                appendToDisplay('sin(');
            } else if (key === 'c') {
                appendToDisplay('cos(');
            } else if (key === 't') {
                appendToDisplay('tan(');
            } else if (key === 'q') {
                appendToDisplay('sqrt(');
            } else if (key === 'l') {
                appendToDisplay('log(');
            } else if (key === 'n') {
                appendToDisplay('ln(');
            } else if (key === '2') {
                appendToDisplay('2^');
            } else if (key === '0') {
                appendToDisplay('10^');
            }
        });
    </script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        result = str(eval(expression, {"__builtins__": {}}, {
            "math": math, "pow": math.pow, "sqrt": math.sqrt, "log": math.log,
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "remainder": math.remainder
        }))
    except Exception:
        result = "Error"
    return result

if __name__ == '__main__':
    app.run(debug=True)