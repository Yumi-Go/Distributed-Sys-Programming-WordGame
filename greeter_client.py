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
            file = "phrases.txt"
            chosen_phrase = stub.ChoosePhrase(wordgame_pb2.PhraseRequest(file_name=file))
            chosen_phrase = chosen_phrase.phrase.strip()
            print("answer : " + chosen_phrase)  # print answer just for check
            init_phrase = stub.InitializePhrase(wordgame_pb2.InitRequest(init_request_phrase=chosen_phrase))
            init_phrase = init_phrase.init_result_phrase.strip()
            print("init_phrase Result before loop: " + init_phrase)  # for check

            while True:
                guess = input("Enter a letter: ")
                changed_phrase = stub.ChangeLetter(wordgame_pb2.LetterRequest(chosen_phrase=chosen_phrase,
                                                                              initialized_phrase=init_phrase, letter=guess))
                init_phrase = changed_phrase.result.strip()
                print()

                print("init_phrase Result: " + init_phrase) # for check
                print("chosen_phrase Result: " + chosen_phrase) # for check

                if init_phrase == chosen_phrase:
                    print("Success!")
                    break
            choice = input("Go again? (Y/N) ")


if __name__ == '__main__':
    logging.basicConfig()
    run()
