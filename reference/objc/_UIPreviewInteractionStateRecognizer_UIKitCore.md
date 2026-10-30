# `_UIPreviewInteractionStateRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _deepPressCount;
d _smoothedForce;
d _maximumForce;
d _previousEffectiveTouchForce;
d _timeMark;
d _currentTime;
d _previousTime;
d _popOffsetInitial;
d _popOffsetLongterm;
d _popOffsetDecayAlpha;
d _lowpassForceAlpha;
d _popDecayingOffset;
d _popReductionForce;
d _progressToStrongThreshold;
B _allowsPopOffsetDecay;
d _popForceReductionThreshold;
d _popAlwaysThreshold;
d _highPopThreshold;
d _previousPopThreshold;
d _saturationForce;
d _revealThreshold;
d _standardThreshold;
d _strongThreshold;
d _hintAndPeekInterval;
d _hintReductionForce;
d _actualHintForce;
d _actualPeekForce;
d _actualPopForce;
d _actualHintTime;
d _actualPeekTime;
d _actualPopTime;
B _shouldDelayReveal;
q _currentState;
d _minimumPreviewDuration;
d _currentTouchForce;
```

## Properties

```
@property (Tq,N,V_currentState) currentState;
@property (Td,N,V_currentTouchForce) currentTouchForce;
@property (Td,R,D,N) velocity;
@property (Td,N,V_minimumPreviewDuration) minimumPreviewDuration;
@property (TB,N,V_shouldDelayReveal) shouldDelayReveal;
```

## Instance methods

```
-[_UIPreviewInteractionStateRecognizer init];
-[_UIPreviewInteractionStateRecognizer dealloc];
-[_UIPreviewInteractionStateRecognizer reset];
-[_UIPreviewInteractionStateRecognizer velocity];
-[_UIPreviewInteractionStateRecognizer setCurrentState:];
-[_UIPreviewInteractionStateRecognizer description];
-[_UIPreviewInteractionStateRecognizer currentState];
-[_UIPreviewInteractionStateRecognizer _accessibilityForceSensitivityChanged:];
-[_UIPreviewInteractionStateRecognizer _currentTouchForceMultiplier];
-[_UIPreviewInteractionStateRecognizer _denormalizedTouchForceValue:];
-[_UIPreviewInteractionStateRecognizer _normalizedTouchForceValue:];
-[_UIPreviewInteractionStateRecognizer _thresholdForForceLevel:];
-[_UIPreviewInteractionStateRecognizer currentProgressToState:];
-[_UIPreviewInteractionStateRecognizer currentTouchForce];
-[_UIPreviewInteractionStateRecognizer evaluateWithTouchForce:atTimestamp:withCentroidAtLocation:];
-[_UIPreviewInteractionStateRecognizer minimumPreviewDuration];
-[_UIPreviewInteractionStateRecognizer setCurrentTouchForce:];
-[_UIPreviewInteractionStateRecognizer setMinimumPreviewDuration:];
-[_UIPreviewInteractionStateRecognizer setShouldDelayReveal:];
-[_UIPreviewInteractionStateRecognizer shouldDelayReveal];
```
