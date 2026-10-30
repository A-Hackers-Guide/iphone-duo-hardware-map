# `CAFlipBookFrame`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 12 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _presentationTime;
Q _frameId;
I _generation;
f _apl;
f _aplDimming;
Q _memoryUsage;
^{__IOSurface=} _rawSurface;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _rawSurfaceFrame;
^{__IOSurface=} _surface;
@ _userInfo;
B _inverted;
B _lowPowerRendering;
Q _lowPowerRenderingPresentationTime;
```

## Properties

```
@property (TQ,R,N) presentationTime;
@property (TQ,R,N) frameId;
@property (T@,R,N) userInfo;
@property (Tf,R,N) apl;
@property (Tf,R,N) aplDimming;
@property (TQ,R,N) memoryUsage;
@property (T^{__IOSurface=},N) rawSurface;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) rawSurfaceFrame;
@property (T^{__IOSurface=},N) surface;
@property (TB,R,N,GisInverted) inverted;
@property (TB,R,N) lowPowerRendering;
@property (TQ,R,N) lowPowerRenderingPresentationTime;
```

## Instance methods

```
-[CAFlipBookFrame isInverted];
-[CAFlipBookFrame setSurface:];
-[CAFlipBookFrame surface];
-[CAFlipBookFrame userInfo];
-[CAFlipBookFrame dealloc];
-[CAFlipBookFrame setLowPowerRenderingPresentationTime:];
-[CAFlipBookFrame frameId];
-[CAFlipBookFrame generation];
-[CAFlipBookFrame description];
-[CAFlipBookFrame lowPowerRenderingPresentationTime];
-[CAFlipBookFrame rawSurfaceFrame];
-[CAFlipBookFrame apl];
-[CAFlipBookFrame _initWithPresentationTime:frameId:generation:apl:aplDimming:memoryUsage:inverted:userInfo:];
-[CAFlipBookFrame aplDimming];
-[CAFlipBookFrame lowPowerRendering];
-[CAFlipBookFrame memoryUsage];
-[CAFlipBookFrame presentationTime];
-[CAFlipBookFrame rawSurface];
-[CAFlipBookFrame releaseSurface];
-[CAFlipBookFrame setLowPowerRendering:];
-[CAFlipBookFrame setRawSurface:];
-[CAFlipBookFrame setRawSurfaceFrame:];
```
