# `_UIKBRTTouchHistoryInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isLeftHand;
B _isActive;
B _ignoreForDrift;
B _ignoreTouch;
@ _touchIdentifier;
d _touchTime;
{CGPoint="x"d"y"d} _actualLocation;
{CGPoint="x"d"y"d} _errorVector;
```

## Properties

```
@property (T@,&,N,V_touchIdentifier) touchIdentifier;
@property (Td,N,V_touchTime) touchTime;
@property (T{CGPoint=dd},N,V_actualLocation) actualLocation;
@property (TB,N,V_isLeftHand) isLeftHand;
@property (TB,N,V_isActive) isActive;
@property (TB,N,V_ignoreForDrift) ignoreForDrift;
@property (TB,N,V_ignoreTouch) ignoreTouch;
@property (T{CGPoint=dd},N,V_errorVector) errorVector;
```

## Instance methods

```
-[_UIKBRTTouchHistoryInfo setIsActive:];
-[_UIKBRTTouchHistoryInfo touchIdentifier];
-[_UIKBRTTouchHistoryInfo init];
-[_UIKBRTTouchHistoryInfo setTouchIdentifier:];
-[_UIKBRTTouchHistoryInfo description];
-[_UIKBRTTouchHistoryInfo isActive];
-[_UIKBRTTouchHistoryInfo setErrorVector:];
-[_UIKBRTTouchHistoryInfo setIgnoreTouch:];
-[_UIKBRTTouchHistoryInfo actualLocation];
-[_UIKBRTTouchHistoryInfo errorVector];
-[_UIKBRTTouchHistoryInfo ignoreForDrift];
-[_UIKBRTTouchHistoryInfo ignoreTouch];
-[_UIKBRTTouchHistoryInfo isLeftHand];
-[_UIKBRTTouchHistoryInfo setActualLocation:];
-[_UIKBRTTouchHistoryInfo setIgnoreForDrift:];
-[_UIKBRTTouchHistoryInfo setIsLeftHand:];
-[_UIKBRTTouchHistoryInfo setTouchTime:];
-[_UIKBRTTouchHistoryInfo touchTime];
```
