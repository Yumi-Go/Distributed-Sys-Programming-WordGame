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

            list_to_delete = [" ", ",", "\'", "!", "-", "."]
            list_for_count = [] # to remove duplicated letter
            for t in chosen_phrase:
                if (t not in list_to_delete) and (t not in list_for_count):
                    list_for_count.append(t)
            # print(list_for_count) # for check
            phrase_len = len(list_for_count)
            # print("length of phrase: " + str(phrase_len)) # for check

            counter = 0
            while True:
                guess = input("Enter a letter: ").upper()
                changed_phrase = stub.ChangeLetter(wordgame_pb2.LetterRequest(chosen_phrase=chosen_phrase,
                                                                              initialized_phrase=init_phrase, letter=guess))
                init_phrase = changed_phrase.result.strip()
                print()

                print("Result: " + init_phrase)
                # print("Answer: " + chosen_phrase) # for check

                counter += 1

                if init_phrase == chosen_phrase:
                    print()
                    print("*********** Success! ***********")
                    result = stub.GameResult(wordgame_pb2.GameResultRequest(counter=counter, phrase_len=phrase_len))
                    result = result.game_result
                    print(f'\tYour Result:\n\t\t{result}')
                    break
            print()
            choice = input("Go again? (Y/N) ")


if __name__ == '__main__':
    logging.basicConfig()
    run()
