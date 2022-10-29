from __future__ import print_function

import logging

import grpc
import wordgame_pb2
import wordgame_pb2_grpc


def run():
    print("$$$$$$$$$$ Welcome to the Wheel of Fortune! $$$$$$$$$$\n")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = wordgame_pb2_grpc.GameStub(channel)
        choice = None
        while choice in (None, '', 'Y', 'y'):
            file = "phrases.txt"
            chosen_phrase = stub.ChoosePhrase(wordgame_pb2.PhraseRequest(file_name=file))
            chosen_phrase = chosen_phrase.phrase.strip().upper()
            print("answer : " + chosen_phrase)  # print answer just for check
            init_phrase = stub.InitializePhrase(wordgame_pb2.InitRequest(init_request_phrase=chosen_phrase))
            init_phrase = init_phrase.init_result_phrase.strip().upper()
            print("init_phrase Result before loop: " + init_phrase)  # for check

            temp_list = list(chosen_phrase)
            list_for_count = [] # to remove duplicated letter
            for t in temp_list:
                if t not in temp_list:
                    list_for_count.append(t)
            print(list_for_count) # for check
            phrase_len = len(list_for_count)
            print("length of phrase: " + phrase_len) # for check

            counter = 0
            while True:
                guess = input("Enter a letter: ").upper()
                changed_phrase = stub.ChangeLetter(wordgame_pb2.LetterRequest(chosen_phrase=chosen_phrase,
                                                                              initialized_phrase=init_phrase, letter=guess))
                init_phrase = changed_phrase.result.strip()
                print()

                print("Result: " + init_phrase) # for check
                print("Answer: " + chosen_phrase) # for check

                counter += 1

                if init_phrase == chosen_phrase:
                    print()
                    print("*********** Success! ***********")
                    result = stub.GameResult(wordgame_pb2.GameResultRequest(counter=counter, phrase_len=phrase_len))
                    print("\tYour Result:\n\t\tresult")
                    break
            print()
            choice = input("Go again? (Y/N) ")


if __name__ == '__main__':
    logging.basicConfig()
    run()
