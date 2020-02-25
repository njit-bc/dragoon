import random
from utils import connect_web3 as connect
from web3 import Web3


if __name__ == '__main__':


    abi = '[{"constant":true,"inputs":[],"name":"gs","outputs":[{"name":"ctr","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"actual_gold_solutions","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"i_val","type":"bytes32[6]"},{"name":"s_val","type":"bytes32[6]"}],"name":"fill_golden","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"workers_counter","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"c1_x","type":"uint256[106]"},{"name":"c1_y","type":"uint256[106]"},{"name":"c2_x","type":"uint256[106]"},{"name":"c2_y","type":"uint256[106]"}],"name":"submit_answers","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"task_swarm_addr","outputs":[{"name":"","type":"bytes32"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"c1_x","type":"uint256"},{"name":"c1_y","type":"uint256"},{"name":"c2_x","type":"uint256"},{"name":"c2_y","type":"uint256"},{"name":"q_index","type":"uint256"},{"name":"worker","type":"address"},{"name":"a_x","type":"uint256"},{"name":"a_y","type":"uint256"},{"name":"z","type":"uint256"}],"name":"different_plaintext_proof","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"actual_gold_indices","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"answers_map","outputs":[{"name":"err_counter","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"indices","type":"uint256[]"},{"name":"sols","type":"uint256[]"},{"name":"r_val","type":"uint256"}],"name":"opening_phase","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"requester","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"workers","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"a","type":"string"}],"name":"FillGold","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"a","type":"bool"}],"name":"debug","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"b","type":"string"}],"name":"OpenGold","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"a","type":"string"}],"name":"PlainTextProof","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"c1_x","type":"uint256"},{"indexed":false,"name":"c1_y","type":"uint256"},{"indexed":false,"name":"c2_x","type":"uint256"},{"indexed":false,"name":"c2_y","type":"uint256"}],"name":"Ciphertexts","type":"event"}]'
    bin = '0x6000801960017fb833be6d483c981488a6b0f32fd133f9f7b8810a9663becb38359c17312105290216601b55608080800160405260ff9091168082526020808301828152810182815201526200005a90601d906004620000b9565b5060006021553480156200006d57600080fd5b5060018054600160a060020a03738884a1aca7d2f031d674994232c10ba64fc339038116600061010081900a91820283830219948516179094558354339092160291161790556200014a565b826004810192821562000107579160200282015b82811115620001075782518260006101000a815481600160a060020a03021916908360ff16021790555091602001919060010190620000cd565b506200011592915062000119565b5090565b6200014791905b8082111562000115578054600160a060020a0360006101000a021916815560010162000120565b90565b611400806200015a6000396000f3006080604052600436106100b85763ffffffff7c0100000000000000000000000000000000000000000000000000000000600035041662e71aaf81146100bd5780630ac41249146100e557806318a9ac3c146100fd578063243cfe1414610174578063257dd823146101895780635d6e6e8f1461026d5780637d047adc1461029d578063830adaee146102ee578063908a938c146103065780639eae737b14610327578063b61e96a5146103c1578063f1a22dc2146103fe575b600080fd5b3480156100c957600080fd5b506100d2610416565b6040805191825251602090910181900390f35b3480156100f157600080fd5b506100d260043561041f565b34801561010957600080fd5b506101726004803603810190808060c0019060068060200260405190810160405280929190826006602002808284375050604080516006602081028083019093529598979660c08101969195509350915083908390808284375093965061043595505050505050565b005b34801561018057600080fd5b506100d26104f8565b34801561019557600080fd5b5061025660048036038101908080610d400190606a806020026040519081016040528092919082606a60200280828437505060408051606a6020810280830190935295989796610d40810196919550935091508390839080828437505060408051606a6020810280830190935295989796610d40810196919550935091508390839080828437505060408051606a6020810280830190935295989796610d40810196919550935091508390839080828437509396506104fe95505050505050565b604080519115151515825251602090910181900390f35b34801561027957600080fd5b506102826109ea565b60408051600019928316909216825251602090910181900390f35b3480156102a957600080fd5b50610256600480359060209081018035919081018035919081018035919081018035919081018035600160a060020a03169190810180359190810180359101356109f0565b3480156102fa57600080fd5b506100d2600435610c75565b34801561031257600080fd5b506100d2600160a060020a0360043516610c84565b34801561033357600080fd5b50610256600480360381019080803590602001908201803590602001908080602002602001604051908101604052809392919081815260200183836020028082843750506040805187358901803560208181028082018501909552818452989b9a9989019892975090820195509350839250850190849080828437509497505093359450610c999350505050565b3480156103cd57600080fd5b506103d6610f35565b6040518082600160a060020a0316600160a060020a0316815260200191505060405180910390f35b34801561040a57600080fd5b506103d6600435610f4d565b600c6002015481565b60158160068110151561042e57fe5b0154905081565b6000809054906101000a9004600160a060020a0316600160a060020a031633600160a060020a031614151561046957600080fd5b610479600060020183600661123b565b5061048b60066002810190839061123b565b507fbe2e6cf1a5f5c472dddfcec10c595b7addbebc6bf89002859defae82d7fedf176040518080602001828103825260128152602001807f476f6c642061727261792066696c6c656421000000000000000000000000000081525060200191505060405180910390a15050565b60215481565b600080600061050b61127f565b600080339450600160009054906101000a9004600160a060020a0316600160a060020a031663a87430ba866040518263ffffffff167c01000000000000000000000000000000000000000000000000000000000281526004018082600160a060020a0316600160a060020a03168152602001915050602060405180830381600087803b15801561059a57600080fd5b505af11580156105ae573d6000803e3d6000fd5b505050506040513d60208110156105c457600080fd5b505115156105d157600080fd5b8982606a811015156105df57fe5b60200201518983606a811015156105f257fe5b60200201518984606a8110151561060557fe5b60200201518985606a8110151561061857fe5b602002015160405180858152602001848152602001838152602001828152602001945050505050604051809103902093507f6d56ffa6ff22d4fa791102c96194240d81171e8c364ceb8509c51787910a41028a83606a8110151561067857fe5b60200201518a84606a8110151561068b57fe5b60200201518a85606a8110151561069e57fe5b60200201518a86606a811015156106b157fe5b60200201516040518085815260200184815260200183815260200182815260200194505050505060405180910390a18383600001516000606a811015156106f457fe5b6020020190600019169081600019168152505082601c600087600160a060020a0316600160a060020a0316815260200190815260200160002060008201518160000190606a6107449291906112ae565b50602082015161075a90606a83019060036112e1565b50604082015181606d0155905050600191505b606a8210156108cf578982606a8110151561078457fe5b60200201518983606a8110151561079757fe5b60200201518984606a811015156107aa57fe5b60200201518985606a811015156107bd57fe5b602002015160405180858152602001848152602001838152602001828152602001945050505050604051809103902093507f6d56ffa6ff22d4fa791102c96194240d81171e8c364ceb8509c51787910a41028a83606a8110151561081d57fe5b60200201518a84606a8110151561083057fe5b60200201518a85606a8110151561084357fe5b60200201518a86606a8110151561085657fe5b60200201516040518085815260200184815260200183815260200182815260200194505050505060405180910390a183601c600087600160a060020a0316600160a060020a0316815260200190815260200160002060000183606a811015156108bb57fe5b60001990921691015560019091019061076d565b5060005b6021548110156109255784600160a060020a0316601d6021546004811015156108f857fe5b0154600160a060020a0360006101000a909104811616141561091d57600095506109dd565b6001016108d3565b600460215410156109d85784601d60215460048110151561094257fe5b0160006101000a815481600160a060020a030219169083600160a060020a031602179055506001602160008282540192505081905550606060405190810160405280606a60ff168152602001606a60ff168152602001606a60ff16815250601c600087600160a060020a0316600160a060020a03168152602001908152602001600020606a019060036109d692919061130f565b505b600195505b5050505050949350505050565b601b5481565b6000805b6006811015610c6257600f81600681101515610a0c57fe5b0154871415610c5a5786601c600088600160a060020a0316600160a060020a03168152602001908152602001600020606a016000600381101515610a4c57fe5b01541415610a5d5760009150610c67565b86601c600088600160a060020a0316600160a060020a03168152602001908152602001600020606a016001600381101515610a9457fe5b01541415610aa55760009150610c67565b86601c600088600160a060020a0316600160a060020a03168152602001908152602001600020606a016002600381101515610adc57fe5b01541415610aed5760009150610c67565b604080518c815260209081018c815281018b815281018a81529151918101829003909120600160a060020a03808916166000908152601c81840190815290920182208219909116910188606a81101515610b4357fe5b0154600019161415610c5157610b728b8b8b8b898989601589600681101515610b6857fe5b0154600103610f75565b15610c5157600160a060020a03808716166000818152601c60208083018281529081018084209484529190529020606d01548891606a0190600381101515610bb657fe5b0155600160a060020a03808716166000908152601c6020808301918252908101909120606d018054600101905560408051808301818103909152601d81527f446966666572656e7420506c61696e746578742056657269666965642100000090830190815290517fad9b8278dfd506d1c9decb1d44a43bcd3f244dab664f2bde7b11b924274d896c929190910181900390a160019150610c67565b60009150610c67565b6001016109f4565b600091505b509998505050505050505050565b600f8160068110151561042e57fe5b601c602052600090815260409020606d015481565b60008080805b6006831015610f26578683815181101515610cb657fe5b6020918201908202015160408051918252805191830182900382208883528151928401839003832060001991821682168452811616918301918252519101819003902086519092508690849081101515610d0c57fe5b6020918201908202015160408051918252805191830182900382208883528151928401839003832060008019928316831685529082169091169284019283529051919092018190039020915060020183600681101515610d6857fe5b0154600019168260001916148015610d9a5750600260060183600681101515610d8d57fe5b0154600019168160001916145b15610e84578683815181101515610dad57fe5b90602001906020020151600f84600681101515610dc657fe5b015585518690849081101515610dd857fe5b90602001906020020151601584600681101515610df157fe5b0155604080516020808201828103909252602482527f436f6d6d69746d656e7420746f20696e64657820616e6420736f6c20636f72729181019182527f65637421000000000000000000000000000000000000000000000000000000009082015281517ff9d5bc1f7d8ca67bb4dc255cfec9eda367d129d600e4c4c725d400580ae2bd82929190910181900390a1610f1b565b7ff9d5bc1f7d8ca67bb4dc255cfec9eda367d129d600e4c4c725d400580ae2bd826040518080602001828103825260228152602001807f436f6d6d69746d656e7420746f20696e64657820616e6420736f6c2066616c7381526020017f652100000000000000000000000000000000000000000000000000000000000081525060400191505060405180910390a160009350610f2b565b600190920191610c9f565b600193505b5050509392505050565b6000809054906101000a9004600160a060020a031681565b601d81600481101515610f5c57fe5b016000915054906101000a9004600160a060020a031681565b600080610f80611342565b610f88611342565b610f90611342565b610f98611342565b610fa28a8a61104e565b9450610fb18c8c8c8c89611073565b9350610fbe8e8e8a6110d1565b9250866001141561101c57610fe9604080519081016040528060018152602001600281525086611109565b9150610ff5828461119d565b905083600001518160000151148015611015575083602001518160200151145b955061103d565b8360000151836000015114801561103a575083602001518360200151145b95505b505050505098975050505050505050565b6040805192835260209283019182525191018190039020608260020a60019091040490565b61107b611342565b611083611342565b61108b611342565b5050604080518082018252878152602080820188905282518084019093528683528201859052906110c5816110c08487611109565b61119d565b98975050505050505050565b6110d9611342565b6110e1611342565b5060408051808201909152848152602081018490526111008184611109565b95945050505050565b611111611342565b611119611359565b6000846000015182600060038110151561112f57fe5b602002018181525050846020015182600160038110151561114c57fe5b60200201528382600260038110151561116157fe5b6020020152606083608084600060076107d05a03f19050806000811461118657611188565bfe5b5080151561119557600080fd5b505092915050565b6111a5611342565b6111ad611378565b600084600001518260006004811015156111c357fe5b60200201818152505084602001518260016004811015156111e057fe5b602002015260008401518260026004811015156111f957fe5b602002018181525050836020015182600360048110151561121657fe5b602002015260608360c084600060066107d05a03f19050806000811461118657611188565b826006810192821561126f579160200282015b8281111561126f57825182906000191690559160200191906001019061124e565b5061127b929150611397565b5090565b610dc0604051908101604052806112946113b4565b81526020016112a1611359565b8152602001600081525090565b82606a810192821561126f579160200282018281111561126f57825182906000191690559160200191906001019061124e565b826003810192821561126f579160200282015b8281111561126f5782518255916020019190600101906112f4565b826003810192821561126f579160200282015b8281111561126f578251829060ff16905591602001919060010190611322565b604080518082019091526000808252602082015290565b6060604051908101604052806003906020820280388339509192915050565b6080604051908101604052806004906020820280388339509192915050565b6113b191905b8082111561127b576000815560010161139d565b90565b610d4060405190810160405280606a9060208202803883395091929150505600a165627a7a723058208b43fa9bf1f53f9d26ccededcb925504b78ce05fa3b207b3030b0b9f9f7eec640029'
    addr = Web3.toChecksumAddress('0xb8eeb62d9d77a06aac25581bb78563cbc3916780')

    web3, pwd = connect()
    web3.personal.unlockAccount(web3.personal.listAccounts[0], pwd)


    contract = web3.eth.contract(abi=abi, bytecode=bin, address=addr)

    num_questions = 106 # total number of questions in a task
    num_workers = 4     # total number of workers
    answers = []        # answers of a particular worker
    ansvec = []         # answers of all workers
    ciphertexts = []    # ciphertext of a particular worker
    ciphervec = []      # ciphertexts of all workers

    total_gas = 0

    golden_standard = []    # golden standard indices
    num_gold = 6
    golden_answers = []     # actual answers of golden standard

    print("-----Generate Gold Standard and solutions-------------")
    # generating distinct golden standard indices at random with a seed
    random.seed(1)
    for i in range(0, num_gold):
        random_index = random.randint(0, num_questions)
        while(random_index in golden_standard):
            random_index = random.randint(0, num_questions)
        golden_standard.append(random_index)
        golden_answers.append(random.randint(0,1))
    golden_standard.sort()
    print("Golden indices: ", golden_standard)
    print("Golden answers: ", golden_answers)


    print("-----Commitment to Golden Standard and Solutions-------------")

    # randomness used for commitment to golden standard indices and solutions
    randcom = 7259499494255386899158208772778770782164622743034610220459868739493258500284


    icom_array = [None] * num_gold
    scom_array = [None] * num_gold
    for i in range(0, num_gold):
        icom = Web3.soliditySha3(['bytes32', 'bytes32'], [Web3.soliditySha3(['uint256'],[golden_standard[i]]),Web3.soliditySha3(['uint256'],[randcom])])    #commitment to index
        scom = Web3.soliditySha3(['bytes32', 'bytes32'], [Web3.soliditySha3(['uint256'],[golden_answers[i]]),Web3.soliditySha3(['uint256'],[randcom])])     #commitment to solution
        icom_array[i] = icom
        scom_array[i] = scom

    fill_golden = contract.functions.fill_golden(icom_array, scom_array)
    gas = fill_golden.estimateGas()
    total_gas = total_gas + gas
    tx_hash = fill_golden.transact({'gas': gas, 'gasPrice': 1000000000})
    print(web3.toHex(tx_hash))
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash, 600)
    print(tx_receipt)
