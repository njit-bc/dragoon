# On July 7th, 2020, we identify that there is a minor implementation bug (i.e., the on-chain veirifer and the off-chain prover for correct decryption are incorrectly instantiated). Though the bug violates security, the fix of it could incur merely small overhead. Patch is under working and will be updated soon.


=========================


# Dragoon: Private Decentralized HITs Made Practical
A fair, efficient, and private decentralized protocol for crowdsourcing of human knowledge

## A deployed instance at Ropsten network

https://ropsten.etherscan.io/address/0x5481b096c78c8e09c1bfbf694e934637f7d66698

Worker 0 (0xbeef1bed3677fe070591074de013cd371b121027): 2,671,953 gas

Worker 1 (0xec1f5acd361e439ad1db6d1d7708341460b9439d): 2,678,991 gas

Worker 2 (0x516d5bb41339db0fc24c47dc5bcca8c38b21775d): 2,666,645 gas

Worker 3 (0xeb00e4c95368d1f7f440d304a0084de5904f17e1): 2,669,299 gas

All workers: 10,686,888 gas

Rquester (optimistic case): 973,045 + 270,605 + 234,099 = 1,477,749 gas for the whole protocol

Rquester (worst case): average (85,335 + 71,221 + 63,680) - 2*21,000 = 178,236 gas to reject per each submission

=========================

Overall (optimistic): 10,686,888 + 1,477,749 = 12,164,637

Overall (worst case): 10,686,888 + 1,477,749 + 178,236 * 4 = 12,877,581
