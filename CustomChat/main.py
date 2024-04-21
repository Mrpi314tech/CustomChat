def run(username):
    import CustomChat
    while True:
        inputvar=input(': ')
        if 'exit' in inputvar or 'goodbye' in inputvar:
            print('exiting')
            break
        print(CustomChat.get_response(inputvar,username))
    CustomChat.reset()
def reset(username):
    import os
    file1 = open(os.path.join(os.path.dirname(__file__), username+"_data"), "w")
    file1.write("''\n['']\n['']\n['']\n['']")
    file1.close()
def get_response(input_text,username):
    import CustomChat.app
    CustomChat.app.compute(input_text,username)
    import ast
    import os
    cwd=os.path.dirname(os.path.realpath(__file__))
    try:
        file1 = open(cwd+"/"+username+"_data", "r")
        dvar=file1.read()
        file1.close()
        dvar=dvar.split('\n')
        Name=dvar[0]
        jsaid=ast.literal_eval(dvar[1])
        data=ast.literal_eval(dvar[2])
        crsponce=ast.literal_eval(dvar[3])
        rsponce=ast.literal_eval(dvar[4])
    except FileNotFoundError:
        file1 = open(os.path.join(os.path.dirname(__file__), username+"_data"), "w")
        file1.write("''\n['']\n['']\n['']\n['']")
        file1.close()
    output_data=[rsponce[0],crsponce[0]]
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
    file1.write("Command_Line="+str(command)+"\nWeb_Scrape="+str(Web)+"\nEdit="+str(Edit)+"")
    file1.close()
