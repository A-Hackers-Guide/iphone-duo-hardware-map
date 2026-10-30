# `CAUserAdjustment`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
d _xDelta;
d _yDelta;
d _luminanceScale;
d _timestamp;
```

## Properties

```
@property (Td,R,V_xDelta) xDelta;
@property (Td,R,V_yDelta) yDelta;
@property (Td,R,V_luminanceScale) luminanceScale;
@property (Td,R,V_timestamp) timestamp;
```

## Instance methods

```
-[CAUserAdjustment timestamp];
-[CAUserAdjustment initWithXDelta:yDelta:luminanceScale:];
-[CAUserAdjustment initWithXDelta:yDelta:luminanceScale:timestamp:];
-[CAUserAdjustment luminanceScale];
-[CAUserAdjustment xDelta];
-[CAUserAdjustment yDelta];
```
