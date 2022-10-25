from __future__ import print_function

import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


def run():

    # response = . (name = "") <-- this is request

    print("Will try to greet world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
      stub = wordgame_pb2_grpc.GreeterStub(channel)
      response = stub.SayHello(wordgame_pb2.HelloRequest(name='you'))
      print("Greeter client received: " + response.message)
      response = stub.SayHelloAgain(wordgame_pb2.HelloRequest(name='you'))
      print("Greeter client received: " + response.message)
      print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
