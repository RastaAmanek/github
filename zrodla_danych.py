
# # with open("tekst_3.txt", "w") as file_obj:
# #     file_obj.writelines(["Ala Ty kurwo\n", "jestes jebana szmata\n"])
#
# with open("text.txt", "r") as file_obj:
#     content = file_obj.read()
#
# # with open("text_2.txt", "r") as file_obj:
# #     content_2 = file_obj.read()
#
# with open("text.txt", encoding="utf-8") as file_obj:
#     content = file_obj.read()
#
# print(1)
# print(content)
# # print(content_2)
# print(3)
#
# import locale
# print(locale.getpreferredencoding())

with open("text.txt", encoding="utf-8") as file_obj:
      content = file_obj.read()

words = content.split()
words_count = len(words)
msg = f"Liczba słów w pliku: {words_count}"
print(msg)


with open("result.txt", "w", encoding="utf-8") as file_obj:
    file_obj.write(msg)
