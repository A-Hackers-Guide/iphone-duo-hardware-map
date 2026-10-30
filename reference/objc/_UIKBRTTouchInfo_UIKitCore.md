# `_UIKBRTTouchInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKBRTObject`
- 12 instance variables, 14 properties, 25 instance methods, 4 class methods

## Instance variables

```
c _currentTouchState;
c _preRuleTouchState;
d _originalTimestamp;
d _maximumRadius;
d _currentTimestamp;
d _originalZGradient;
d _currentZGradient;
@ _touchIdentifier;
@"_UIKBRTTimerBlock" _timer;
@"NSObject<OS_dispatch_queue>" _timerQueue;
{CGPoint="x"d"y"d} _originalTouchPoint;
{CGPoint="x"d"y"d} _currentTouchPoint;
```

## Properties

```
@property (T@"_UIKBRTTimerBlock",R,N,V_timer) timer;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_timerQueue) timerQueue;
@property (T@"_UIKBRTTouchInfo",R,N) previousTouch;
@property (T@"_UIKBRTTouchInfo",R,N) nextTouch;
@property (Td,R,N,V_originalTimestamp) originalTimestamp;
@property (T{CGPoint=dd},R,N,V_originalTouchPoint) originalTouchPoint;
@property (T{CGPoint=dd},R,N,V_currentTouchPoint) currentTouchPoint;
@property (Td,R,N,V_maximumRadius) maximumRadius;
@property (Td,R,N,V_currentTimestamp) currentTimestamp;
@property (Td,R,N,V_originalZGradient) originalZGradient;
@property (Td,R,N,V_currentZGradient) currentZGradient;
@property (Tc,N,V_currentTouchState) currentTouchState;
@property (Tc,N,V_preRuleTouchState) preRuleTouchState;
@property (T@,R,N,V_touchIdentifier) touchIdentifier;
```

## Class methods

```
+[_UIKBRTTouchInfo createTouchInfoForTouch:withIdentifier:canLogTouch:];
+[_UIKBRTTouchInfo setTouchInfo:forIdentifier:];
+[_UIKBRTTouchInfo touchDict];
+[_UIKBRTTouchInfo touchInfoForTouch:withIdentifier:];
```

## Instance methods

```
-[_UIKBRTTouchInfo cleanup];
-[_UIKBRTTouchInfo touchIdentifier];
-[_UIKBRTTouchInfo currentTimestamp];
-[_UIKBRTTouchInfo timer];
-[_UIKBRTTouchInfo dealloc];
-[_UIKBRTTouchInfo originalTimestamp];
-[_UIKBRTTouchInfo originalTouchPoint];
-[_UIKBRTTouchInfo timerQueue];
-[_UIKBRTTouchInfo invalidateTimer];
-[_UIKBRTTouchInfo currentTouchPoint];
-[_UIKBRTTouchInfo currentTouchState];
-[_UIKBRTTouchInfo currentZGradient];
-[_UIKBRTTouchInfo fireTimerNow];
-[_UIKBRTTouchInfo initWithTouch:withIdentifier:canLogTouch:];
-[_UIKBRTTouchInfo maximumRadius];
-[_UIKBRTTouchInfo nextTouch];
-[_UIKBRTTouchInfo originalZGradient];
-[_UIKBRTTouchInfo preRuleTouchState];
-[_UIKBRTTouchInfo previousTouch];
-[_UIKBRTTouchInfo setCurrentTouchState:];
-[_UIKBRTTouchInfo setOfTouchesToIgnoreWhenSettingTouchInfo:toState:];
-[_UIKBRTTouchInfo setPreRuleTouchState:];
-[_UIKBRTTouchInfo setTimerWithTimeInterval:onQueue:do:];
-[_UIKBRTTouchInfo updateTouch:];
-[_UIKBRTTouchInfo willChangeTouchInfo:toState:];
```
