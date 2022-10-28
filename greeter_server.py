from concurrent import futures
import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc

from random import *

class Game(wordgame_pb2_grpc.GameServicer):

    def GuessingLetter(self, request, context):

        phrases = []

        file = open("phrases.txt", "r")
        line = file.readline()
        phrases.append(line)
        file.close()

        phrase = choice(phrases)
        print("answer : " + phrase)  # print answer just for check
        # words = phrase.split()

        #letter = input("Enter a letter >> ")
        letters = ""

        while True:
            success = True
            print()
            for i in phrase:
                print(i)
                if request.letter == i:

                    letters = letters + request.letter
                    # print(request.letter)
                    # return wordgame_pb2.ResultReply(result='%s is correct' % request.letter)
                else:
                    letters = letters + "_"
                    success = False
                    # return wordgame_pb2.ResultReply(result='%s is incorrect' % request.letter)

            if success:
                print("Success!")
                break

            return wordgame_pb2.ResultReply(result=letters)

        # return wordgame_pb2.HelloReply(message='Hello, %s!' % request.name)



def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    wordgame_pb2_grpc.add_GameServicer_to_server(Game(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
