# `SBCaptureHardwareButtonScanningPowerLinkedTimer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 3 instance variables, 5 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _timer;
@"<BSInvalidatable>" _buttonPowerRequest;
B _invalid;
```

## Properties

```
@property (TB,R,N,GisScheduled) scheduled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureHardwareButtonScanningPowerLinkedTimer isScheduled];
-[SBCaptureHardwareButtonScanningPowerLinkedTimer dealloc];
-[SBCaptureHardwareButtonScanningPowerLinkedTimer invalidate];
-[SBCaptureHardwareButtonScanningPowerLinkedTimer _didTimeoutWithHandler:];
-[SBCaptureHardwareButtonScanningPowerLinkedTimer initWithIdentifier:timeout:existingRequest:scanModeResource:handler:];
```
