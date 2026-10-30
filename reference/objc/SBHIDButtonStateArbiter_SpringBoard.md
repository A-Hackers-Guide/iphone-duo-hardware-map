# `SBHIDButtonStateArbiter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
Q _previousUpTime;
B _recognizedLongPress;
@"BSAbsoluteMachTimer" _longPressTimer;
@"BSAbsoluteMachTimer" _repeatedPressTimer;
Q _downEventSenderID;
d _longPressTimeoutAtDownEvent;
d _repeatedPressTimeoutAtUpEvent;
d _longPressTimeout;
Q _repeatedPressCount;
Q _maximumRepeatedPressCount;
d _repeatedPressTimeout;
q _pressSequence;
Q _downTime;
Q _repeatedPressInitialDownTime;
@"<SBHIDButtonStateDelegate>" _delegate;
```

## Properties

```
@property (TB,R,N,GisLongPressDisabled) longPressDisabled;
@property (Td,N,V_longPressTimeout) longPressTimeout;
@property (TB,R,N,GisRepeatedPressDisabled) repeatedPressDisabled;
@property (TQ,R,N,V_repeatedPressCount) repeatedPressCount;
@property (TQ,N,V_maximumRepeatedPressCount) maximumRepeatedPressCount;
@property (Td,N,V_repeatedPressTimeout) repeatedPressTimeout;
@property (Tq,R,N,V_pressSequence) pressSequence;
@property (TQ,R,N,V_downTime) downTime;
@property (TQ,R,N,V_repeatedPressInitialDownTime) repeatedPressInitialDownTime;
@property (T@"<SBHIDButtonStateDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBHIDButtonStateArbiter init];
-[SBHIDButtonStateArbiter dealloc];
-[SBHIDButtonStateArbiter reset];
-[SBHIDButtonStateArbiter setDelegate:];
-[SBHIDButtonStateArbiter delegate];
-[SBHIDButtonStateArbiter setLongPressTimeout:];
-[SBHIDButtonStateArbiter longPressTimeout];
-[SBHIDButtonStateArbiter processEvent:];
-[SBHIDButtonStateArbiter downTime];
-[SBHIDButtonStateArbiter isLongPressDisabled];
-[SBHIDButtonStateArbiter isRepeatedPressDisabled];
-[SBHIDButtonStateArbiter maximumRepeatedPressCount];
-[SBHIDButtonStateArbiter pressSequence];
-[SBHIDButtonStateArbiter repeatedPressCount];
-[SBHIDButtonStateArbiter repeatedPressInitialDownTime];
-[SBHIDButtonStateArbiter repeatedPressTimeout];
-[SBHIDButtonStateArbiter setMaximumRepeatedPressCount:];
-[SBHIDButtonStateArbiter setRepeatedPressTimeout:];
```
