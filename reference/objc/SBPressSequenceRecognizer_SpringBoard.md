# `SBPressSequenceRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 18 instance methods, 0 class methods

## Instance variables

```
d _lastPressDownEvent;
d _lastPressUpEvent;
@"BSAbsoluteMachTimer" _watchdogTimer;
@"SBPressTuple" _currentPressTuple;
@"NSMutableArray" _currentSequence;
@"<SBPressSequenceRecognizerDelegate>" _delegate;
@"SBPressSequenceValidator" _validator;
Q _numberOfPresses;
```

## Properties

```
@property (T@"<SBPressSequenceRecognizerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBPressSequenceValidator",R,N,V_validator) validator;
@property (TQ,R,N,V_numberOfPresses) numberOfPresses;
```

## Instance methods

```
-[SBPressSequenceRecognizer _reset];
-[SBPressSequenceRecognizer validator];
-[SBPressSequenceRecognizer init];
-[SBPressSequenceRecognizer dealloc];
-[SBPressSequenceRecognizer _resetWatchdogIfNecessary];
-[SBPressSequenceRecognizer setDelegate:];
-[SBPressSequenceRecognizer delegate];
-[SBPressSequenceRecognizer _complete];
-[SBPressSequenceRecognizer _resetAndNotify];
-[SBPressSequenceRecognizer _watchdogTimeIntervalFromDelay:];
-[SBPressSequenceRecognizer numberOfPresses];
-[SBPressSequenceRecognizer registerPressDownWithTimestamp:];
-[SBPressSequenceRecognizer _handlePressDownWithTimestamp:];
-[SBPressSequenceRecognizer _handlePressUpWithTimestamp:];
-[SBPressSequenceRecognizer _resetAfterDelay:];
-[SBPressSequenceRecognizer initWithValidator:numberOfPresses:];
-[SBPressSequenceRecognizer registerPressUpWithTimestamp:];
-[SBPressSequenceRecognizer resetWithNewValidator:numberOfPresses:];
```
