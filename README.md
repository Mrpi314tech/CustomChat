# CustomChat

CustomChat is an easily customizable AI chatbot powered by Jimbot AI. Whether you're running it on an online compiler or locally, CustomChat empowers you to tailor it to your specific needs.

## Installation

To install CustomChat, follow these steps:

1. Download the package with pip:
   <pre><code>pip install CustomChat</code></pre>
   
2. Test the code with python:
   <pre><code>import CustomChat
   CustomChat.run(username)</code></pre>

   This will start CustomChat and you can begin customizing it for your needs.

## How to Use

CustomChat is designed for seamless interaction and easy customization. Follow these simple steps to maximize your experience:

1. **Initializing CustomChat:**
   - After installation, import CustomChat into your Python environment and start the chatbot by running:
     ```python
     import CustomChat
     CustomChat.run(username)
     ```
   This command initializes CustomChat, allowing you to interact with it. Username can be any string, it just has to identify who is using the bot.

2. **Getting Responses:**
   - To receive responses from CustomChat based on your inputs, use the following function:
     ```python
     responses = CustomChat.get_response('your input here','your username')
     ```
   This function returns a list containing the main response as the first element and the secondary response as the second element. The username variable can be anything from a name to an ip address.

3. **Resetting Data:**
   - If needed, you can reset the chatbot's data by running:
     ```python
     CustomChat.reset(username)
     ```
   This clears the information stored for that user.

### Requirements

CustomChat requires the following Python libraries:
- `bs4` (Beautiful Soup): For web scraping capabilities.
- `requests` For making HTTP requests.

These are already in the "Dependencies" folder.

## Customization

Tailoring CustomChat to your requirements is a breeze. You can personalize the chatbot's name and incorporate keywords to suit your preferences. Simply type the code ```CustomChat.change_name('Your Name Here')```  to modify the name. Additionally, to integrate your own keywords, initiate CustomChat and input "edit" to follow the prompts. CustomChat can only be edited from the terminal.

## Restrictions

CustomChat offers flexibility in managing permissions. Should you wish to impose restrictions, such as prohibiting users from executing commands, you can effortlessly adjust settings in the configuration file. By running the code ```CustomChat.set_config()``` you can easily adjust the permissions to what you want.

## Capabilities

CustomChat boasts an array of functionalities to enhance user experience:

- **Website and File Access:** Configure CustomChat to open websites and files as per your requirements.
- **Command Execution:** Enable CustomChat to execute commands, providing seamless interaction.
- **Keyword-based Responses:** Customize CustomChat to deliver specific responses based on designated keywords.

Moreover, CustomChat's capabilities extend to:

- **Web Scraping:** Leveraging web scraping capabilities, CustomChat can retrieve information from various online sources.
- **General Knowledge:** Accessing Google through web scraping, CustomChat can provide answers to general inquiries.
- **Command Line Integration:** With access to the command line, CustomChat enables users to execute commands effortlessly by typing "run" followed by the desired command.

For further information about the AI powering CustomChat, visit [Jimbot AI](https://jb.mrpi314.com/ai).

Enhance your chatbot experience with CustomChat's versatility and adaptability.
