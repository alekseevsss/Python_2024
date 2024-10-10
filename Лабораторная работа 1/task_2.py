# TODO Найдите количество книг, которое можно разместить на дискете
disk_size_mb=1.44
disk_size_bytes=disk_size_mb*1024*1024
number_of_book_pages=100
number_of_string_on_page=50
number_of_symbols_in_string=25
symbol_size_byte=4

number_of_books=int(disk_size_bytes//(number_of_book_pages*number_of_string_on_page*number_of_symbols_in_string*symbol_size_byte))
print("Количество книг, помещающихся на дискету:", number_of_books)
