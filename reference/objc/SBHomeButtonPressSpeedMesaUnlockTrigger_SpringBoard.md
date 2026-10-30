# `SBHomeButtonPressSpeedMesaUnlockTrigger`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBMesaUnlockTrigger`
- 6 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _slowPressTimer;
B _bioUnlockOccurred;
B _buttonIsDown;
B _fingerIsOn;
B _timerFired;
d _slowPressDuration;
```

## Properties

```
@property (Td,N,V_slowPressDuration) slowPressDuration;
```

## Instance methods

```
-[SBHomeButtonPressSpeedMesaUnlockTrigger screenOff];
-[SBHomeButtonPressSpeedMesaUnlockTrigger succinctDescriptionBuilder];
-[SBHomeButtonPressSpeedMesaUnlockTrigger init];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _timerFired];
-[SBHomeButtonPressSpeedMesaUnlockTrigger dealloc];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _startTimer];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _invalidateTimer];
-[SBHomeButtonPressSpeedMesaUnlockTrigger description];
-[SBHomeButtonPressSpeedMesaUnlockTrigger setSlowPressDuration:];
-[SBHomeButtonPressSpeedMesaUnlockTrigger slowPressDuration];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _evaluateUnlock];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _isTimerRunning];
-[SBHomeButtonPressSpeedMesaUnlockTrigger _isPrimed];
-[SBHomeButtonPressSpeedMesaUnlockTrigger bioUnlock];
-[SBHomeButtonPressSpeedMesaUnlockTrigger fingerOff];
-[SBHomeButtonPressSpeedMesaUnlockTrigger menuButtonDown];
-[SBHomeButtonPressSpeedMesaUnlockTrigger menuButtonUp];
```
