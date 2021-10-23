CONTRACTS = {
    "GovernorAlpha": "0xc0dA01a04C3f3E0be433606045bB7017A7323E38",
    "GovernorBravo": "0xc0da02939e1441f497fd74f78ce7decb17b66529"
}

CREATE = "ProposalCreated(uint256,address,address[],uint256[],string[],bytes[],uint256,uint256,string)"
VOTE_CAST = "VoteCast(address,uint256,bool,uint256)"
CANCEL = "ProposalCanceled(uint256)"
EXECUTE = "ProposalExecuted(uint256)"
QUEUED = "ProposalQueued(uint256,uint256)"
VOTING_DELAY = "VotingDelaySet(uint256,uint256)"
VOTING_PERIOD = "VotingPeriodSet(uint256,uint256)"
NEW_IMPLEMENTATION = "NewImplementation(address,address)"
PROPOSAL_THRESHOLD = "ProposalThresholdSet(uint256,uint256)"
NEW_PENDING_ADMIN = "NewPendingAdmin(address,address)"

SIGNATURES_DICT = {
    CREATE: 'Create',
    VOTE_CAST: 'VoteCast',
    CANCEL: 'Cancel',
    EXECUTE: 'Execute',
    QUEUED: 'Queue',
    VOTING_DELAY: 'Voting Delay',
    VOTING_PERIOD: 'Voting Period',
    NEW_IMPLEMENTATION: 'New Implementation',
    PROPOSAL_THRESHOLD: 'Proposal Threshold',
    NEW_PENDING_ADMIN: 'New Pending Admin'
}

SIGNATURES_ID = {
    CREATE: 'COMP_GOV_ALERT_CREATE',
    VOTE_CAST: 'COMP_GOV_ALERT_VOTE_CAST',
    CANCEL: 'COMP_GOV_ALERT_CANCEL',
    EXECUTE: 'COMP_GOV_ALERT_EXECUTE',
    QUEUED: 'COMP_GOV_ALERT_QUEUED',
    VOTING_DELAY: 'COMP_GOV_ALERT_VOTING_DELAY',
    VOTING_PERIOD: 'COMP_GOV_ALERT_VOTING_PERIOD',
    NEW_IMPLEMENTATION: 'COMP_GOV_ALERT_IMPLEMENTATION',
    PROPOSAL_THRESHOLD: 'COMP_GOV_ALERT_THRESHOLD',
    NEW_PENDING_ADMIN: 'COMP_GOV_ALERT_ADMIN'
}