# `SHSDualSIMToneController`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SHSToneController`
- Protocols: `TKTonePickerViewControllerDelegate`, `TKVibrationPickerViewControllerDelegate`
- 3 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isDefaultSIMLineController;
@"NSString" _topic;
@"SHSDualSIMToneTitleView" _titleView;
```

## Properties

```
@property (T@"NSString",&,N,V_topic) topic;
@property (T@"SHSDualSIMToneTitleView",&,N,V_titleView) titleView;
@property (TB,N,V_isDefaultSIMLineController) isDefaultSIMLineController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SHSDualSIMToneController setTitleView:];
-[SHSDualSIMToneController setTopic:];
-[SHSDualSIMToneController init];
-[SHSDualSIMToneController topic];
-[SHSDualSIMToneController setSpecifier:];
-[SHSDualSIMToneController titleView];
-[SHSDualSIMToneController _defaultVibrationIdentifierForVibrationPickerWithAlertType:topic:];
-[SHSDualSIMToneController _updateReloadSpecifierInParentController];
-[SHSDualSIMToneController isDefaultSIMLineController];
-[SHSDualSIMToneController setIsDefaultSIMLineController:];
-[SHSDualSIMToneController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:];
-[SHSDualSIMToneController tonePickerViewController:requestsPresentingVibrationPickerViewController:animated:];
-[SHSDualSIMToneController tonePickerViewController:selectedToneWithIdentifier:];
-[SHSDualSIMToneController vibrationPickerViewController:selectedVibrationWithIdentifier:];
```
