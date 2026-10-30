# `CAMNightModeInstructionLabel`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMInstructionLabel`
- 2 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" __countDownTimer;
d __secondsRemaining;
```

## Properties

```
@property (T@"NSTimer",&,N,V__countDownTimer) _countDownTimer;
@property (Td,N,V__secondsRemaining) _secondsRemaining;
```

## Instance methods

```
-[CAMNightModeInstructionLabel initWithFrame:];
-[CAMNightModeInstructionLabel _updateDisplay];
-[CAMNightModeInstructionLabel cancelCountDown];
-[CAMNightModeInstructionLabel _countDownTimer];
-[CAMNightModeInstructionLabel _secondsRemaining];
-[CAMNightModeInstructionLabel _updateSecondsRemaining];
-[CAMNightModeInstructionLabel _zeroOutSecondsRemainingAndCancelTimer];
-[CAMNightModeInstructionLabel countDownFrom:];
-[CAMNightModeInstructionLabel set_countDownTimer:];
-[CAMNightModeInstructionLabel set_secondsRemaining:];
```
