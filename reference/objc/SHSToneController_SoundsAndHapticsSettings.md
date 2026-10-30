# `SHSToneController`

- Image: [`/System/Library/PrivateFrameworks/Settings/SoundsAndHapticsSettings.framework/SoundsAndHapticsSettings`](../userland/System__Library__PrivateFrameworks__Settings__SoundsAndHapticsSettings.framework__SoundsAndHapticsSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PSViewController`
- Protocols: `TKTonePickerViewControllerDelegate`, `TKVibrationPickerViewControllerDelegate`
- 2 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"TKTonePickerViewController" _tonePickerViewController;
@"TKVibrationPickerViewController" _vibrationPickerViewController;
```

## Properties

```
@property (T@"TKTonePickerViewController",&,N,V_tonePickerViewController) tonePickerViewController;
@property (T@"TKVibrationPickerViewController",&,N,V_vibrationPickerViewController) vibrationPickerViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SHSToneController _handleAlertOverridePolicyDidChangeNotification:];
-[SHSToneController init];
-[SHSToneController dealloc];
-[SHSToneController viewDidLoad];
-[SHSToneController setSpecifier:];
-[SHSToneController viewDidAppear:];
-[SHSToneController _defaultToneIdentifierForTonePickerWithAlertType:topic:];
-[SHSToneController _defaultVibrationIdentifierForVibrationPickerWithAlertType:topic:];
-[SHSToneController _insertTonePickerView];
-[SHSToneController _updateReloadSpecifierInParentController];
-[SHSToneController setTonePickerViewController:];
-[SHSToneController setVibrationPickerViewController:];
-[SHSToneController tonePickerViewController];
-[SHSToneController tonePickerViewController:didDismissVibrationPickerViewController:];
-[SHSToneController tonePickerViewController:requestsPresentingToneClassicsViewController:animated:];
-[SHSToneController tonePickerViewController:requestsPresentingVibrationPickerViewController:animated:];
-[SHSToneController tonePickerViewController:selectedToneWithIdentifier:];
-[SHSToneController tonePickerViewController:willPresentVibrationPickerViewController:];
-[SHSToneController vibrationPickerViewController];
-[SHSToneController vibrationPickerViewController:selectedVibrationWithIdentifier:];
```
