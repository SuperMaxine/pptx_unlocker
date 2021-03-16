# pptx_unlocker

<img src="F:\TyporaImages\README\powerpoint.png" alt="powerpoint" style="zoom: 25%;" />

[![GitHub issues](https://img.shields.io/github/issues/SuperMaxine/pptx_unlocker)](https://github.com/SuperMaxine/pptx_unlocker/issues)

[![GitHub forks](https://img.shields.io/github/forks/SuperMaxine/pptx_unlocker)](https://github.com/SuperMaxine/pptx_unlocker/network)

[![GitHub stars](https://img.shields.io/github/stars/SuperMaxine/pptx_unlocker)](https://github.com/SuperMaxine/pptx_unlocker/stargazers)

[![GitHub license](https://img.shields.io/github/license/SuperMaxine/pptx_unlocker)](https://github.com/SuperMaxine/pptx_unlocker)

This is an open source project to unlock a pptx file encrypted with a password and make it editable

## Effect Preview

**Before**

![image-20210316223726683](F:\TyporaImages\README\image-20210316223726683.png)

**After**

![image-20210316223918548](F:\TyporaImages\README\image-20210316223918548.png)

## How to use

### For quick use or beginners

Please download the executable file directly from the [release](https://github.com/SuperMaxine/pptx_unlocker/releases/tag/pptx_unlocker) link, which is available for 64-bit Windows hosts

1. Double click on the .exe file to open the application, it is a single file application, so you can open it anywhere you want
   ![image-20210316225319051](F:\TyporaImages\README\image-20210316225319051.png)

2. Drag your `.pptx` files into the newly opened window.
   ![image-20210316225746602](F:\TyporaImages\README\image-20210316225746602.png)
3. Waiting for the processing
   ![image-20210316225858692](F:\TyporaImages\README\image-20210316225858692.png)
4. And BOOM!! The files are all unlock, enjoy!
   ![image-20210316225947592](F:\TyporaImages\README\image-20210316225947592.png)

### For advanced users or Linux/MacOS users

1. Use the command `git clone https://github.com/SuperMaxine/pptx_unlocker.git` to clone the project locally

2. Go to the project directory and run `pip install -r requirements.txt` to install the dependencies, the main ones are as follows:

   ```txt
   pyinstaller==4.2
   PyQt5==5.15.2
   pyqt5-tools==5.15.2.3.0.2
   (optional)pyinstaller==4.2
   ```

3. Theoretically you can run `python3 main.py` to open the GUI application, be aware that the python version needs to be as close to 3.8 as possible, if you encounter any problems feel free to send me an issue