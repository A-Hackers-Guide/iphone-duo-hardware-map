# `DBSReferenceAndCalibrationController`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSListController`
- 3 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"PSSpecifier" _proModeSwitchSpecifier;
@"PSSpecifier" _fineTuneSpecifier;
@"PSSpecifier" _autoDimSwitchSpecifier;
```

## Properties

```
@property (T@"PSSpecifier",R,N,V_proModeSwitchSpecifier) proModeSwitchSpecifier;
@property (T@"PSSpecifier",R,N,V_fineTuneSpecifier) fineTuneSpecifier;
@property (T@"PSSpecifier",R,N,V_autoDimSwitchSpecifier) autoDimSwitchSpecifier;
```

## Instance methods

```
-[DBSReferenceAndCalibrationController viewDidLoad];
-[DBSReferenceAndCalibrationController viewWillAppear:];
-[DBSReferenceAndCalibrationController specifiers];
-[DBSReferenceAndCalibrationController setAutoDimEnabled:forSpecifier:];
-[DBSReferenceAndCalibrationController setProModeEnabled:forSpecifier:];
-[DBSReferenceAndCalibrationController autoDimSwitchSpecifier];
-[DBSReferenceAndCalibrationController fineTuneSpecifier];
-[DBSReferenceAndCalibrationController getAutoDimEnabled:];
-[DBSReferenceAndCalibrationController getProModeEnabled];
-[DBSReferenceAndCalibrationController getProModeEnabled:];
-[DBSReferenceAndCalibrationController presentModalFineTuneController];
-[DBSReferenceAndCalibrationController proModeSupported];
-[DBSReferenceAndCalibrationController proModeSwitchSpecifier];
-[DBSReferenceAndCalibrationController setProModeEnabled:];
```
