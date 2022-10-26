from concurrent import futures
import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc

from random import *

class Greeter(wordgame_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):

        phrases = []

        file = open("phrases.txt", "r")
        line = file.readline()
        phrases.append(line)
        file.close()

        phrase = choice(phrases)
        print("answer : " + phrase)  # print answer just for check
        # words = phrase.split()

        letter = input("Enter a letter >> ")

        while True:
            succeed = True
            print()

            # if letter in phrase:
            #     print("Correct")
            # else:
            #     print("Wrong")

            for i in phrase:
                if letter == i:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
                    succeed = False
            print()

            if succeed:
                print("Success!")
                break


        # return wordgame_pb2.HelloReply(message='Hello, %s!' % request.name)



def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wordgame_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
