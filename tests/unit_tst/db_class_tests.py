import pytest
from ...classes.database_files.db_tables import CompanyTicker

@pytest.mark.skip('pending code')
def test_company_ticker_no_args_1(CompanyTicker):
    company = CompanyTicker()
    actual = company.__repr__()
    expected = """

        """