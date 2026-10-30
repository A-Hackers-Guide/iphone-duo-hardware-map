# `SBDashBoardMesaUnlockBehaviorConfiguration`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBLiftToWakeObserver`, `SBBiometricUnlockBehaviorConfiguration`
- 5 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<SBBiometricUnlockBehaviorConfigurationDelegate>" _delegate;
@"SBLiftToWakeController" _liftToWakeController;
@"CSLockScreenSettings" _prototypeSettings;
@"SBUIBiometricResource" _biometricResource;
# _currentTriggerClass;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorConfigurationDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBDashBoardMesaUnlockBehaviorConfiguration dealloc];
-[SBDashBoardMesaUnlockBehaviorConfiguration setDelegate:];
-[SBDashBoardMesaUnlockBehaviorConfiguration delegate];
-[SBDashBoardMesaUnlockBehaviorConfiguration _accessibilityOptionsChanged:];
-[SBDashBoardMesaUnlockBehaviorConfiguration _currentUnlockTriggerClass];
-[SBDashBoardMesaUnlockBehaviorConfiguration _evaluateTriggerClass];
-[SBDashBoardMesaUnlockBehaviorConfiguration _expectedTriggerClassIncludingAccessibility:];
-[SBDashBoardMesaUnlockBehaviorConfiguration _isAccessibilityRestingUnlockPreferenceEnabled];
-[SBDashBoardMesaUnlockBehaviorConfiguration _liftToWakeController];
-[SBDashBoardMesaUnlockBehaviorConfiguration _setLiftToWakeController:];
-[SBDashBoardMesaUnlockBehaviorConfiguration _unlockTriggerWithClass:];
-[SBDashBoardMesaUnlockBehaviorConfiguration initWithLiftToWakeController:biometricResource:lockScreenPrototypeSettings:];
-[SBDashBoardMesaUnlockBehaviorConfiguration initWithLiftToWakeController:biometricResource:lockScreenPrototypeSettings:evaluateTriggerClass:];
-[SBDashBoardMesaUnlockBehaviorConfiguration liftToWakeControllerEnablementDidChange:];
-[SBDashBoardMesaUnlockBehaviorConfiguration newBehaviorForCurrentConfiguration];
```
