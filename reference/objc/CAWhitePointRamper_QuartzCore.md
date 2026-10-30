# `CAWhitePointRamper`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAWindowServerRamper`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
f _scaleStart;
f _scaleEnd;
{?="matrix"[9f]} _whitePointStart;
{?="matrix"[9f]} _whitePointEnd;
```

## Properties

```
@property (T{?=[9f]},V_whitePointStart) whitePointStart;
@property (T{?=[9f]},V_whitePointEnd) whitePointEnd;
@property (Tf,V_scaleStart) scaleStart;
@property (Tf,V_scaleEnd) scaleEnd;
```

## Instance methods

```
-[CAWhitePointRamper initWithDisplay:];
-[CAWhitePointRamper rampCallback:];
-[CAWhitePointRamper whitePointStart];
-[CAWhitePointRamper scaleEnd];
-[CAWhitePointRamper scaleStart];
-[CAWhitePointRamper setScaleEnd:];
-[CAWhitePointRamper setScaleStart:];
-[CAWhitePointRamper setWhitePointEnd:];
-[CAWhitePointRamper setWhitePointStart:];
-[CAWhitePointRamper whitePointEnd];
```
