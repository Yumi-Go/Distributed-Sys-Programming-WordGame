from __future__ import print_function

import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


def run():
    print("Welcome to the Wheel of Fortune!")
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = wordgame_pb2_grpc.GameStub(channel)
      choice = None
      while choice in (None, '', 'Y', 'y'):
          guess = input("Enter a letter: ")
          response = stub.GuessingLetter(wordgame_pb2.LetterRequest(letter=guess))
          if response.result == 'correct':
              print(guess, end=" ")
          else:
              print("_", end=" ")
          print()
          print("Result: " + response.result)
          choice = input("Go again? (Y/N) ")
      # guess = input("Enter a letter: ")
      # response = stub.GuessingLetter(wordgame_pb2.LetterRequest(letter=guess))
      # if response.result == 'correct':
      #     print(guess, end=" ")
      # else:
      #     print("_", end=" ")

    print()
    print("Result: " + response.result)



if __name__ == '__main__':
    logging.basicConfig()
    run()
