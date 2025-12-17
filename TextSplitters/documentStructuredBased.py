## used for different strucutres of documents like that of HTML, JSON, etc
# here also we use 'RecursiveCharacterTextSplitter' just like TextStructuredBased, the only difference
## is that we use 'seprators' in case of 'DocumentStructuredBased' text splitter

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
text = """

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def getName(self):
        return self.name
    def isPassing(self):
        return self.grade>=6
    
    ## example usage -
student1 = Student("Khushi",'A++')
print(student1.getName())

"""

## initializing the splitter - for DocumentStructuredBased type of text splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 10,
    chunk_overlap = 5
)

chunks = splitter.split_text(text=text)
print(len(chunks))
print(chunks[0])
print(chunks[1])
print(chunks[2])