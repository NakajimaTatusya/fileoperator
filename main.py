
import datetime

from rjlib.fileoperator import FileOperator as fo
from rjlib.fileoperator import CodecConvertor as co

if __name__ == "__main__":
    user_path = r"."

    test = fo.get_file_full_path_list(user_path)
    for t in test:
        print("first time   | ", t)

    # 拡張子でフィルタ
    test = fo.get_file_full_path_list(user_path, r".*\.pdf$")
    for t in test:
        print("second times | ", t)

    # ファイル名の先頭一致
    test = fo.get_file_full_path_list(user_path, r"^Windows.*")
    for t in test:
        print("third times  | ", t)

    # 最終更新日でフィルタ
    date_filter = datetime.datetime.strptime("2021-01-08", "%Y-%m-%d")
    test = fo.get_file_full_path_list(user_path, last_update=date_filter)
    for t in test:
        print("fourth times | ", t)

    # ファイル名の中間一致と最終更新日でフィルタ
    date_filter = datetime.datetime.strptime("2021-01-08", "%Y-%m-%d")
    test = fo.get_file_full_path_list(
        user_path, pattern=r"^.*KB.*$", last_update=date_filter)
    for t in test:
        print("fifth times  | ", t)

    co.convert_char_code("test.txt", "text-utf8.txt", "shift_jis", "utf_8")
