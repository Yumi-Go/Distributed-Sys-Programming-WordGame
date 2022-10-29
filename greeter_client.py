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
            list_for_count = []
            for l in temp_list:
                if l not in temp_list:
                    list_for_count.append(l)
            print(list_for_count) # for check

            num_character = len(chosen_phrase)
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

                    if counter == len(list_for_count):
                        print("Score: 100%")
                        print("Great! You succeeded in only one try every letter!")
                    elif counter >= (2 * len(list_for_count)):
                        score = 100 / counter
                        print("Score: " + score)
                        if score >= 70:
                            print("Score: " + score)
                            print("Well Done!")
                        elif score > 50:
                            print("Score: " + score)
                            print("Not good")
                        else:
                            print("Score: " + score)
                            print("Too Bad~ Practice more!")


                    break
            print()
            choice = input("Go again? (Y/N) ")


if __name__ == '__main__':
    logging.basicConfig()
    run()
