# `DBSFineTuneController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 18 instance variables, 0 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSNumberFormatter" _xyNumberFormatter;
@"NSNumberFormatter" _luminanceNumberFormatter;
@"NSNumber" _measuredWhitePointX;
@"NSNumber" _measuredWhitePointY;
@"NSNumber" _measuredLuminance;
@"NSNumber" _targetWhitePointX;
@"NSNumber" _targetWhitePointY;
@"NSNumber" _targetLuminance;
@"CADisplayPreset" _currentPreset;
@"PSSpecifier" _measuredWhitePointXSpecifier;
@"PSSpecifier" _measuredWhitePointYSpecifier;
@"PSSpecifier" _measuredLuminanceSpecifier;
@"PSSpecifier" _targetWhitePointXSpecifier;
@"PSSpecifier" _targetWhitePointYSpecifier;
@"PSSpecifier" _targetLuminanceSpecifier;
@"PSSpecifier" _restoreDefaultsSpecifier;
@"PSSpecifier" _introductionSpecifier;
@"PSSpecifier" _fineTuneTargetGroupSpecifier;
```

## Instance methods

```
-[DBSFineTuneController init];
-[DBSFineTuneController viewDidLoad];
-[DBSFineTuneController specifiers];
-[DBSFineTuneController userDidTapDone:];
-[DBSFineTuneController addOrRemoveTargetFooter];
-[DBSFineTuneController getMeasuredLuminance:];
-[DBSFineTuneController getMeasuredWhitePointX:];
-[DBSFineTuneController getMeasuredWhitePointY:];
-[DBSFineTuneController getTargetLuminance:];
-[DBSFineTuneController getTargetWhitePointX:];
-[DBSFineTuneController getTargetWhitePointY:];
-[DBSFineTuneController openFineTuneHelpLink];
-[DBSFineTuneController openTargetOutOfRangeHelpLink];
-[DBSFineTuneController restoreDefaults:];
-[DBSFineTuneController setMeasuredLuminance:forSpecifier:];
-[DBSFineTuneController setMeasuredWhitePointX:forSpecifier:];
-[DBSFineTuneController setMeasuredWhitePointY:forSpecifier:];
-[DBSFineTuneController setTargetLuminance:forSpecifier:];
-[DBSFineTuneController setTargetWhitePointX:forSpecifier:];
-[DBSFineTuneController setTargetWhitePointY:forSpecifier:];
-[DBSFineTuneController updateTargetLuminanceValidationRange];
-[DBSFineTuneController updateValidationRanges];
-[DBSFineTuneController userDidTapCancel:];
-[DBSFineTuneController validateUserAdjustment];
```
