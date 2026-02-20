from app.connectors.crm_connector import CRMConnector

def test_crm_connector():
    connector = CRMConnector()
    data = connector.fetch()
    assert isinstance(data, list)
    assert len(data) > 0
