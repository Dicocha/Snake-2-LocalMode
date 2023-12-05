import os

class FileManager:
    FILE_STORE_SCORES = os.path.join("resources", "Scores.txt")

    def insert(name, score):
        with open(FileManager.FILE_STORE_SCORES, 'a') as file:
            file.write(f"{name} {score}\n")

    @staticmethod
    def read() -> dict:
        scores = {}
        try:
            with open(FileManager.FILE_STORE_SCORES, 'r') as file:
                for line in file:
                    name, score = line.strip().split()
                    scores[name] = int(score)
        except FileNotFoundError:
            pass
        return FileManager.sort(scores)

    @staticmethod
    def sort(pdict) -> dict:
        return dict(sorted(pdict.items(), key = lambda item: item[1]))
