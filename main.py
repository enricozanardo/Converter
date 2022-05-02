import json

from Converter import Converter

if __name__ == "__main__":

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
