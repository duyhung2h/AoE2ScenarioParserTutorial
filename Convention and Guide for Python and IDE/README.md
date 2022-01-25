# Convention and Guide for Python and IDE:
These are short tutorials about convention and small tips of how you should write Python, which are also followed by most of other programming language, and PyCharm's useful functionalities you should know (which is also included in most IDE)

If you want to check more extensive tutorials about Python, visit [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp). This documents only covers the basics that you should know.

## Some general Python tips:

### 1. Identation
Code blocks are separated by indentation (this is similar to other programming language curly braces "{}"), that means after a statement, like `if ... else` or `for`. You need to separate your code within a statement by pressing `TAB`, or 4 `Spacebar` spaces. This is to indicate if your code is within the statement or not.
![image](https://user-images.githubusercontent.com/40296674/151033526-84e0d492-0a9e-45e1-8966-21cdf53352a2.png)

### 2. print()
Use the `print` function to quickly print out a string, an attribute value, lists, etc... to (almost) check everything's value:

```print(triggers[0].name)```. 

You can also use print for debugging purposes, such as to check if a code block got runned or not.

Remember, you cannot print out specific types, like `int`, but you can always convert them to type `str` by writing: `str(10)`
### 3. Class
A class is an entity, usually stored in another python file, and defined in the start by `class`. Within a class there are several attributes you can declare (inside a constructor subroutine, which is `def __init__` in Python, and you can reuse them later on for ease of use to write data. Class can also be contained inside a list.

Some attributes within a class can also have a default value, simply in the constructor declaration assign a value to it (like in this example below, `Effect` class will have 1 as its default value):

```
class Effect
  def __init__(self, effect_type, source_player=1):
    self.effect_type = effect_type
    self.source_player = source_player
    # ...
```

It's like a template that you can reuse infinite number of times, like how a Trigger class can have different attributes (taken inside AoE2ScenarioParser library):

```
class Trigger
    def __init__(self,
                 name: str,
                 description: str = "",
                 description_stid: int = -1,
                 display_as_objective: int = 0,
                 short_description: str = "",
                 short_description_stid: int = -1,
                 display_on_screen: int = 0,
                 description_order: int = 0,
                 enabled: int = 1,
                 looping: int = 0,
                 header: int = 0,
                 mute_objectives: int = 0,
                 conditions: List[Condition] = None,
                 condition_order: List[int] = None,
                 effects: List[Effect] = None,
                 effect_order: List[int] = None,
                 trigger_id: int = -1,
                 **kwargs
                 ):
```

Read more about classes in [W3School](https://www.w3schools.com/python/python_classes.asp)

### 4. Comments
In Python, you can use comment by adding `#` before a sentence.

Comments are for code-readability, and to summerize the functionality of your codes.

Be sure to comment often, so others (and future you!) to understand your code. Comments should be short and percise.

```
# This is a Character class
#
# A character can have different attributes, such as unitId, unitName (their true name displayed in the scenario)
# characterClass indicates which class a character is, which will affect on their gear restriction.
# There are 4 character classes at the moment: warrior, rogue, ranger and soulweaver.
# They can also have different panel areas, according to their position on the list.

class Character:
  # ...
```

Or you can comment lines of functioning code to prevent its execution, while keeping it's written text in your script.

Read more about comments in [W3School](https://www.w3schools.com/python/python_comments.asp)

## PyCharm useful functionalities you should know

### 1. Hold CTRL + click on items
You can hold `CTRL` and click on an attribute / class / function to go to its declaration, to find out about attributes and documents about them.

For example, to know all about attributes that contains inside the `ObjectAttribute` class, used in the "Modify Attribute" effect, hold `CTRL` and click on the class name:

![image](https://user-images.githubusercontent.com/40296674/151027885-4b79738b-dda7-4df5-bb87-3a9df59a5785.png)

### 2. Quick comment (CTRL + /)
You can comment a line of code, or a block of code quickly by selecting them,

Then hold `CTRL`, and press `/`.

![image](https://user-images.githubusercontent.com/40296674/151028180-2641477a-885f-4cca-bb4c-924238494cb4.png)

### 3. Quick format (CTRL + ALT + L)
If your script is messy with unnecessary white spaces or indentation, it could cause a dent on code-readability, or sometimes it could cause some unnecessary error.

Remember to reformat your code script often!

### 4. Suggestion box
In PyCharm, sometimes suggestion box will show while you type so you can quickly finish writing an attribute's name, or a class's name:

![image](https://user-images.githubusercontent.com/40296674/151034118-88bb414e-8053-466b-b632-26407513b959.png)

Or if you want to force PyCharm to display more relevant suggestion, or sometimes autofill attribute or function names if there's only one suggestion, Hold `CTRL` and press `Space`.

![image](https://user-images.githubusercontent.com/40296674/151034604-3b0a3c65-1513-41fc-adc8-7e568cb2085f.png)



