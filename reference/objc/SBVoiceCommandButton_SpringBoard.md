# `SBVoiceCommandButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDButtonStateDelegate`, `SBHardwareButtonColluding`
- 4 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isLongPressRecognized;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBHIDButtonStateArbiter" _buttonArbiter;
@"SBSiriHardwareButtonInteraction" _siriHardwareButtonInteraction;
```

## Properties

```
@property (T@"SBHIDButtonStateArbiter",&,N,V_buttonArbiter) buttonArbiter;
@property (T@"SBSiriHardwareButtonInteraction",&,N,V_siriHardwareButtonInteraction) siriHardwareButtonInteraction;
@property (TB,N,V_isLongPressRecognized) isLongPressRecognized;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBVoiceCommandButton init];
-[SBVoiceCommandButton hardwareButtonIdentifier];
-[SBVoiceCommandButton cancelHardwareButtonPress];
-[SBVoiceCommandButton performActionsForButtonUp:];
-[SBVoiceCommandButton performActionsForButtonDown:];
-[SBVoiceCommandButton setHardwareButtonCoordinator:];
-[SBVoiceCommandButton performActionsForButtonLongPress:];
-[SBVoiceCommandButton hardwareButtonCoordinator];
-[SBVoiceCommandButton handleButtonEvent:];
-[SBVoiceCommandButton _isPermittedToBegin];
-[SBVoiceCommandButton buttonArbiter];
-[SBVoiceCommandButton isLongPressRecognized];
-[SBVoiceCommandButton setButtonArbiter:];
-[SBVoiceCommandButton setIsLongPressRecognized:];
-[SBVoiceCommandButton setSiriHardwareButtonInteraction:];
-[SBVoiceCommandButton siriHardwareButtonInteraction];
```
