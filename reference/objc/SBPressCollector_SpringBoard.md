# `SBPressCollector`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 3 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _hardEndTimer;
@"NSMutableArray" _currentSequence;
@"SBPressTuple" _currentTuple;
d _lastHandledDownEvent;
d _lastHandledUpEvent;
@"<SBPressCollectorDelegate>" _delegate;
d _maxPressDownDuration;
d _maxPressUpDuration;
```

## Properties

```
@property (T@"<SBPressCollectorDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_maxPressDownDuration) maxPressDownDuration;
@property (Td,N,V_maxPressUpDuration) maxPressUpDuration;
```

## Class methods

```
+[SBPressCollector currentTimeStamp];
```

## Instance methods

```
-[SBPressCollector _reset];
-[SBPressCollector init];
-[SBPressCollector dealloc];
-[SBPressCollector setDelegate:];
-[SBPressCollector delegate];
-[SBPressCollector _end];
-[SBPressCollector registerPressDownWithTimeStamp:];
-[SBPressCollector _fireEndTimerWithDelay:isButtonDown:];
-[SBPressCollector _handlePressDownWithTimeStamp:];
-[SBPressCollector _handlePressUpWithTimeStamp:];
-[SBPressCollector _resetTimersIfNecessary];
-[SBPressCollector endCurrentSequence];
-[SBPressCollector maxPressDownDuration];
-[SBPressCollector maxPressUpDuration];
-[SBPressCollector registerPressUpWithTimeStamp:];
-[SBPressCollector setMaxPressDownDuration:];
-[SBPressCollector setMaxPressUpDuration:];
```
