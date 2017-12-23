#!/usr/bin/python3
#
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        inputFile = str(sys.argv[1])
        outputFile = str(sys.argv[2])
        wordCount = int(sys.argv[3])
        with open(inputFile, "rb") as fi, open(outputFile, "w") as fo:
            for i in range(wordCount):
                b = fi.read(4);
                if len(b) == 4:
                    fo.write("{:02x}{:02x}{:02x}{:02x}\n".format(b[3], b[2], b[1], b[0]))
                else:
                    fo.write("0\n")

    else:
        print("Not enough parameters {0}".format(len(sys.argv)))
        print("Usage: bin32hex <inputBinFile> <outputHexFile> <32bitWordCount>")