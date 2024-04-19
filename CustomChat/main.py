def run():
    import CustomChat.app
def get_response(input_text):
    import CustomChat.app
    CustomChat.app.compute(input_text)
    import CustomChat.ai_data as dvar
    output_data=[dvar.rsponce[0],dvar.crsponce[0]]
    return output_data
def change_name(name):
    import os
    file1 = open(os.path.join(os.path.dirname(__file__), "Name.py"), "w")
    file1.write(name)
    file1.close()
def set_config():
    import os
    import CustomChat.configuration as config
    command=input('Would you like the Command Line to be enabled? ')
    if 'yes' in command.lower() or 'true' in command.lower():
        command=True
    else:
        command=False
    Web=input('Would you like to enable web scraping? ')
    if 'yes' in Web.lower() or 'true' in Web.lower():
        Web=True
    else:
        Web=False
    Edit=input('Would you like to lock your edits? ')
    if 'yes' in Edit.lower() or 'false' in Edit.lower():
        Edit=False
    else:
        Edit=True
    file1 = open(os.path.join(os.path.dirname(__file__), "configuration.py"), "w")
    file1.write("Command_Line="+command+"\nWeb_Scrape="+Web+"\nEdit="+Edit+"")
    file1.close()