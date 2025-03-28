import os, shutil, subprocess, requests, zipfile, threading, json, customtkinter as ctk
from tkinter import filedialog
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class DogHubApp(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Dog Hub Launcher")
        self.geometry("600x400")
        self.label = ctk.CTkLabel(self, text="Добро пожаловать в Dog Hub", font=('Arial',
                                                                                 20))
        self.label.pack(pady=20)
        self.game_list = ctk.CTkComboBox(self, values=["Wroom", "The DOGS"], command=(self.update_versions))
        self.game_list.pack(pady=10)
        self.version_list = ctk.CTkComboBox(self)
        self.version_list.pack(pady=10)
        self.download_button = ctk.CTkButton(self, text="Скачать и установить", command=(self.start_download_thread))
        self.download_button.pack(pady=10)
        self.play_button = ctk.CTkButton(self, text="Запустить игру", command=(self.launch_game))
        self.play_button.pack(pady=10)
        self.toggle_log_button = ctk.CTkButton(self, text="Скрыть логи", command=(self.toggle_logs))
        self.toggle_log_button.pack(pady=10)
        self.log_text = ctk.CTkTextbox(self, height=10)
        self.log_text.pack(pady=10, fill="both", expand=True)
        self.logs_visible = True
        self.installed_games_file = "installed_games.json"
        self.game_urls = {'Wroom':{
          'Alpha 1.0.7.2': '"https://github.com/Wroom-Studio/wroom_for_launcher/releases/download/1.0.7.2-alpha/Wroom_Alpha_1.0.7.2_Win.zip"', 
          'Alpha 1.0.8.1': '"https://github.com/Wroom-Studio/wroom_for_launcher/releases/download/1.0.8-alpha/Wroom_Alpha_1.0.8.1_Win.zip"', 
          'Alpha 1.0.9.1': '"https://github.com/Wroom-Studio/wroom_for_launcher/releases/download/1.0.9-alpha/Wroom_Alpha_1.0.9.1_Win.zip"', 
          'Alpha Test 1.0.11.3': '"https://github.com/Wroom-Studio/wroom_for_launcher/releases/download/1.0.11.3-alpha-test/Wroom_Alpha_1.0.11.3_Win.zip"'}, 
         'The DOGS':{
          'Alpha 2.0': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.0-alpha/The_DOGS_Alpha_2.0_Win.zip"', 
          'Alpha 2.1.0': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.1-alpha/The_DOGS_Alpha_2.1.0_Win.zip"', 
          'Alpha 2.2': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.2-alpha/The_DOGS_Alpha_2.2_Win.zip"', 
          'Alpha 2.3': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.3-alpha/The_DOGS_Alpha_2.3_Win.zip"', 
          'Alpha 2.4': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.4-alpha/The_DOGS_Alpha_2.4_Win.zip"', 
          'Alpha 2.5': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.5-alpha/The_DOGS_Alpha_2.5_Win.zip"', 
          'Alpha 2.7': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/2.7-alpha/The_DOGS_Alpha_2.7_Win.zip"', 
          'Alpha 3.0': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/3.0-alpha/The_DOGS_Alpha_3.0_Win.zip"', 
          'Beta 0.5': '"https://github.com/GulyaTV/TheDOGS_for_launcher/releases/download/1.0-beta/The_DOGS_Beta_0.5_Win.zip"'}}
        self.installed_games = self.load_installed_games()
        self.update_versions()

    def log(self, message):
        self.log_text.insert("end", message + "\n")
        self.log_text.see("end")

    def toggle_logs(self):
        if self.logs_visible:
            self.log_text.pack_forget()
            self.toggle_log_button.configure(text="Показать логи")
        else:
            self.log_text.pack(pady=10, fill="both", expand=True)
            self.toggle_log_button.configure(text="Скрыть логи")
        self.logs_visible = not self.logs_visible

    def update_versions(self, event=None):
        game = self.game_list.get()
        if game in self.game_urls:
            versions = list(self.game_urls[game].keys())
            self.version_list.configure(values=versions)
            if versions:
                self.version_list.set(versions[0])

    def load_installed_gamesParse error at or near `ROT_TWO' instruction at offset 38

    def save_installed_games(self):
        with openself.installed_games_file"w" as file:
            json.dump((self.installed_games), file, indent=4)

    def start_download_thread(self):
        thread = threading.Thread(target=(self.download_and_install))
        thread.start()

    def download_and_install(self):
        game = self.game_list.get()
        version = self.version_list.get()
        if game not in self.game_urls or version not in self.game_urls[game]:
            self.log("Выберите игру и версию для скачивания.")
            return
        if game in self.installed_games:
            if version in self.installed_games[game]:
                self.log(f"{game} {version} уже установлена.")
                return
        url = self.game_urls[game][version]
        version_folder = os.path.join(game, version)
        if not os.path.exists(game):
            os.makedirs(game)
        if not os.path.exists(version_folder):
            os.makedirs(version_folder)
        self.log(f"Скачивание {game} {version}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            zip_path = os.path.join(version_folder, f"{version}.zip")
            with openzip_path"wb" as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)

            self.log("Скачивание завершено.")
            self.log("Распаковка...")
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                extracted_path = os.path.join(version_folder, "extracted")
                zip_ref.extractall(extracted_path)
                exe_file = None
                for root, _, files in os.walk(extracted_path):
                    for file in files:
                        if game == "The DOGS" and file in ('Dog Simulator.exe', 'The DOGS.exe') or game == "Wroom" and file == "Wroom.exe":
                            pass
                        exe_file = os.path.join(root, file)
                        break

                else:
                    if exe_file:
                        break
                    if exe_file:
                        final_path = os.path.join(version_folder, os.path.basename(extracted_path))
                        shutil.move(extracted_path, final_path)
                        self.installed_games.setdefault(game, {})[version] = exe_file
                        self.save_installed_games()
                        self.log(f"Найден исполняемый файл: {exe_file}")
                    else:
                        self.log("Исполняемый файл не найден.")

            os.remove(zip_path)
            self.log(f"{game} {version} успешно установлена.")
        except requests.RequestException as e:
            try:
                self.log(f"Ошибка скачивания: {e}")
            finally:
                e = None
                del e

        except zipfile.BadZipFile as e:
            try:
                self.log(f"Ошибка распаковки: {e}")
            finally:
                e = None
                del e

    def launch_game(self):
        game = self.game_list.get()
        version = self.version_list.get()
        if game in self.installed_games and version in self.installed_games[game]:
            exe_path = self.installed_games[game][version]
            self.log(f"Запуск {game} {version} из {exe_path}...")
            try:
                subprocess.Popen(exe_path, shell=True)
            except Exception as e:
                try:
                    self.log(f"Ошибка запуска игры: {e}")
                finally:
                    e = None
                    del e

        else:
            self.log("Игра не установлена. Пожалуйста, скачайте её сначала.")


if __name__ == "__main__":
    app = DogHubApp()
    app.mainloop()
