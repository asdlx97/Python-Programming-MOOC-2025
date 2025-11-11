# Python Programming MOOC 2025 Solutions
This repository contains my personal solutions to the exercises from the [**Python Programming MOOC 2025**](https://programming-25.mooc.fi/) by the University of Helsinki.  
The original course materials are available under the [Creative Commons BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/deed).
---
## About the Course
The **Python Programming MOOC** is a free online course designed to teach Python from the ground up — from basic syntax and data structures to more advanced topics like object-oriented programming and file handling.  
The course repository can be found here: [rage/programming-25 on GitHub](https://github.com/rage/programming-25)
---
## About This Repository
This repo includes **my personal solutions** to the programming exercises provided in the course, which are (partly) overlapping with the suggested solutions included in the course material and this repo.  
These solutions are shared **for learning and discussion purposes only** — please do **not** copy them directly if you're taking the course. Try solving the tasks yourself first!  
---
## License
All original course materials belong to the University of Helsinki and are licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed).  
My own code and solutions in this repository are shared under the same license to ensure compatibility:
> **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**
---
## Learning Goals
- Learn basic Python syntax
- Strengthen my Python fundamentals  
- Practice clean, readable, and efficient code  
- Develop problem-solving skills through consistent challenge  
---
## How the Course Works

### Test My Code (TMC) Plugin
The course uses the **TestMyCode (TMC)** extension for VS Code to deliver and evaluate exercises automatically. Here's how it works:

1. **Download exercises** - Use the TMC extension to download exercise sets directly into your VS Code workspace
2. **Write your solution** - Each exercise comes with a template file where you write your code
3. **Run tests locally** - Before submitting, you can run tests locally to check if your solution passes all test cases. The TMC plugin runs automated unit tests that verify your code's correctness
4. **Submit your solution** - Once all local tests pass, you can submit your solution to the TMC server
5. **Get instant feedback** - The server runs the same tests and provides immediate feedback on whether you passed or failed
6. **View suggested solutions** - After passing an exercise, you can view the course's suggested solution to compare approaches

The automated testing system checks not just if your code produces the right output, but also whether it handles edge cases, follows the specified requirements, and works correctly with various inputs. This immediate feedback loop is invaluable for learning!

---
## Notes
If you're also learning Python, feel free to browse around!  

### On the Use of LLMs
I'm proud to say that I haven't reached out to LLMs to solve the exercises and have solely relied on the provided concepts and syntax within the course materials up until that point in the course. I wanted to avoid using any LLM assistance in order to really get a grasp of the material.

However, I did use an LLM to compare my solution to the suggested solution that I got to see after submitting mine and passing each exercise. This helped me understand alternative approaches and identify areas for improvement.

I'm planning to eventually use LLMs after completing the course to improve my codebase — but only once I fully understand what's going on under the hood.

### Tips for Disabling AI Assistance in VS Code
If you want to learn without AI suggestions (which I highly recommend while learning fundamentals), here's how to disable them:

**Disable GitHub Copilot:**
- Open Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
- Type "GitHub Copilot: Disable"
- Or add to your `settings.json`:
```json
  "github.copilot.enable": {
      "*": false
  }
```

**Disable Inline Suggestions:**
- Add to your `settings.json`:
```json
  "editor.inlineSuggest.enabled": false
```

**Disable IntelliSense Auto-complete (if desired):**
- Add to your `settings.json`:
```json
  "editor.quickSuggestions": {
      "other": false,
      "comments": false,
      "strings": false
  }
```

You can still manually trigger suggestions with `Ctrl+Space` when you need them!

---
**Happy coding!**  
– Arno
