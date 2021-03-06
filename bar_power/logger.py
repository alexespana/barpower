import logging, os
from bar_power.config import Config

class Logger():
    """Representa un objeto para registrar la actividad de la aplicación"""

    def __init__(self, format='%(asctime)s <=> %(levelname)s <=> %(pathname)s <=> %(message)s', level=logging.DEBUG):
        self.configuration = Config()
        self.log_directory = self.configuration.get_log_directory()
        self.log_file      = self.configuration.get_log_file()
        self.milogger = logging.getLogger()     # Objeto de log
        self.format        = format
        self.level         = level

        # Crear directorio en caso de no existir
        if not os.path.exists(self.log_directory):
            try:
                os.makedirs(self.log_directory, exist_ok=True)
            except OSError:
                raise OSError("Error al intentar crear el directorio ")

        # Nivel de logging
        self.milogger.setLevel(level)

        # Configuración básica del sistema de log
        logging.basicConfig(filename=self.log_directory + self.log_file, format=self.format)
    
    
    def debug(self, msg : str):
        """
        Método para registrar actividad del nivel DEBUG en la aplicación
        
        Parameters
        -----------
        msg : str
            Mensaje de registro para el nivel debug
        """
        self.milogger.debug(msg)
    
    def info(self, msg : str):
        """
        Método para registrar actividad del nivel INFO en la aplicación
        
        Parameters
        -----------
        msg : str
            Mensaje de registro para el nivel info
        """
        self.milogger.info(msg)

    def warning(self, msg : str): 
        """
        Método para registrar actividad del nivel WARNING en la aplicación
        
        Parameters
        -----------
        msg : str
            Mensaje de registro para el nivel warning
        """
        self.milogger.warning(msg)

    def error(self, msg : str):
        """
        Método para registrar actividad del nivel ERROR en la aplicación
        
        Parameters
        -----------
        msg : str
            Mensaje de registro para el nivel error
        """
        self.milogger.error(msg)

    def critical(self, msg : str):
        """
        Método para registrar actividad del nivel CRITICAL en la aplicación
        
        Parameters
        -----------
        msg : str
            Mensaje de registro para el nivel critical
        """
        self.milogger.critical(msg)
