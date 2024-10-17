import traceback
import keyword

def load_settings(global_dict):

    def is_identifier_valid(identifier):
        return identifier.isidentifier() and identifier not in keyword.kwlist

    def is_user_allocated(identifier):
        return identifier.isupper() and is_identifier_valid(identifier)

    try: 
        with open("serve.settings", 'r') as file:
            for index, line in enumerate(file):
                line = line.strip() 
                line = line.replace(" ", "")
                line = line.split(":", 1)
                
                identifier = line[0]
                if is_identifier_valid(identifier):
                    global_dict[identifier] = line[1]
                else:
                    print("The", identifier, "identifier (line", index, "of serve.settings) is not a valid identifier")

    except FileNotFoundError:
        print("Creating serve.settings file...")
        settings = ""
        for identifier in global_dict:
            if(is_user_allocated(identifier)):
                settings += identifier + ": " + str(global_dict[identifier]) + "\n"
        with open("serve.settings", 'w') as file:
            file.write(settings)

    except:
        print("Unexpected error found:")
        traceback.print_exc()
