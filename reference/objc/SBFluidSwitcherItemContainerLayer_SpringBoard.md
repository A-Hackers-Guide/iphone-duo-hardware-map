# `SBFluidSwitcherItemContainerLayer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 4 instance variables, 2 properties, 8 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _previousPosition;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _previousTransform;
B _positionAnimationsBeginFromModelState;
B _transformAnimationsAreLegacyCounterRotations;
```

## Properties

```
@property (TB,N,V_positionAnimationsBeginFromModelState) positionAnimationsBeginFromModelState;
@property (TB,N,V_transformAnimationsAreLegacyCounterRotations) transformAnimationsAreLegacyCounterRotations;
```

## Instance methods

```
-[SBFluidSwitcherItemContainerLayer transformAnimationsAreLegacyCounterRotations];
-[SBFluidSwitcherItemContainerLayer setPositionAnimationsBeginFromModelState:];
-[SBFluidSwitcherItemContainerLayer setTransformAnimationsAreLegacyCounterRotations:];
-[SBFluidSwitcherItemContainerLayer positionAnimationsBeginFromModelState];
-[SBFluidSwitcherItemContainerLayer init];
-[SBFluidSwitcherItemContainerLayer addAnimation:forKey:];
-[SBFluidSwitcherItemContainerLayer setTransform:];
-[SBFluidSwitcherItemContainerLayer setPosition:];
```
