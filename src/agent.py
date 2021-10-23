from src.constants import CONTRACTS, SIGNATURES_DICT, SIGNATURES_ID
from forta_agent import Finding, FindingType, FindingSeverity
from Crypto.Hash import keccak
from forta_agent import transaction_event


# This is the monkey patch which resolves the issue with Error: python: module 'sha3' has no attribute 'keccak_256'
def patch_keccak(val):
    hash = keccak.new(digest_bits=256)
    hash.update(bytes(val, encoding='utf-8'))
    return f'0x{hash.hexdigest()}'


transaction_event.keccak256 = patch_keccak


def handle_transaction(transaction_event):
    findings = []
    for (key, contract) in CONTRACTS.items():
        for signature in SIGNATURES_DICT.keys():
            logs_list = transaction_event.filter_event(signature, contract)
            if not logs_list:
                continue

            if transaction_event.status:
                findings.append(Finding({
                    'name': 'Compound Governance Event',
                    'description': f'Proposal Event: {SIGNATURES_DICT.get(signature)} for {key}',
                    'alert_id': SIGNATURES_ID.get(signature),
                    'type': FindingType.Suspicious,
                    'severity': FindingSeverity.Info,
                }))

            else:
                findings.append(Finding({
                    'name': 'Compound Governance Event',
                    'description': f'Proposal Event Failed: {SIGNATURES_DICT.get(signature)} for {key}',
                    'alert_id': SIGNATURES_ID.get(signature),
                    'type': FindingType.Suspicious,
                    'severity': FindingSeverity.High,
                }))

    return findings
