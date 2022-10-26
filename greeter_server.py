from concurrent import futures
import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc

from random import *

class Greeter(wordgame_pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        words = ["apple", "banana", "orange"]  # 리스트에 영어 단어 후보를 나열
        word = choice(words)  # 랜덤으로 단어 중 1개를 선택
        print("answer : " + word)  # print answer just for check
        letters = ""  # 플레이어가 지금까지 입력한 알파벳들 저장

        print("Welcome to the Wheel of Fortune!")
        # 정답을 맞힐 때까지 무한 반복
        while True:
            succeed = True  # 성공 여부 확인
            print()
            for letter in word:  # 랜덤 선택된 단어를 알파벳별로 한 글자씩 비교
                if letter in letters:  # 현재 알파벳이 플레이어가 입력한 값들 중에 있으면
                    print(letter, end=" ")  # 그 알파벳을 표시
                else:  # 입력한 값들 중에 없으면
                    print("_", end=" ")  # 밑줄을 표시
                    succeed = False  # 밑줄이 있다는 것은 아직 다 풀지 못했음을 의미 !
            print()

            if succeed:  # 만약 성공했다면 게임 종료
                print("Success")
                break

            letter = input("Enter a letter >> ")  # 플레이어로부터 한 글자씩 입력
            if letter not in letters:  # 입력값 중에 포함되어 있지 않다면
                letters += letter  # 새로 입력받은 글자를 입력값에 추가

            if letter in word:  # 입력한 글자가 제시 단어에 포함되었다면
                print("Correct")
            else:  # 포함되어있지 않다면
                print("Wrong")



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
