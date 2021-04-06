import codecs
import datetime
import os
import platform
import re


class _ConstantVariables(object):
    PLATFORM_NAME_WINDOWS = "Windows"

    def __setattr__(self, *_):
        raise AttributeError


class FileOperator:
    @staticmethod
    def get_filename_without_extension(path: str):
        """
        拡張子を除いてファイル名を返す
        """
        return os.path.splitext(os.path.basename(path))[0]

    @staticmethod
    def get_dir_without_filename(path: str):
        """
        pathからファイル名を除いてDirectoryパスを返す
        """
        return os.path.dirname(path) + os.sep

    @staticmethod
    def get_file_full_path_list(path: str, pattern: str = r"^.*$", last_update: datetime = None):
        """
        summary:
            対象のディレクトリパスから、ファイルフルパスリストを作成して返す
            ファイル名が正規表現パターンにマッチするもの
            最終更新日が指定された日付を含み未来のもの
        args:
            path: パス
            pattern: 正規表現パターン
            last_update: 最終更新日
        return:
            フルパスLIST
        """
        try:
            _constant = _ConstantVariables()
            _retval = []
            for _f in [__f for __f in os.listdir(path) if os.path.isfile(os.path.join(path, __f))]:
                if re.search(pattern, _f):
                    _fullpath = os.path.join(path, _f)
                    if last_update:
                        if platform.system() == _constant.PLATFORM_NAME_WINDOWS:
                            if datetime.datetime.fromtimestamp(os.path.getmtime(_fullpath)) >= last_update:
                                _retval.append(_fullpath)
                        else:
                            try:
                                _stat = os.stat(_fullpath)
                                if datetime.datetime.fromtimestamp(_stat.st_ctime) >= last_update:
                                    _retval.append(_fullpath)
                            except AttributeError as _ae:
                                raise _ae
                    else:
                        _retval.append(_fullpath)

            _retval.sort()
            return _retval
        except Exception as _e:
            raise _e


class CodecConvertor:
    @staticmethod
    def convert_char_code(src_path: str, dest_path: str, src_codec: str, dest_codec: str):
        """
        src_path 指定のファイルを dest_codec 指定のコーデックに変換する。
        出力ファイルは、dest_path で指定されたパスに出力する。
        python 標準エンコーディング(https://docs.python.org/ja/3.7/library/codecs.html#standard-encodings)
        """
        with codecs.open(src_path, "r", src_codec) as fsrc, codecs.open(dest_path, "w", dest_codec) as fdest:
            for row in fsrc:
                fdest.write(row)
            fdest.flush()
