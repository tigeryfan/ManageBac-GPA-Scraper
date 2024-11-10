### Scrape grades, calculate GPA, and export into Excel!

This Python script automates the process of navigating to each ManageBac class, copying the overall grade, and calculating the GPA manually. This highly customizable script provides a quick way to track your academic progress, and provides valuable insights on how to improve your grade.
## Features
- Automated MB Grade Scraping: Simply pass your cookie value into the `config.toml` file, and the script will automatically scrape grades.
- GPA Calculation: Unweighted GPA is calculated automatically
- Excel Export: All data is exported into an Excel file, providing an easy way to view your progress.
## Setup
**Linux & macOS:**
```shell
git clone https://github.com/tigeryfan/ManageBac-GPA-Scraper.git
cd ManageBac-GPA-Scraper
pip install -r requirements.txt
```

**Windows:**
> [!WARNING]
> Untested as I do not own a Windows machine. PRs welcome!
```shell
git clone https://github.com/tigeryfan/ManageBac-GPA-Scraper.git
cd ManageBac-GPA-Scraper
pip install -r requirements.txt
```

Fill the `config.toml` file with your preferences.
## `mb_cookie`
You may be confused by what to put in `mb_cookie`. Here's a step-by-step guide:
1. Head to your school's MB portal and login if necessary.
2. Open DevTools (Usually F12)
3. At the top of the window that just popped up, click **Storage** (it may be hidden behind the double chevrolets)
4. Under **Cookies**, click your school's MB domain
5. Double click the string of characters to the right of `_managebac_session` and copy the highlighted text
7. Paste that **inside of the double quotes** in `config.toml`

![[get_cookie.png]]![[paste_cookie.png]]

## Usage
After configuring `config.toml`, simply run `main.py`.
```shell
python main.py
```
> [!TIP]
> Some Linux or macOS users may need to use `python3` instead of `python`.

Keep in mind that the ManageBac cookies expire after some time, so if the script fails, follow [these instructions](#`mb_cookie`) again.

## License
MIT License - Copyright (c) 2024 tigeryfan