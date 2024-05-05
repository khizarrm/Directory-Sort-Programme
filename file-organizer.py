from os import listdir
from os.path import isfile, join
import os
import shutil
import re 

filePath = '/Users/khizarmalik/Downloads'

image_extensions = [
    'jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp',  # JPEG formats
    'png',                                  # Portable Network Graphics
    'gif',                                  # Graphics Interchange Format
    'tiff', 'tif',                          # Tagged Image File Format
    'bmp', 'dib',                           # Bitmap formats
    'webp',                                 # WebP format
    'raw', 'cr2', 'nef', 'orf', 'sr2', 'JPG',# RAW formats for various cameras
    'heic'
]

document_extensions = [
    'doc', 'docx',                        # Microsoft Word documents
    'pdf',                                # Portable Document Format
    'txt',                                # Text files
    'odt',                                # OpenDocument Text
    'rtf',                                # Rich Text Format
    'html', 'htm',                        # HTML files
    'xls', 'xlsx',                        # Microsoft Excel files
    'ods',                                # OpenDocument Spreadsheet
    'ppt', 'pptx',                        # Microsoft PowerPoint presentations
    'odp',                                # OpenDocument Presentation
    'csv',                                # Comma-Separated Values files
    'md',                                 # Markdown files
    'epub',                               # eBook format
]

music_extensions = [
    'mp3',    # MPEG Layer 3 Audio
    'wav',    # Waveform Audio File Format
    'aac',    # Advanced Audio Coding
    'm4a',    # MPEG-4 Audio File
    'flac',   # Free Lossless Audio Codec
    'ogg',    # Ogg Vorbis
    'wma',    # Windows Media Audio
    'mid', 'midi', # Musical Instrument Digital Interface
    'aif', 'aiff', 'aifc', # Audio Interchange File Format
    'opus',   # Opus Audio Codec
    'amr'     # Adaptive Multi-Rate Audio Codec
]

video_extensions = [
    'mp4',     # MPEG-4 Part 14, commonly used for digital video
    'avi',     # Audio Video Interleave, used by many Windows-based applications
    'mov',     # Apple QuickTime Movie
    'wmv',     # Windows Media Video
    'flv',     # Flash Video, used by many online video sites
    'mkv',     # Matroska Video, a container format that can hold multiple audio, video, and subtitle tracks
    'webm',    # WebM, used for HTML5 video
    'mpeg', 'mpg', # MPEG-1 or MPEG-2 video
    'm4v',     # MPEG-4 Video File, similar to MP4
    '3gp',     # 3GPP Multimedia File, used on 3G mobile phones but can also be played on some 2G and 4G phones
    '3g2',     # 3GPP2 Multimedia File, used on some mobile phones for video
    'f4v',     # Flash MP4 Video File, used in Adobe Flash
    'm2ts',    # MPEG-2 Transport Stream, used for high definition Blu-ray and AVCHD
    'mts',     # AVCHD Video File, used by many HD camcorders
    'ts',      # Transport Stream, used for storing video on DVDs
    'vob',     # DVD Video Object, used for storing video and audio on DVDs
]

files = [f for f in listdir(filePath) if isfile(join(filePath, f))]
fileTypes = []
fileDict = []
pattern = re.compile(r'\.([^.]+)$')
for f in files:
    match = pattern.search(f)
    if match and match not in fileTypes:
        extension = match.group(1).lower()
        fileTypes.append(extension)
        sourcePath = filePath + '/' + f
        if extension in image_extensions:
            destPath = '/Users/khizarmalik/Pictures/' + f
            if not os.path.exists(destPath):
                shutil.move(sourcePath, '/Users/khizarmalik/Pictures')
            print("Moved " + f + " to images folder")
        elif extension in document_extensions:
            destPath = '/Users/khizarmalik/Documents/' + f
            if not os.path.exists(destPath):
                shutil.move(sourcePath, '/Users/khizarmalik/Documents')
            print("Moved " + f + " to documents folder")
        elif extension in music_extensions:
            destPath = '/Users/khizarmalik/Music/' + f
            if not os.path.exists(destPath):
                shutil.move(sourcePath, '/Users/khizarmalik/Music')
            print("Moved " + f + " to music folder")
        elif extension in video_extensions:
            destPath = '/Users/khizarmalik/Movies/' + f
            if not os.path.exists(destPath):
                shutil.move(sourcePath, '/Users/khizarmalik/Movies')
            print("Moved " + f + " to movies folder")