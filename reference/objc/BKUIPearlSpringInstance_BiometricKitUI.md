# `BKUIPearlSpringInstance`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
[3@"FLSpring"] springs;
_value;
{?="columns"[4]} _matrix;
{?="columns"[4]} _initialMatrix;
_color;
f _alphaFactor;
f _alphaDecay;
f _scale;
f _scaleDest;
B _grayscale;
Q _axisOrientation;
Q _springState;
_target;
```

## Properties

```
@property (TQ,V_axisOrientation) axisOrientation;
@property (TQ,N,V_springState) springState;
@property (T,N,V_target) target;
@property (T,N) value;
@property (TB,N,V_grayscale) grayscale;
```

## Instance methods

```
-[BKUIPearlSpringInstance setGrayscale:];
-[BKUIPearlSpringInstance setParameters:];
-[BKUIPearlSpringInstance value];
-[BKUIPearlSpringInstance velocity];
-[BKUIPearlSpringInstance color];
-[BKUIPearlSpringInstance grayscale];
-[BKUIPearlSpringInstance setValue:];
-[BKUIPearlSpringInstance step:];
-[BKUIPearlSpringInstance setTarget:];
-[BKUIPearlSpringInstance target];
-[BKUIPearlSpringInstance matrix];
-[BKUIPearlSpringInstance axisOrientation];
-[BKUIPearlSpringInstance setSpringState:];
-[BKUIPearlSpringInstance createAxisRotationMatrix:];
-[BKUIPearlSpringInstance initWithInitialRotation:color:];
-[BKUIPearlSpringInstance setAxisOrientation:];
-[BKUIPearlSpringInstance springState];
```
