def ask_yes_or_no(mensaje: str) -> bool:
    """ Function to carry out queries in the console, waiting for a "yes" or "no" response.
    - "if" returns `True`.
    - "no" returns `False`.
    - Any other input is recognized as invalid, forcing the user to answer again.

    Parameters:
    message (str): message to display in console.

    Returns:
    boolean: Validated response from the user.
    """
    while True:
        print(mensaje)
        respuesta = input()
        if respuesta == 'yes': return True
        elif respuesta == 'no': return False
        print("Please enter 'yes' or 'no'")