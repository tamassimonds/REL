import logging
import os
import sys
from datetime import datetime
from typing import Optional

class CustomLogger:
    """A custom logger that can be used across the application."""
    
    LEVELS = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }

    def __init__(
        self,
        name: str = 'app',
        log_level: str = 'INFO',
        log_file: Optional[str] = 'logs/app.log',
        format_string: Optional[str] = None
    ):
        """
        Initialize the logger.
        
        Args:
            name: Logger name
            log_level: Minimum log level to display
            log_file: Path to log file (None for console-only)
            format_string: Custom format string for log messages
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.LEVELS.get(log_level.upper(), logging.INFO))
        
        if not self.logger.handlers:
            # Default format string if none provided
            if format_string is None:
                format_string = '[%(asctime)s] %(levelname)s [%(name)s] - %(message)s'
            
            formatter = logging.Formatter(format_string)
            
            # Console handler
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)
            
            # File handler (if log_file is specified)
            if log_file:
                # Create logs directory if it doesn't exist
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def debug(self, message: str, *args, **kwargs):
        """Log debug message."""
        self.logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        """Log info message."""
        self.logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        """Log warning message."""
        self.logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        """Log error message."""
        self.logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs):
        """Log critical message."""
        self.logger.critical(message, *args, **kwargs)

# Create a default logger instance
default_logger = CustomLogger()

# Convenience functions using the default logger
def debug(message: str, *args, **kwargs):
    default_logger.debug(message, *args, **kwargs)

def info(message: str, *args, **kwargs):
    default_logger.info(message, *args, **kwargs)

def warning(message: str, *args, **kwargs):
    default_logger.warning(message, *args, **kwargs)

def error(message: str, *args, **kwargs):
    default_logger.error(message, *args, **kwargs)

def critical(message: str, *args, **kwargs):
    default_logger.critical(message, *args, **kwargs)
