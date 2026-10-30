# `SBBiometricEventLogger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIBiometricResourceObserver`
- 7 instance variables, 7 properties, 28 instance methods, 3 class methods

## Instance variables

```
@"BiometricKit" _biometricKit;
B _isScreenOn;
B _passcodeSuccessAfterBioFailureTriggerArmed;
@"<SBUIBiometricResource>" _biometricResource;
B _keybagUnlocked;
B _fingerOn;
B _fingerOnWithScreenOn;
```

## Properties

```
@property (TB,N,V_keybagUnlocked) keybagUnlocked;
@property (TB,N,V_fingerOn) fingerOn;
@property (TB,N,V_fingerOnWithScreenOn) fingerOnWithScreenOn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBBiometricEventLogger sharedInstance];
+[SBBiometricEventLogger logEvent:];
+[SBBiometricEventLogger logClass:code:];
```

## Instance methods

```
-[SBBiometricEventLogger init];
-[SBBiometricEventLogger _clearEverything];
-[SBBiometricEventLogger timestampEvent:];
-[SBBiometricEventLogger biometricResource:observeEvent:];
-[SBBiometricEventLogger _authRequestCompleted:];
-[SBBiometricEventLogger _backlightLevelChanged:];
-[SBBiometricEventLogger _biometricAuthenticationFailed];
-[SBBiometricEventLogger _biometricAuthenticationSucceeded];
-[SBBiometricEventLogger _coversheetSwipedForDismissal:];
-[SBBiometricEventLogger _fingerOn:];
-[SBBiometricEventLogger _keybagBioUnlock:];
-[SBBiometricEventLogger _machTimeInMilliseconds];
-[SBBiometricEventLogger _passcodeAuthenticationSucceeded];
-[SBBiometricEventLogger _passcodePromptCancelled:];
-[SBBiometricEventLogger _passcodeViewTransitionedToPasscode:];
-[SBBiometricEventLogger _prearmMatch:];
-[SBBiometricEventLogger _resetPasscodeStateMachine];
-[SBBiometricEventLogger _screenTurnedOn:];
-[SBBiometricEventLogger _shouldSyslogTimestamps];
-[SBBiometricEventLogger _systemDidWakeFromSleep:];
-[SBBiometricEventLogger _tryAgain:];
-[SBBiometricEventLogger _unlockAnimationWillStart:];
-[SBBiometricEventLogger fingerOn];
-[SBBiometricEventLogger fingerOnWithScreenOn];
-[SBBiometricEventLogger keybagUnlocked];
-[SBBiometricEventLogger setFingerOn:];
-[SBBiometricEventLogger setFingerOnWithScreenOn:];
-[SBBiometricEventLogger setKeybagUnlocked:];
```
