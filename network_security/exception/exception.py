import sys
import inspect
from network_security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        # Try to get a traceback from the provided error_details; if none is active,
        # fall back to the caller frame so the exception still reports a useful file/line.
        _, _, exc_tb = error_details.exc_info()
        if exc_tb is None:
            # Use inspect to get the caller frame info
            frame = inspect.stack()[1]
            self.lineno = frame.lineno
            self.file_name = frame.filename
        else:
            self.lineno = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

'''
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise NetworkSecurityException(e,sys)
'''