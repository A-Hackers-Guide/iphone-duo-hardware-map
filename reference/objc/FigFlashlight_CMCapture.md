# `FigFlashlight`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _available;
B _overheated;
```

## Properties

```
@property (TB,R,GisAvailable,V_available) available;
@property (TB,R,GisOverheated,V_overheated) overheated;
@property (Tf,R) level;
@property (Tf,R) beamWidth;
```

## Instance methods

```
-[FigFlashlight powerOn];
-[FigFlashlight isAvailable];
-[FigFlashlight level];
-[FigFlashlight available];
-[FigFlashlight setLevel:];
-[FigFlashlight setLowCurrentTorchEnabled:];
-[FigFlashlight isOverheated];
-[FigFlashlight beamWidth];
-[FigFlashlight setBeamWidth:];
-[FigFlashlight notifyForCurrentState];
-[FigFlashlight powerOff];
-[FigFlashlight overHeated];
```
