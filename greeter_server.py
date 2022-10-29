from concurrent import futures
import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc

from random import *

class Game(wordgame_pb2_grpc.GameServicer):

    def ChoosePhrase(self, request, context):

        file = open(request.file_name, "r")
        phrases = file.readlines()
        file.close()

        # for check
        for x in range(len(phrases)):
            print(phrases[x])

        chosen_phrase = choice(phrases)
        # print("answer : " + chosen_phrase)  # print answer just for check
        return wordgame_pb2.PhraseResultReply(phrase=chosen_phrase)


    def InitializePhrase(self, request, context):

        letters_list = []
        init_letters = ""
        phrase = request.init_request_phrase

        for k in range(len(phrase)):
            if phrase[k] == " ":
                letters_list.append(" ")
            elif phrase[k] == ",":
                letters_list.append(",")
            elif phrase[k] == "\'":
                letters_list.append("\'")
            else:
                letters_list.append("_")

        # for check
        for y in range(len(letters_list)):
            init_letters = init_letters + letters_list[y]
        print(init_letters + "this is init_letters") # for check

        return wordgame_pb2.InitResultReply(init_result_phrase=init_letters)

    def ChangeLetter(self, request, context):
        chosen_phrase = request.chosen_phrase
        changed_phrase = request.initialized_phrase
        letter = request.letter
        print("chosen_phrase: " + chosen_phrase) # for check
        print("changed_phrase: " + changed_phrase) # for check
        print("letter: " + letter) # for check

        letters_list = list(changed_phrase)
        # letters_list = []
        # for g in range(len(changed_phrase)):
        #     letters_list.append(changed_phrase[g])

        for i in range(len(chosen_phrase)):
            print("chosen_phrase[i]: " + chosen_phrase[i])  # for check
            if letter == chosen_phrase[i]:
                letters_list[i] = letter

        result_phrase = ''.join(letters_list)

        print("changed_phrase after change: " + result_phrase)
        # for d in range(len(letters_list)):
        #     result_letters = result_letters + letters_list[d]
        # print(result_letters + "this is result_letters")
        #
        # if result_letters == phrase:
        #     print("Success!")
        #     success = True
        #     break

        return wordgame_pb2.LetterResultReply(result=result_phrase)




    # def GuessingLetter(self, request, context):
    #
    #     success = False
    #
    #     while not success:
    #         print()
    #         for i in range(len(phrase)):
    #             print(phrase[i])  # for check
    #             if request.letter == phrase[i]:
    #                 letters_list[i] = request.letter
    #
    #         for d in range(len(letters_list)):
    #             result_letters = result_letters + letters_list[d]
    #         print(result_letters + "this is result_letters")
    #
    #         if result_letters == phrase:
    #             print("Success!")
    #             success = True
    #             break
    #
    #
    #     # while True:
    #     #     success = True
    #     #     print()
    #
    #         # for i in range(len(phrase)):
    #         #     print(phrase[i])  # for check
    #         #     if request.letter == phrase[i]:
    #         #         letters_list.append(request.letter)
    #         #
    #         #     else:
    #         #         letters_list.append("_")
    #         #         success = False
    #
    #         # for j in range(len(letters_list)):
    #         #     letters = letters + letters_list[j]
    #         #
    #         # print(letters) # for check
    #         #
    #         # if success:
    #         #     print("Success!")
    #         #     break
    #
    #     return wordgame_pb2.ResultReply(result=success)





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
