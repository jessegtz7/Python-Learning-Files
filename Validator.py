#Example of a custom module to be imported *Check the Modules.py File*

import re

def validar_correo(correo):
    if len(correo) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", correo)
                   )