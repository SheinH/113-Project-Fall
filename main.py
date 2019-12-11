from letter_classifier_manual import LetterClassifierManual
from letter_classsifier_machine import LetterClassifierMachine

def main():
    manual_classifier = LetterClassifierManual()
    manual_classifier.classifyLetters()

    machine_classifier = LetterClassifierMachine()
    machine_classifier.train_h_set()

main()