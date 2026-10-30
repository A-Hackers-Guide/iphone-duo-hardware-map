# `UIKBHandwritingInputSpeedModel`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _recordedIntervals;
@"NSMutableArray" _recordedSpeeds;
d _lastStrokeTimeStamp;
d _lastTouchTimeStamp;
{CGPoint="x"d"y"d} _lastTouchLocation;
@"NSMutableArray" _pointsCurrentStroke;
B _duringStroke;
B _autoConfirmationEnabled;
d _minTimeout;
d _maxTimeout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _handwritingFrame;
```

## Properties

```
@property (TB,R,N,V_autoConfirmationEnabled) autoConfirmationEnabled;
@property (Td,R,N,V_minTimeout) minTimeout;
@property (Td,R,N,V_maxTimeout) maxTimeout;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_handwritingFrame) handwritingFrame;
```

## Instance methods

```
-[UIKBHandwritingInputSpeedModel init];
-[UIKBHandwritingInputSpeedModel addPoint:timestamp:];
-[UIKBHandwritingInputSpeedModel autoConfirmationEnabled];
-[UIKBHandwritingInputSpeedModel beginStroke];
-[UIKBHandwritingInputSpeedModel endCharacter];
-[UIKBHandwritingInputSpeedModel endStroke];
-[UIKBHandwritingInputSpeedModel handwritingFrame];
-[UIKBHandwritingInputSpeedModel maxTimeout];
-[UIKBHandwritingInputSpeedModel minTimeout];
-[UIKBHandwritingInputSpeedModel setHandwritingFrame:];
-[UIKBHandwritingInputSpeedModel smoothValueFromArray:];
-[UIKBHandwritingInputSpeedModel speedForCurrentStroke];
-[UIKBHandwritingInputSpeedModel timeoutForNextPage];
-[UIKBHandwritingInputSpeedModel updatePreferences];
```
