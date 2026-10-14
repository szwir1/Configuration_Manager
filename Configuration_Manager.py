test_settings = {
    "theme": "light",
    "language": "english"}

def add_setting(parametr1, parametr2):
    key, value = parametr2
    key = key.lower()
    value = value.lower()
    

    if key in parametr1:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        parametr1[key] = value
        return(f"Setting '{key}' added with value '{value}' successfully!")


def update_setting(parametr1, parametr2):
    key, value = parametr2
    key = key.lower()
    value = value.lower()

    
    
    if key in parametr1:
        parametr1[key] = value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    
    else:  
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(parametr1, parametr2):
    key = parametr2
    key = key.lower()
    

    if key in parametr1:
        del parametr1[key]
        return(f"Setting '{key}' deleted successfully!")
    else:
        return('Setting not found!')

def view_settings(parametr):
    if not parametr:
        return('No settings available.')
    title = 'Current User Settings:\n'
    for key, value in parametr.items():
        title += f"{key.capitalize()}: {value}\n"
    return (title)          
        

    

print('1. Początkowe ustawienia:')
print(view_settings(test_settings))

print('2. Próba dodania istniejącego ustawienia:')
print(add_setting(test_settings, ('THEME', 'DARK')))

print('3. Dodanie nowego ustawienia:')
print(add_setting(test_settings, ('VOLUME', 'HIGH')))
print(test_settings)

print('4. Aktualizacja istniejącego ustawienia:')
print(update_setting(test_settings, ('VOLUME', 'LOW')))
print(test_settings)

print('5. Aktualizacja nieistniejącego ustawienia:')
print(update_setting(test_settings, ('COLOR', 'BLUE')))
print(test_settings)

print('6. Usunięcie istniejącego ustawienia:')
print(delete_setting(test_settings, 'LANGUAGE'))
print(test_settings)

print('7. Usunięcie nieistniejącego ustawienia:')
print(delete_setting(test_settings, 'FONT'))

print('8. Końcowe ustawienia:')
print(view_settings(test_settings))

print('9. Pusty słownik:')
print(view_settings({}))   


        

    
    