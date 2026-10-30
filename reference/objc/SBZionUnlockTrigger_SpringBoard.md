# `SBZionUnlockTrigger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMesaUnlockTrigger`
- 9 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"<SBBiometricUnlockBehaviorConfigurationDelegate>" _behaviorConfigurationDelegate;
B _hasVisibleContentToReveal;
B _fingerOn;
B _fingerOffSinceWake;
B _lockButtonDown;
@"BSAbsoluteMachTimer" _restToOpenTimer;
@"BSAbsoluteMachTimer" _minTouchIDTimer;
@"BSAbsoluteMachTimer" _liftFingerCoachingTimer;
B _liftFingerCoachingVisible;
```

## Instance methods

```
-[SBZionUnlockTrigger screenOff];
-[SBZionUnlockTrigger succinctDescriptionBuilder];
-[SBZionUnlockTrigger dealloc];
-[SBZionUnlockTrigger screenOn];
-[SBZionUnlockTrigger description];
-[SBZionUnlockTrigger _cancelLiftFingerCoachingTimer];
-[SBZionUnlockTrigger _cancelMinTouchIDTimer];
-[SBZionUnlockTrigger _cancelRestToOpenTimer];
-[SBZionUnlockTrigger _clickToWakeRestToOpenDuration];
-[SBZionUnlockTrigger _evaluateRestToOpenTimer];
-[SBZionUnlockTrigger _hideLiftFingerCoaching];
-[SBZionUnlockTrigger _isRestToOpenAvailable];
-[SBZionUnlockTrigger _shouldStartRestToOpenTimerAfterBioUnlock];
-[SBZionUnlockTrigger _showLiftFingerCoaching];
-[SBZionUnlockTrigger _startLiftFingerCoachingTimer];
-[SBZionUnlockTrigger _startRestToOpenTimer];
-[SBZionUnlockTrigger _startRestToOpenTimerWithDuration:];
-[SBZionUnlockTrigger bioUnlock];
-[SBZionUnlockTrigger fingerOff];
-[SBZionUnlockTrigger fingerOn];
-[SBZionUnlockTrigger initWithUnlockBehaviorConfigurationDelegate:];
-[SBZionUnlockTrigger lockButtonDown];
-[SBZionUnlockTrigger lockButtonUp];
```
