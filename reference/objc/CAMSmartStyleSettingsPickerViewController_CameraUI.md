# `CAMSmartStyleSettingsPickerViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PHPickerViewControllerDelegate`, `PHPickerViewControllerDelegate_Private`
- 5 instance variables, 13 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"<CAMSmartStyleSettingsPickerViewControllerDelegate>" _delegate;
@"NSArray" _selectedAssetIdentifiers;
@"NSArray" _initialSelectedAssetIdentifiers;
@"PHPickerViewController" __phPicker;
q __styleType;
```

## Properties

```
@property (T@"PHPickerViewController",R,N,V__phPicker) _phPicker;
@property (T@"NSArray",&,N,V_selectedAssetIdentifiers) selectedAssetIdentifiers;
@property (Tq,R,N,V__styleType) _styleType;
@property (T@"CAMSmartStyleSettingsPickerView",R,N) _pickerView;
@property (T@"UIButton",R,N) _continueButton;
@property (T@"UIButton",R,N) _deselectAllButton;
@property (T@"<CAMSmartStyleSettingsPickerViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSArray",R,N,V_initialSelectedAssetIdentifiers) initialSelectedAssetIdentifiers;
@property (TB,N,GisWaitingOnLoading) waitingOnLoading;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSmartStyleSettingsPickerViewController selectedAssetIdentifiers];
-[CAMSmartStyleSettingsPickerViewController setSelectedAssetIdentifiers:];
-[CAMSmartStyleSettingsPickerViewController picker:didFinishPicking:];
-[CAMSmartStyleSettingsPickerViewController setDelegate:];
-[CAMSmartStyleSettingsPickerViewController loadView];
-[CAMSmartStyleSettingsPickerViewController delegate];
-[CAMSmartStyleSettingsPickerViewController _pickerView];
-[CAMSmartStyleSettingsPickerViewController _handleContinueButton:];
-[CAMSmartStyleSettingsPickerViewController _pickerDidPerformCancelAction:];
-[CAMSmartStyleSettingsPickerViewController _pickerDidPerformConfirmationAction:];
-[CAMSmartStyleSettingsPickerViewController _continueButton];
-[CAMSmartStyleSettingsPickerViewController initWithPickerConfiguration:selectedAssetIdentifiers:styleType:];
-[CAMSmartStyleSettingsPickerViewController initialSelectedAssetIdentifiers];
-[CAMSmartStyleSettingsPickerViewController _deselectAllButton];
-[CAMSmartStyleSettingsPickerViewController _handleDeselectAllButton:];
-[CAMSmartStyleSettingsPickerViewController _phPicker];
-[CAMSmartStyleSettingsPickerViewController _styleType];
-[CAMSmartStyleSettingsPickerViewController _updateButtonsEnablementState];
-[CAMSmartStyleSettingsPickerViewController isWaitingOnLoading];
-[CAMSmartStyleSettingsPickerViewController setWaitingOnLoading:];
```
