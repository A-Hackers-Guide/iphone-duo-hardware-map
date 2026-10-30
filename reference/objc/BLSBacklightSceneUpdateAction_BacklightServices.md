# `BLSBacklightSceneUpdateAction`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 0 instance variables, 4 properties, 5 instance methods, 0 class methods

## Properties

```
@property (T@"BLSBacklightChangeEvent",R,N) event;
@property (TB,R,N,GisAnimated) animated;
@property (TB,R,N,GisTouchTargetable) touchTargetable;
@property (TB,R,N) isUpdateToDateSpecifier;
```

## Instance methods

```
-[BLSBacklightSceneUpdateAction isAnimated];
-[BLSBacklightSceneUpdateAction isUpdateToDateSpecifier];
-[BLSBacklightSceneUpdateAction event];
-[BLSBacklightSceneUpdateAction initWithBacklightChangeEvent:animated:touchTargetable:isUpdateToDateSpecifier:completion:];
-[BLSBacklightSceneUpdateAction isTouchTargetable];
```
