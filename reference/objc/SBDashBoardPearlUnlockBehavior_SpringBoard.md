# `SBDashBoardPearlUnlockBehavior`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBMesaUnlockTriggerDelegate`, `SBBiometricUnlockBehavior`
- 3 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CSLockScreenPearlSettings" _pearlSettings;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
@"SBMesaUnlockTrigger" _trigger;
```

## Properties

```
@property (T@"SBMesaUnlockTrigger",&,N,G_trigger,S_setTrigger:,V_trigger) trigger;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
```

## Instance methods

```
-[SBDashBoardPearlUnlockBehavior succinctDescriptionBuilder];
-[SBDashBoardPearlUnlockBehavior descriptionWithMultilinePrefix:];
-[SBDashBoardPearlUnlockBehavior succinctDescription];
-[SBDashBoardPearlUnlockBehavior _trigger];
-[SBDashBoardPearlUnlockBehavior biometricUnlockBehaviorDelegate];
-[SBDashBoardPearlUnlockBehavior description];
-[SBDashBoardPearlUnlockBehavior handleBiometricEvent:];
-[SBDashBoardPearlUnlockBehavior setBiometricUnlockBehaviorDelegate:];
-[SBDashBoardPearlUnlockBehavior descriptionBuilderWithMultilinePrefix:];
-[SBDashBoardPearlUnlockBehavior _feedbackForBioUnlockEventThatWasSpontaneous:];
-[SBDashBoardPearlUnlockBehavior _feedbackForFailureSettings:];
-[SBDashBoardPearlUnlockBehavior _feedbackForPasscodeEvent];
-[SBDashBoardPearlUnlockBehavior _handlePearlFailure];
-[SBDashBoardPearlUnlockBehavior _setTrigger:];
-[SBDashBoardPearlUnlockBehavior initWithPearlSettings:andUnlockTrigger:];
-[SBDashBoardPearlUnlockBehavior mesaUnlockTriggerFired:];
```
