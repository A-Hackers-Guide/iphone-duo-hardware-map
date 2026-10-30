# `UIKBCadenceMonitor`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIKBRTRecognizerAveragingRuleProtocol`
- 8 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
B _isUserTyping;
f _cadence;
f _confidence;
f _typingAvg;
i _touchCount;
d _gapAvg;
d _prevTouchDown;
@"UIDelayedAction" _touchLogTimer;
```

## Properties

```
@property (TB,N,V_isUserTyping) isUserTyping;
@property (Tf,N,V_cadence) cadence;
@property (Tf,N,V_confidence) confidence;
@property (Tf,N,V_typingAvg) typingAvg;
@property (Td,N,V_gapAvg) gapAvg;
@property (Td,N,V_prevTouchDown) prevTouchDown;
@property (Ti,N,V_touchCount) touchCount;
@property (T@"UIDelayedAction",&,N,V_touchLogTimer) touchLogTimer;
```

## Instance methods

```
-[UIKBCadenceMonitor cadence];
-[UIKBCadenceMonitor init];
-[UIKBCadenceMonitor reset];
-[UIKBCadenceMonitor touchCount];
-[UIKBCadenceMonitor setConfidence:];
-[UIKBCadenceMonitor setCadence:];
-[UIKBCadenceMonitor confidence];
-[UIKBCadenceMonitor addTypingTouchTime:];
-[UIKBCadenceMonitor gapAvg];
-[UIKBCadenceMonitor isUserTyping];
-[UIKBCadenceMonitor logUserTyping:];
-[UIKBCadenceMonitor prevTouchDown];
-[UIKBCadenceMonitor recognizer:confidenceWhenPendingTouchInfo:];
-[UIKBCadenceMonitor recognizer:confidenceWhenSettingTouchInfo:];
-[UIKBCadenceMonitor setGapAvg:];
-[UIKBCadenceMonitor setIsUserTyping:];
-[UIKBCadenceMonitor setPrevTouchDown:];
-[UIKBCadenceMonitor setTouchCount:];
-[UIKBCadenceMonitor setTouchLogTimer:];
-[UIKBCadenceMonitor setTypingAvg:];
-[UIKBCadenceMonitor touchLogTimer];
-[UIKBCadenceMonitor typingAvg];
-[UIKBCadenceMonitor typingCadence:];
-[UIKBCadenceMonitor updateConfidenceWithGap:];
```
