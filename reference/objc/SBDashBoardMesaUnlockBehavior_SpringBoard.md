# `SBDashBoardMesaUnlockBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBMesaUnlockTriggerDelegate`, `SBBiometricUnlockBehavior`
- 6 instance variables, 9 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"SBMesaUnlockFailureCounter" _failureCounter;
@"CSLockScreenMesaSettings" _mesaSettings;
@"SBHomeHardwareButton" _homeHardwareButton;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
B _didRequestBioLockoutFeedbackForFingerPlacement;
@"SBMesaUnlockTrigger" _trigger;
```

## Properties

```
@property (T@"SBHomeHardwareButton",&,N,G_getHomeHardwareButton,S_setHomeHardwareButton:,V_homeHardwareButton) homeHardwareButton;
@property (T@"SBMesaUnlockFailureCounter",&,N,G_getFailureCounter,S_setFailureCounter:,V_failureCounter) failureCounter;
@property (T@"SBMesaUnlockTrigger",&,N,G_trigger,S_setTrigger:,V_trigger) trigger;
@property (T@"CSLockScreenMesaSettings",R,N,G_mesaSettings,V_mesaSettings) mesaSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
```

## Instance methods

```
-[SBDashBoardMesaUnlockBehavior screenOff];
-[SBDashBoardMesaUnlockBehavior setAuthenticated:];
-[SBDashBoardMesaUnlockBehavior succinctDescriptionBuilder];
-[SBDashBoardMesaUnlockBehavior descriptionWithMultilinePrefix:];
-[SBDashBoardMesaUnlockBehavior succinctDescription];
-[SBDashBoardMesaUnlockBehavior screenOn];
-[SBDashBoardMesaUnlockBehavior fingerPresenceDidChange:];
-[SBDashBoardMesaUnlockBehavior _trigger];
-[SBDashBoardMesaUnlockBehavior biometricUnlockBehaviorDelegate];
-[SBDashBoardMesaUnlockBehavior description];
-[SBDashBoardMesaUnlockBehavior handleBiometricEvent:];
-[SBDashBoardMesaUnlockBehavior setBiometricUnlockBehaviorDelegate:];
-[SBDashBoardMesaUnlockBehavior descriptionBuilderWithMultilinePrefix:];
-[SBDashBoardMesaUnlockBehavior _isPoseidonPhone];
-[SBDashBoardMesaUnlockBehavior _failureSettingsForFailAttempt:];
-[SBDashBoardMesaUnlockBehavior _failureCounter];
-[SBDashBoardMesaUnlockBehavior _feedbackForBioLockoutEvent];
-[SBDashBoardMesaUnlockBehavior _feedbackForBioUnlockEventThatWasSpontaneous:];
-[SBDashBoardMesaUnlockBehavior _feedbackForFailureSettings:];
-[SBDashBoardMesaUnlockBehavior _feedbackForPasscodeEvent];
-[SBDashBoardMesaUnlockBehavior _getFailureCounter];
-[SBDashBoardMesaUnlockBehavior _getHomeHardwareButton];
-[SBDashBoardMesaUnlockBehavior _handleBioUnlock];
-[SBDashBoardMesaUnlockBehavior _handleMesaFailure];
-[SBDashBoardMesaUnlockBehavior _homeHardwareButton];
-[SBDashBoardMesaUnlockBehavior _mesaSettings];
-[SBDashBoardMesaUnlockBehavior _setFailureCounter:];
-[SBDashBoardMesaUnlockBehavior _setHomeHardwareButton:];
-[SBDashBoardMesaUnlockBehavior _setTrigger:];
-[SBDashBoardMesaUnlockBehavior _shouldHandleAuthenticationEvents];
-[SBDashBoardMesaUnlockBehavior initWithMesaSettings:andUnlockTrigger:];
-[SBDashBoardMesaUnlockBehavior lockButtonDown];
-[SBDashBoardMesaUnlockBehavior lockButtonUp];
-[SBDashBoardMesaUnlockBehavior menuButtonDown];
-[SBDashBoardMesaUnlockBehavior menuButtonUp];
-[SBDashBoardMesaUnlockBehavior mesaUnlockTriggerFired:];
-[SBDashBoardMesaUnlockBehavior significantUserInteractionDidOccur];
```
