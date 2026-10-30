# `_UIDictationAudioLevelSmoother`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
f _minimumPower;
f _maximumPower;
q _historyLength;
q _samplesSinceLastCleared;
^f _runningPowerLevels;
I _powerPointer;
f _previousLevel;
f _attackVelocity;
f _decayVelocity;
B _usesExponentialCurve;
B _usesAttackAndDecaySpeed;
f _attackSpeed;
f _decaySpeed;
f _baseValue;
f _exponentMultiplier;
```

## Properties

```
@property (TB,R,N,V_usesExponentialCurve) usesExponentialCurve;
@property (TB,R,N,V_usesAttackAndDecaySpeed) usesAttackAndDecaySpeed;
@property (Tf,N,V_minimumPower) minimumPower;
@property (Tf,N,V_maximumPower) maximumPower;
@property (Tf,N,V_attackSpeed) attackSpeed;
@property (Tf,N,V_decaySpeed) decaySpeed;
@property (Tf,N,V_baseValue) baseValue;
@property (Tf,N,V_exponentMultiplier) exponentMultiplier;
```

## Instance methods

```
-[_UIDictationAudioLevelSmoother dealloc];
-[_UIDictationAudioLevelSmoother setAttackSpeed:];
-[_UIDictationAudioLevelSmoother _initWithHistoryLength:];
-[_UIDictationAudioLevelSmoother _updateMedianWithNewValue:];
-[_UIDictationAudioLevelSmoother attackSpeed];
-[_UIDictationAudioLevelSmoother baseValue];
-[_UIDictationAudioLevelSmoother clearHistory];
-[_UIDictationAudioLevelSmoother decaySpeed];
-[_UIDictationAudioLevelSmoother exponentMultiplier];
-[_UIDictationAudioLevelSmoother initWithBaseValue:exponentMultiplier:historyLength:];
-[_UIDictationAudioLevelSmoother initWithMinimumPower:maximumPower:historyLength:];
-[_UIDictationAudioLevelSmoother initWithMinimumPower:maximumPower:historyLength:attackSpeed:decaySpeed:];
-[_UIDictationAudioLevelSmoother maximumPower];
-[_UIDictationAudioLevelSmoother minimumPower];
-[_UIDictationAudioLevelSmoother setBaseValue:];
-[_UIDictationAudioLevelSmoother setDecaySpeed:];
-[_UIDictationAudioLevelSmoother setExponentMultiplier:];
-[_UIDictationAudioLevelSmoother setMaximumPower:];
-[_UIDictationAudioLevelSmoother setMinimumPower:];
-[_UIDictationAudioLevelSmoother smoothedLevelForMicPower:];
-[_UIDictationAudioLevelSmoother usesAttackAndDecaySpeed];
-[_UIDictationAudioLevelSmoother usesExponentialCurve];
```
