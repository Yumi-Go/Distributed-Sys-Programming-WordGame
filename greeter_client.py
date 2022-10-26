from __future__ import print_function

import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


def run():
    print("Welcome to the Wheel of Fortune!")
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = wordgame_pb2_grpc.GameStub(channel)
      Guess = input("Enter letter: ")
      response = stub.GuessingLetter(wordgame_pb2.LetterRequest(letter=Guess))
      print("Result: " + response.result)



if __name__ == '__main__':
    logging.basicConfig()
    run()
