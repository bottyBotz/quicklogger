import os
import pytest
import tempfile
import logging
from quicklogging import setup_logger


def test_setup_logger_default_level():
    logger = setup_logger()
    assert logger.level == logging.INFO


def test_setup_logger_custom_level():
    logger = setup_logger(level=logging.DEBUG)
    assert logger.level == logging.DEBUG


def test_setup_logger_file_handler():
    with tempfile.TemporaryDirectory() as temp_dir:
        log_file = os.path.join(temp_dir, 'test_logger.log')
        logger = setup_logger(level=logging.DEBUG, log_file=log_file)

        logger.debug("Test file handler")

        assert os.path.isfile(log_file)
        with open(log_file, 'rt') as f:
            log_contents = f.read()
        assert "Test file handler" in log_contents




def test_setup_logger_stream_handler(capsys):
    logger = setup_logger(level=logging.WARNING)

    logger.warning("Test stream handler")

    captured = capsys.readouterr()
    assert "Test stream handler" in captured.out


if __name__ == '__main__':
    pytest.main()
