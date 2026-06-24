# 09_practice_board.py
# 학습일: 2026-06-24
# 개념: OOP 총정리 - 추상클래스, 클래스변수, @property, 상속, super(),
# isinstance(), @staticmethod, @classmethod, 매직메서드

from abc import ABC, abstractmethod

class Post(ABC):

    post_count = 0  # 클래스 변수

    def __init__(self, title: str, content: str, author: str):
        self._title = title
        self.content = content
        self.author = author
        Post.post_count += 1

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("제목은 비어 있을 수 없습니다.")
        self._title = value
        
    @abstractmethod
    def get_type(self):
        pass

    @staticmethod
    def valid_title(title: str) -> bool:
        return bool(title)
    
    def __str__(self):
        return f"[{self.get_type()}] {self._title} - {self.author}"

class Article(Post):
    def get_type(self) -> str:
        return "Article"
    
    @classmethod
    def from_string(cls, data: str) -> "Article":
        title, content, author = data.split(",")
        return cls(title, content, author)
    
class Notice(Post):
    def get_type(self) -> str:
        return "Notice"
    
# 실행 코드
a1 = Article("파이썬 공부법", "열심히 하면 됩니다", "김철수")
a2 = Article("취업 후기", "합격했습니다", "이영희")
n1 = Notice("공지사항", "내일 휴무입니다", "관리자")

print(Post.post_count)              # 3
print(a1)                           # [Article] 파이썬 공부법 - 김철수
print(isinstance(a1, Post))         # True
print(isinstance(n1, Notice))       # True

a3 = Article.from_string("제목,내용,작성자")
print(a3.title)                     # 제목

print(Post.valid_title("제목"))     # True
print(Post.valid_title(""))         # False