class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, *args: int):
        if len(args)==1:
            return(args[0].upper())
        if len(args) == 2:
            return args[0]+args[1]



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
