# `BLSBacklightSceneUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _touchTargetable;
@"BLSBacklightSceneVisualState" _visualState;
@"BLSBacklightSceneVisualState" _previousVisualState;
@"BLSAlwaysOnFrameSpecifier" _frameSpecifier;
@"BLSBacklightChangeEvent" _triggerEvent;
```

## Properties

```
@property (T@"BLSBacklightSceneVisualState",R,N,V_visualState) visualState;
@property (T@"BLSBacklightSceneVisualState",R,N,V_previousVisualState) previousVisualState;
@property (T@"BLSAlwaysOnFrameSpecifier",R,N,V_frameSpecifier) frameSpecifier;
@property (TB,R,N,GisAnimated,V_animated) animated;
@property (T@"BLSBacklightChangeEvent",R,N,V_triggerEvent) triggerEvent;
@property (TB,R,N,GisTouchTargetable,V_touchTargetable) touchTargetable;
```

## Instance methods

```
-[BLSBacklightSceneUpdateContext triggerEvent];
-[BLSBacklightSceneUpdateContext visualState];
-[BLSBacklightSceneUpdateContext isAnimated];
-[BLSBacklightSceneUpdateContext hash];
-[BLSBacklightSceneUpdateContext description];
-[BLSBacklightSceneUpdateContext isEqual:];
-[BLSBacklightSceneUpdateContext isTouchTargetable];
-[BLSBacklightSceneUpdateContext frameSpecifier];
-[BLSBacklightSceneUpdateContext previousVisualState];
-[BLSBacklightSceneUpdateContext initWithVisualState:previousVisualState:frameSpecifier:animated:triggerEvent:touchTargetable:];
```
