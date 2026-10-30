# `CAMSmartStyleSettingsPickerView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _waitingOnLoading;
@"UIButton" _continueButton;
@"UIButton" _deselectAllButton;
@"UIView" __pickerView;
@"UIView" __pickerOverlayDisablingView;
```

## Properties

```
@property (T@"UIView",&,N,V__pickerView) _pickerView;
@property (T@"UIView",R,N,V__pickerOverlayDisablingView) _pickerOverlayDisablingView;
@property (T@"UIButton",R,N,V_continueButton) continueButton;
@property (T@"UIButton",R,N,V_deselectAllButton) deselectAllButton;
@property (TB,N,GisWaitingOnLoading,V_waitingOnLoading) waitingOnLoading;
```

## Instance methods

```
-[CAMSmartStyleSettingsPickerView _pickerView];
-[CAMSmartStyleSettingsPickerView continueButton];
-[CAMSmartStyleSettingsPickerView deselectAllButton];
-[CAMSmartStyleSettingsPickerView _setConstraints];
-[CAMSmartStyleSettingsPickerView set_pickerView:];
-[CAMSmartStyleSettingsPickerView _pickerOverlayDisablingView];
-[CAMSmartStyleSettingsPickerView _updateContinueButtonConfiguration];
-[CAMSmartStyleSettingsPickerView _updateDeselectAllButtonConfiguration];
-[CAMSmartStyleSettingsPickerView initWithPHPickerView:];
-[CAMSmartStyleSettingsPickerView isWaitingOnLoading];
-[CAMSmartStyleSettingsPickerView setWaitingOnLoading:];
```
