import json


class Converter():
    """
    A simple string converter for Solidity string32 arrays to use the Ballot Example!!!
    """

    def arrayStringToByte32Array(self, names):
        values = []
        for name in names:
            value = self.stringToByte32Array(name)
            values.append(value)

        # Return a json list type!
        jsonValues = json.dumps(values)

        return jsonValues

    def stringToByte32Array(self, text: str) -> str:
        size = 64
        hexVal = text.encode().hex()
        delta = size - len(hexVal)

        index = 0
        while index < delta:
            index += 1
            hexVal = hexVal + "0"

        hexVal = "0x" + hexVal

        return hexVal

    def byte32ToString(self, hexVal: str):
        # remove "0x"
        text = hexVal[2:]

        # Convert to bytes object
        bytesObject = bytes.fromhex(text)

        # Convert to ASCII representation
        asciiString = bytesObject.decode("ASCII")

        return asciiString
