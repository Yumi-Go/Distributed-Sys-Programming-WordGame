from concurrent import futures
import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


class Greeter(wordgame_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        # read phrases change to _____ ___ ______ if request in phrase..
        # return phrase



        return wordgame_pb2.HelloReply(message='Hello, %s!' % request.name)

    def SayHelloAgain(self, request, context):
      return wordgame_pb2.HelloReply(message='Hello again, %s!' % request.name)


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