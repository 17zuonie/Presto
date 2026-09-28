# -*- coding: utf-8 -*-

import os
from enum import Enum
from qfluentwidgets import qconfig, QConfig, ConfigItem, OptionsConfigItem, BoolValidator, OptionsValidator, \
    FolderValidator, RangeConfigItem, RangeValidator, EnumSerializer, ConfigValidator


class BufSize(Enum):
    _32 = "32 MB"
    _64 = "64 MB"
    _128 = "128 MB"
    _256 = "256 MB"
    _512 = "512 MB"
    _1024 = "1 GB"


class OptionalFolderValidator(FolderValidator):
    def correct(self, value):
        if not value:
            return ""
        return super().correct(value)


class Config(QConfig):
    AutoRun = ConfigItem("MainWindow", "AutoRun", True, BoolValidator())
    Notify = ConfigItem("MainWindow", "Notify", True, BoolValidator())
    IsSourceCloud = OptionsConfigItem("MainWindow", "IsSourceCloud", True, BoolValidator())
    ScanCycle = RangeConfigItem("MainWindow", "ScanCycle", 10, RangeValidator(1, 50))
    ConcurrentProcess = ConfigItem("MainWindow", "ConcurrentProcess", 3, RangeValidator(1, 5))
    BufSize = OptionsConfigItem("MainWindow", "BufSize", BufSize._256, OptionsValidator(BufSize),
                                EnumSerializer(BufSize))
    dpiScale = OptionsConfigItem("MainWindow", "DpiScale", "Auto", OptionsValidator([1, 1.25, 1.5, 1.75, 2, "Auto"]),
                                 restart=True)

    sourceFolder = ConfigItem("Folders", "SourceFolder", "", OptionalFolderValidator())
    yuwenFolder = ConfigItem("Folders", "Yuwen", "", OptionalFolderValidator())
    shuxueFolder = ConfigItem("Folders", "Shuxue", "", OptionalFolderValidator())
    yingyuFolder = ConfigItem("Folders", "Yingyu", "", OptionalFolderValidator())
    wuliFolder = ConfigItem("Folders", "Wuli", "", OptionalFolderValidator())
    huaxueFolder = ConfigItem("Folders", "Huaxue", "", OptionalFolderValidator())
    shengwuFolder = ConfigItem("Folders", "Shengwu", "", OptionalFolderValidator())
    zhengzhiFolder = ConfigItem("Folders", "Zhengzhi", "", OptionalFolderValidator())
    lishiFolder = ConfigItem("Folders", "Lishi", "", OptionalFolderValidator())
    diliFolder = ConfigItem("Folders", "Dili", "", OptionalFolderValidator())
    jishuFolder = ConfigItem("Folders", "Jishu", "", OptionalFolderValidator())
    ziliaoFolder = ConfigItem("Folders", "Ziliao", "", OptionalFolderValidator())

    IsSkipEmptyDir = OptionsConfigItem("Filter", "IsSkipEmptyDir", False, BoolValidator())
    IsSizeFilter = OptionsConfigItem("Filter", "IsSizeFilter", False, BoolValidator())
    SizeFilterUnit = OptionsConfigItem("Filter", "SizeFilterUnit", "GB", OptionsValidator(["KB", "MB", "GB"]))
    SizeFilterValue = ConfigItem("Filter", "SizeFilterValue", 1, RangeValidator(1, 1024))
    IsTypeFilter = OptionsConfigItem("Filter", "IsTypeFilter", False, BoolValidator())
    TypeFilterMode = OptionsConfigItem("Filter", "TypeFilterMode", "Exclude", OptionsValidator(["Exclude", "Include"]))
    IsDocument = OptionsConfigItem("Filter", "IsDocument", False, BoolValidator())
    IsPicture = OptionsConfigItem("Filter", "IsPicture", False, BoolValidator())
    IsAudio = OptionsConfigItem("Filter", "IsAudio", False, BoolValidator())
    IsVideo = OptionsConfigItem("Filter", "IsVideo", False, BoolValidator())
    IsApplication = OptionsConfigItem("Filter", "IsApplication", False, BoolValidator())
    IsZipFile = OptionsConfigItem("Filter", "IsZipFile", False, BoolValidator())
    IsCustomType = OptionsConfigItem("Filter", "IsCustomType", False, BoolValidator())
    CustomType = ConfigItem("Filter", "CustomTpe", ".db, .lnk", ConfigValidator())


YEAR = "2026"
VERSION = "v7.6.1"
cfg = Config()
qconfig.load(os.path.join(os.path.expanduser('~'), '.Presto', 'config', 'config.json'), cfg)
