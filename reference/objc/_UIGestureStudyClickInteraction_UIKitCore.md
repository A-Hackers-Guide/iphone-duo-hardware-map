# `_UIGestureStudyClickInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickInteractionDriverDelegate`, `UIInteraction`, `_UIGestureStudyParticipating`
- 7 instance variables, 14 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _usesForce;
@"UIView" _view;
@"<_UIClickInteractionDriving>" _driver;
@ _target;
: _action;
d _startTimestamp;
{CGPoint="x"d"y"d} _originalCentroid;
```

## Properties

```
@property (T@"<_UIClickInteractionDriving>",&,N,V_driver) driver;
@property (T@,W,N,V_target) target;
@property (T:,N,V_action) action;
@property (TB,N,V_usesForce) usesForce;
@property (Td,N,V_startTimestamp) startTimestamp;
@property (T{CGPoint=dd},N,V_originalCentroid) originalCentroid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
@property (T@"NSString",R,N) eventName;
@property (Td,R,N) duration;
@property (Td,R,N) movement;
```

## Instance methods

```
-[_UIGestureStudyClickInteraction clickDriver:didPerformEvent:];
-[_UIGestureStudyClickInteraction clickDriver:shouldBegin:];
-[_UIGestureStudyClickInteraction locationInCoordinateSpace:];
-[_UIGestureStudyClickInteraction setStartTimestamp:];
-[_UIGestureStudyClickInteraction driver];
-[_UIGestureStudyClickInteraction setOriginalCentroid:];
-[_UIGestureStudyClickInteraction setAction:];
-[_UIGestureStudyClickInteraction setDriver:];
-[_UIGestureStudyClickInteraction action];
-[_UIGestureStudyClickInteraction duration];
-[_UIGestureStudyClickInteraction startTimestamp];
-[_UIGestureStudyClickInteraction view];
-[_UIGestureStudyClickInteraction eventName];
-[_UIGestureStudyClickInteraction setTarget:];
-[_UIGestureStudyClickInteraction willMoveToView:];
-[_UIGestureStudyClickInteraction description];
-[_UIGestureStudyClickInteraction originalCentroid];
-[_UIGestureStudyClickInteraction target];
-[_UIGestureStudyClickInteraction didMoveToView:];
-[_UIGestureStudyClickInteraction initWithTarget:action:useForce:];
-[_UIGestureStudyClickInteraction movement];
-[_UIGestureStudyClickInteraction setUsesForce:];
-[_UIGestureStudyClickInteraction usesForce];
```
