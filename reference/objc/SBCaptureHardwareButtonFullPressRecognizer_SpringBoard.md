# `SBCaptureHardwareButtonFullPressRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIAbstractDynamicButtonGestureRecognizer`
- 4 instance variables, 0 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _lastDownTimestamp;
Q _lastUpTimestamp;
B _isCaptureButtonFullyPressed;
B _isCaptureButtonSourceAccessibility;
```

## Instance methods

```
-[SBCaptureHardwareButtonFullPressRecognizer _endIfNeeded];
-[SBCaptureHardwareButtonFullPressRecognizer _shouldReceiveDynamicButton:];
-[SBCaptureHardwareButtonFullPressRecognizer isCaptureButtonSourceAccessibility];
-[SBCaptureHardwareButtonFullPressRecognizer _cancelIfNeeded];
-[SBCaptureHardwareButtonFullPressRecognizer _dynamicButtonsCancelled:withEvent:];
-[SBCaptureHardwareButtonFullPressRecognizer reset];
-[SBCaptureHardwareButtonFullPressRecognizer initWithTarget:action:];
-[SBCaptureHardwareButtonFullPressRecognizer isCaptureButtonFullyPressed];
-[SBCaptureHardwareButtonFullPressRecognizer _beginIfNeeded];
-[SBCaptureHardwareButtonFullPressRecognizer _dynamicButtonsEnded:withEvent:];
-[SBCaptureHardwareButtonFullPressRecognizer pressUpTimestamp];
-[SBCaptureHardwareButtonFullPressRecognizer _dynamicButtonsBegan:withEvent:];
-[SBCaptureHardwareButtonFullPressRecognizer _dynamicButtonsChanged:withEvent:];
-[SBCaptureHardwareButtonFullPressRecognizer pressDownTimestamp];
```
