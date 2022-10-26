from __future__ import print_function

import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


def run():
    print("Welcome to the Wheel of Fortune!")
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = wordgame_pb2_grpc.GameStub(channel)
      response = stub.GuessingLetter(wordgame_pb2.LetterRequest())
      print("Result: " + response.result)
      # print("Greeter client received: " + response.message)
      # response = stub.SayHelloAgain(wordgame_pb2.HelloRequest(name='you'))
      # print("Greeter client received: " + response.message)
      # print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
