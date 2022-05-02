# Converter 🪄

When you want to deploy the Ballot Solidity Smart Contract you need to provide a bytes32[] array ....

```
constructor(bytes32[] memory proposalNames) {
        chairperson = msg.sender;
        voters[chairperson].weight = 1;

        for (uint i = 0; i < proposalNames.length; i++) {
            // 'Proposal({...})' creates a temporary
            // Proposal object and 'proposals.push(...)'
            // appends it to the end of 'proposals'.
            proposals.push(Proposal({
                name: proposalNames[i],
                voteCount: 0
            }));
        }
    }
```

Using this converter, you can trasform a list of **string** into a **byte32[]** array and be ready to deploy your smart contract in the right manner 🦸🏻

Check/Run the main to see the example with Alice and Bob!

```
    proposals = ["Alice", "Bob"]

    converter = Converter()
    results = converter.arrayStringToByte32Array(proposals)

    print(results)

    # Trasform again the json to a python list!
    resultsList = json.loads(results)

    alice = converter.byte32ToString(resultsList[0])
    print(alice)

    bob = converter.byte32ToString(resultsList[1])
    print(bob)

```

Output:

```
["0x416c696365000000000000000000000000000000000000000000000000000000", "0x426f620000000000000000000000000000000000000000000000000000000000"]
Alice
Bob
```

Happy hacking! 🤟🏼
