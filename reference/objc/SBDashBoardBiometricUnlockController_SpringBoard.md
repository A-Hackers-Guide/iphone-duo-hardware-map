# `SBDashBoardBiometricUnlockController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBiometricUnlockBehaviorDelegate`, `SBBiometricUnlockBehaviorConfigurationDelegate`, `CSExternalEventHandling`, `SBBiometricUnlockBehavior`
- 4 instance variables, 7 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"CSCoverSheetViewController" _coverSheetViewController;
@"<SBBiometricUnlockBehaviorConfiguration>" _biometricUnlockBehaviorConfiguration;
@"<SBBiometricUnlockBehavior>" _biometricUnlockBehavior;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
```

## Instance methods

```
-[SBDashBoardBiometricUnlockController setAuthenticated:];
-[SBDashBoardBiometricUnlockController handleEvent:];
-[SBDashBoardBiometricUnlockController wouldHandleButtonEvent:];
-[SBDashBoardBiometricUnlockController succinctDescriptionBuilder];
-[SBDashBoardBiometricUnlockController dealloc];
-[SBDashBoardBiometricUnlockController noteLockButtonUp];
-[SBDashBoardBiometricUnlockController descriptionWithMultilinePrefix:];
-[SBDashBoardBiometricUnlockController biometricUnlockBehavior:requestsFeedback:];
-[SBDashBoardBiometricUnlockController succinctDescription];
-[SBDashBoardBiometricUnlockController hasVisibleContentToReveal];
-[SBDashBoardBiometricUnlockController fingerPresenceDidChange:];
-[SBDashBoardBiometricUnlockController hasBeenDismissedSinceKeybagLockAndAuthenticated];
-[SBDashBoardBiometricUnlockController biometricUnlockBehaviorDelegate];
-[SBDashBoardBiometricUnlockController handleBiometricEvent:];
-[SBDashBoardBiometricUnlockController conformsToCSEventHandling];
-[SBDashBoardBiometricUnlockController coverSheetIdentifier];
-[SBDashBoardBiometricUnlockController noteMenuButtonUp];
-[SBDashBoardBiometricUnlockController biometricUnlockBehavior:requestsUnlock:withFeedback:];
-[SBDashBoardBiometricUnlockController setBiometricUnlockBehaviorDelegate:];
-[SBDashBoardBiometricUnlockController noteMenuButtonDown];
-[SBDashBoardBiometricUnlockController participantState];
-[SBDashBoardBiometricUnlockController descriptionBuilderWithMultilinePrefix:];
-[SBDashBoardBiometricUnlockController resetRestToOpen];
-[SBDashBoardBiometricUnlockController fillRestToOpenWithDuration:];
-[SBDashBoardBiometricUnlockController isLockScreenShowingDefaultContent];
-[SBDashBoardBiometricUnlockController isRestToOpenAvailable];
-[SBDashBoardBiometricUnlockController setLiftAndRestToOpenCoachingVisible:];
-[SBDashBoardBiometricUnlockController startRestToOpenCoachingWithCompletion:];
-[SBDashBoardBiometricUnlockController _mesaUnlockBehavior];
-[SBDashBoardBiometricUnlockController biometricUnlockBehaviorConfigurationDidChange:];
-[SBDashBoardBiometricUnlockController biometricUnlockBehaviorShouldHandleAuthenticationEvents:];
-[SBDashBoardBiometricUnlockController initWithCoverSheetViewController:liftToWakeController:];
-[SBDashBoardBiometricUnlockController lockScreenWakeSource];
-[SBDashBoardBiometricUnlockController noteLockButtonDown];
```
