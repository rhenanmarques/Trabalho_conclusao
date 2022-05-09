import os

class DataScore:
    def hiScore(self, newScore=0):
        if not os.path.isfile('data.txt'):
            file = open('data.txt', 'wt+')
            file.write("0" + "\n")
            file.close()
            return 0
        else:
            file = open("data.txt", "r")
            if file.readline():
                file.seek(0)
                score = int(file.readline().strip())
                file.close()
                if score < newScore:
                    file = open("data.txt", "w")
                    file.write(str(newScore))
                    file.close()
                return score
