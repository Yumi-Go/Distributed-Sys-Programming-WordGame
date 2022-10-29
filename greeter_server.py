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

        # # for check
        # for x in range(len(phrases)):
        #     print(phrases[x])

        chosen_phrase = choice(phrases)
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
            elif phrase[k] == "!":
                letters_list.append("!")
            elif phrase[k] == "-":
                letters_list.append("-")
            elif phrase[k] == ".":
                letters_list.append(".")
            else:
                letters_list.append("_")

        # for check
        for y in range(len(letters_list)):
            init_letters = init_letters + letters_list[y]
        # print("Initialized letters: " + init_letters) # for check

        return wordgame_pb2.InitResultReply(init_result_phrase=init_letters)

    def ChangeLetter(self, request, context):
        chosen_phrase = request.chosen_phrase
        changed_phrase = request.initialized_phrase
        letter = request.letter
        # print("chosen_phrase: " + chosen_phrase) # for check
        # print("changed_phrase: " + changed_phrase) # for check
        # print("letter: " + letter) # for check

        letters_list = list(changed_phrase)

        for i in range(len(chosen_phrase)):
            # print(f'chosen_phrase[{i}]: ' + chosen_phrase[i])  # for check
            if letter == chosen_phrase[i]:
                letters_list[i] = letter

        result_phrase = ''.join(letters_list)
        # print("changed_phrase after change: " + result_phrase) # for check

        return wordgame_pb2.LetterResultReply(result=result_phrase)


    def GameResult(self, request, context):
        counter = request.counter
        phrase_len = request.phrase_len

        if counter == phrase_len:
            result = "Great! You succeeded in only one try every letter!"
            # print(result) # for check
        elif counter <= (1.2 * phrase_len):
            result = f'Well Done!\n\t\tSuccess after {counter} attempts'
            # print(result) # for check
        elif counter <= (1.5 * phrase_len):
            result = f'So-So\n\t\tSuccess after {counter} attempts'
            # print(result) # for check
        else:
            result = f'Not Good~ Practice more!\n\t\tSuccess after {counter} attempts'
            # print(result) # for check

        return wordgame_pb2.GameResultReply(game_result=result)


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
