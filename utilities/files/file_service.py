class FileService:

    @staticmethod
    def write_file_text(dir_path: str, file_name: str, text: str, mode="w+"):
        file = open(dir_path + file_name, mode)
        file.write(text)
        file.close()

    @staticmethod
    def write_file_text_lines(dir_path: str, file_name: str, m_dict: dict, mode="w+"):
        file = open(dir_path + file_name, mode)
        for key in m_dict.keys():
            file.write("{0}:{1}\n".format(key, m_dict[key]))
        file.close()

    @staticmethod
    def read_file_lines(dir_path: str, file_name: str):
        file = open(dir_path + file_name, "r")
        lines = file.readlines()
        file.close()
        return lines
