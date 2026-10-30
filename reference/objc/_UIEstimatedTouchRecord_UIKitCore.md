# `_UIEstimatedTouchRecord`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
{?="needsPressureUpdate"b1"hasUpdatedPressure"b1"updatedPressureStillEstimated"b1"needsRollAngleUpdate"b1"hasUpdatedRollAngle"b1"updatedRollAngleStillEstimated"b1} _stateFlags;
@"NSMutableArray" _touchables;
d _updatedPressure;
d _updatedRollAngle;
@"UITouch" _liveTouch;
@"UITouch" _frozenTouch;
@"NSNumber" _contextID;
```

## Properties

```
@property (T@"UITouch",R,N,V_liveTouch) liveTouch;
@property (T@"UITouch",R,N,V_frozenTouch) frozenTouch;
@property (T@"NSArray",R,N,V_touchables) touchables;
@property (T@"NSNumber",R,N,V_contextID) contextID;
@property (TB,R,N) hasRemainingUpdates;
```

## Instance methods

```
-[_UIEstimatedTouchRecord contextID];
-[_UIEstimatedTouchRecord _dispatchWithCurrentUpdates];
-[_UIEstimatedTouchRecord addTouchable:];
-[_UIEstimatedTouchRecord dispatchUpdateWithPressure:stillEstimated:];
-[_UIEstimatedTouchRecord dispatchUpdateWithRollAngle:stillEstimated:];
-[_UIEstimatedTouchRecord frozenTouch];
-[_UIEstimatedTouchRecord hasRemainingUpdates];
-[_UIEstimatedTouchRecord initWithLiveTouch:freezeTouch:contextID:];
-[_UIEstimatedTouchRecord liveTouch];
-[_UIEstimatedTouchRecord removeTouchable:];
-[_UIEstimatedTouchRecord touchables];
```
