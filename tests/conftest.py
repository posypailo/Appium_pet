import pytest
from mobile_project.utils.driver_factory import DriverFactory
from mobile_project.configs.android_config import get_android_capabilities
from mobile_project.configs.ios_config import get_ios_capabilities
from mobile_project.utils.logger import configure_logging


@pytest.fixture(scope="session", autouse=True)
def configure_log():
    configure_logging()


@pytest.fixture(scope="session")
def android_driver():
    capabilities = get_android_capabilities()
    driver = DriverFactory.get_driver('android', capabilities)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def ios_driver():
    capabilities = get_ios_capabilities()
    driver = DriverFactory.get_driver('ios', capabilities)
    yield driver
    driver.quit()
