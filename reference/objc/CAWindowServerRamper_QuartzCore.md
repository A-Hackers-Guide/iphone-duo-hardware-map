# `CAWindowServerRamper`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
i _id;
@"CAWindowServerDisplay" _display;
@"CADisplay" _cadisplay;
@"CADisplayLink" _link;
d _duration;
d _beginTime;
```

## Properties

```
@property (T@"CAWindowServerDisplay",&,V_display) display;
@property (T@"CADisplay",&,V_cadisplay) cadisplay;
@property (T@"CADisplayLink",&,V_link) link;
@property (Td,V_duration) duration;
@property (Ti,V_id) id;
@property (Td,V_beginTime) beginTime;
```

## Instance methods

```
-[CAWindowServerRamper initWithDisplay:];
-[CAWindowServerRamper setDisplay:];
-[CAWindowServerRamper setBeginTime:];
-[CAWindowServerRamper display];
-[CAWindowServerRamper id];
-[CAWindowServerRamper duration];
-[CAWindowServerRamper rampCallback:];
-[CAWindowServerRamper setDuration:];
-[CAWindowServerRamper beginTime];
-[CAWindowServerRamper link];
-[CAWindowServerRamper setLink:];
-[CAWindowServerRamper runRamp];
-[CAWindowServerRamper cadisplay];
-[CAWindowServerRamper setCadisplay:];
-[CAWindowServerRamper setId:];
```
