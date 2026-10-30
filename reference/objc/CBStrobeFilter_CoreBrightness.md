# `CBStrobeFilter`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBFilter`
- 3 instance variables, 1 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CBFlashlightManager" _flashlightManager;
B _isActive;
B _pollutedWithEvent;
```

## Properties

```
@property (TB,R) isPolluted;
```

## Instance methods

```
-[CBStrobeFilter initWithQueue:];
-[CBStrobeFilter stop];
-[CBStrobeFilter dealloc];
-[CBStrobeFilter start];
-[CBStrobeFilter filterEvent:];
-[CBStrobeFilter handleALSEvent:];
-[CBStrobeFilter initWithFlashlightManager:];
-[CBStrobeFilter isPolluted];
-[CBStrobeFilter wasFlashlightOnAt:];
```
