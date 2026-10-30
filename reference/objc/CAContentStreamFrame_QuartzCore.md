# `CAContentStreamFrame`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _fastPath;
i _status;
I _surfaceId;
Q _displayTime;
Q _updateBeginTime;
^{__IOSurface=} _surface;
Q _dropCount;
d _displayResolution;
d _contentScaleX;
d _contentScaleY;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _contentRect;
```

## Properties

```
@property (Ti,V_status) status;
@property (TQ,V_displayTime) displayTime;
@property (TQ,V_updateBeginTime) updateBeginTime;
@property (T^{__IOSurface=},V_surface) surface;
@property (TI,V_surfaceId) surfaceId;
@property (TQ,V_dropCount) dropCount;
@property (Td,V_displayResolution) displayResolution;
@property (Td,V_contentScaleX) contentScaleX;
@property (Td,V_contentScaleY) contentScaleY;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_contentRect) contentRect;
@property (TB,V_fastPath) fastPath;
```

## Instance methods

```
-[CAContentStreamFrame setSurface:];
-[CAContentStreamFrame surface];
-[CAContentStreamFrame contentRect];
-[CAContentStreamFrame status];
-[CAContentStreamFrame setContentRect:];
-[CAContentStreamFrame setStatus:];
-[CAContentStreamFrame setDisplayTime:];
-[CAContentStreamFrame updateBeginTime];
-[CAContentStreamFrame contentScaleX];
-[CAContentStreamFrame contentScaleY];
-[CAContentStreamFrame displayResolution];
-[CAContentStreamFrame displayTime];
-[CAContentStreamFrame dropCount];
-[CAContentStreamFrame fastPath];
-[CAContentStreamFrame setContentScaleX:];
-[CAContentStreamFrame setContentScaleY:];
-[CAContentStreamFrame setDisplayResolution:];
-[CAContentStreamFrame setDropCount:];
-[CAContentStreamFrame setFastPath:];
-[CAContentStreamFrame setSurfaceId:];
-[CAContentStreamFrame setUpdateBeginTime:];
-[CAContentStreamFrame surfaceId];
```
