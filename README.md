# OneNoteFilenameParser
During analysis of a malicious OneNote file I observed that the filename & path where the file originated from are saved within the OneNote file:

![image](https://user-images.githubusercontent.com/87302600/220171074-0d613834-296d-4e42-baff-26e2380584bc.png)

I created a POC python script that will extract this data and show it on the commandline.

# Usage
python3 onenoteparser.py filename.one [weight]

# Methodology
This data is stored in a block of bytes `00 00 00 00 FF FF FF FF FF FF FF FF 00 00 00 00` & `00 00 00 00 FF FF FF FF FF FF FF FF 00 00 00 00`. The script will take these snippets and translate it to readable text. whilst doing so it will also attmept to remove as many false positives as possible.

# Weight
The implemented weight system is used to limit false positives, the default is 500. The higher you go, the more results will be shown.
