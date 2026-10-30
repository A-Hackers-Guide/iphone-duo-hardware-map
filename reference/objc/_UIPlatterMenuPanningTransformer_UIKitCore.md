# `_UIPlatterMenuPanningTransformer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 18 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"<_UIPlatterMenuPanningTransformerDelegate>" _delegate;
d _minimumXVelocityForAxisLock;
Q _axisLock;
Q _overrideLockAxis;
d _lastAxisLockTime;
@"NSDate" _timeForLastDirectionalChange;
@"NSDate" _panBeginTime;
@"_UIVelocityIntegrator" _velocityIntegrator;
{CGPoint="x"d"y"d} _transitionZonePosition;
{CGSize="width"d"height"d} _transitionZoneSize;
{CGPoint="x"d"y"d} _lastTouchPosition;
{CGVector="dx"d"dy"d} _lastOffset;
{CGPoint="x"d"y"d} _lastTransformedPoint;
{CGPoint="x"d"y"d} _panBeginTouchPosition;
{CGPoint="x"d"y"d} _lastDirectionChangeTouchPosition;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _transitionZoneRect;
```

## Properties

```
@property (T{CGPoint=dd},N,V_transitionZonePosition) transitionZonePosition;
@property (T{CGSize=dd},N,V_transitionZoneSize) transitionZoneSize;
@property (T{CGPoint=dd},N,V_lastTouchPosition) lastTouchPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_transitionZoneRect) transitionZoneRect;
@property (TQ,N,V_axisLock) axisLock;
@property (TQ,N,V_overrideLockAxis) overrideLockAxis;
@property (Td,N,V_lastAxisLockTime) lastAxisLockTime;
@property (T{CGVector=dd},N,V_lastOffset) lastOffset;
@property (T@"NSDate",&,N,V_timeForLastDirectionalChange) timeForLastDirectionalChange;
@property (T{CGPoint=dd},N,V_lastTransformedPoint) lastTransformedPoint;
@property (T{CGPoint=dd},N,V_panBeginTouchPosition) panBeginTouchPosition;
@property (T{CGPoint=dd},N,V_lastDirectionChangeTouchPosition) lastDirectionChangeTouchPosition;
@property (T@"NSDate",&,N,V_panBeginTime) panBeginTime;
@property (T@"_UIVelocityIntegrator",&,N,V_velocityIntegrator) velocityIntegrator;
@property (T@"<_UIPlatterMenuPanningTransformerDelegate>",W,N,V_delegate) delegate;
@property (T{CGVector=dd},R,N) offset;
@property (T{CGVector=dd},R,N) velocity;
@property (Td,N,V_minimumXVelocityForAxisLock) minimumXVelocityForAxisLock;
```

## Class methods

```
+[_UIPlatterMenuPanningTransformer transformerWithAxisTransitionZonePosition:axisTransitionZoneSize:];
```

## Instance methods

```
-[_UIPlatterMenuPanningTransformer velocity];
-[_UIPlatterMenuPanningTransformer setDelegate:];
-[_UIPlatterMenuPanningTransformer delegate];
-[_UIPlatterMenuPanningTransformer velocityIntegrator];
-[_UIPlatterMenuPanningTransformer setVelocityIntegrator:];
-[_UIPlatterMenuPanningTransformer offset];
-[_UIPlatterMenuPanningTransformer setMinimumXVelocityForAxisLock:];
-[_UIPlatterMenuPanningTransformer _enterYLockedState];
-[_UIPlatterMenuPanningTransformer axisLock];
-[_UIPlatterMenuPanningTransformer didBeginPanningWithTouchPosition:currentTransformedPosition:];
-[_UIPlatterMenuPanningTransformer didEndPanningWithTouchPosition:currentTransformedPosition:];
-[_UIPlatterMenuPanningTransformer didPanWithTouchPosition:currentTransformedPosition:];
-[_UIPlatterMenuPanningTransformer initWithAxisTransitionZonePosition:axisTransitionZoneSize:];
-[_UIPlatterMenuPanningTransformer lastAxisLockTime];
-[_UIPlatterMenuPanningTransformer lastDirectionChangeTouchPosition];
-[_UIPlatterMenuPanningTransformer lastOffset];
-[_UIPlatterMenuPanningTransformer lastTouchPosition];
-[_UIPlatterMenuPanningTransformer lastTransformedPoint];
-[_UIPlatterMenuPanningTransformer lockIntoYAxis];
-[_UIPlatterMenuPanningTransformer minimumXVelocityForAxisLock];
-[_UIPlatterMenuPanningTransformer overrideLockAxis];
-[_UIPlatterMenuPanningTransformer panBeginTime];
-[_UIPlatterMenuPanningTransformer panBeginTouchPosition];
-[_UIPlatterMenuPanningTransformer setAxisLock:];
-[_UIPlatterMenuPanningTransformer setLastAxisLockTime:];
-[_UIPlatterMenuPanningTransformer setLastDirectionChangeTouchPosition:];
-[_UIPlatterMenuPanningTransformer setLastOffset:];
-[_UIPlatterMenuPanningTransformer setLastTouchPosition:];
-[_UIPlatterMenuPanningTransformer setLastTransformedPoint:];
-[_UIPlatterMenuPanningTransformer setOverrideLockAxis:];
-[_UIPlatterMenuPanningTransformer setPanBeginTime:];
-[_UIPlatterMenuPanningTransformer setPanBeginTouchPosition:];
-[_UIPlatterMenuPanningTransformer setTimeForLastDirectionalChange:];
-[_UIPlatterMenuPanningTransformer setTransitionZonePosition:];
-[_UIPlatterMenuPanningTransformer setTransitionZoneRect:];
-[_UIPlatterMenuPanningTransformer setTransitionZoneSize:];
-[_UIPlatterMenuPanningTransformer timeForLastDirectionalChange];
-[_UIPlatterMenuPanningTransformer timeIntervalSinceLastDirectionChange];
-[_UIPlatterMenuPanningTransformer transitionZonePosition];
-[_UIPlatterMenuPanningTransformer transitionZoneRect];
-[_UIPlatterMenuPanningTransformer transitionZoneSize];
```
