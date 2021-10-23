from forta_agent import FindingSeverity, FindingType, create_transaction_event
from agent import handle_transaction
from agent import patch_keccak
from src.constants import CREATE


def generate_keccak256(sign: str) -> str:
    hash = patch_keccak(sign)
    return hash


class TestHighGasAgent:
    def test_returns_empty_findings_if_address_is_wrong(self):
        hash = generate_keccak256(CREATE)
        tx_event = create_transaction_event({
            'receipt': {
                'logs': [{'topics': [hash],
                          'address': "0xlol"}]}
        })

        findings = handle_transaction(tx_event)
        assert len(findings) == 0

    def test_returns_empty_findings_if_hash_is_wrong(self):
        hash = '0xlol'
        tx_event = create_transaction_event({
            'receipt': {
                'logs': [{'topics': [hash],
                          'address': "0xc0dA01a04C3f3E0be433606045bB7017A7323E38"}]}
        })

        findings = handle_transaction(tx_event)
        assert len(findings) == 0

    def test_returns_findings_if_everything_is_correct(self):
        hash = generate_keccak256(CREATE)
        tx_event = create_transaction_event({
            'receipt': {
                'logs': [{'topics': [],
                          'address': "0xc0dA01a04C3f3E0be433606045bB7017A7323E38"},
                         {'topics': [hash],
                          'address': "0xc0dA01a04C3f3E0be433606045bB7017A7323E38"}]}
        })

        findings = handle_transaction(tx_event)
        assert len(findings) != 0
        for finding in findings:
            assert finding.name == 'Compound Governance Event'
            assert finding.description == 'Proposal Event Failed: Create for GovernorAlpha'
            assert finding.protocol == 'ethereum'
            assert finding.alert_id == 'COMP_GOV_ALERT_CREATE'
            assert finding.severity == FindingSeverity.High
            assert finding.type == FindingType.Suspicious
