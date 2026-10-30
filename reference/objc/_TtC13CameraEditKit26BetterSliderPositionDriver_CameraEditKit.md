# `_TtC13CameraEditKit26BetterSliderPositionDriver`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKSliderPositionDriver`
- 5 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
CoreGraphics.CGFloat translation;
CoreGraphics.CGFloat decelerationTarget;
CameraEditKit.OverwritingRingBuffer CameraEditKit.BetterSliderPositionDriver.DeltaSample allSamples;
CameraEditKit.OverwritingRingBuffer CameraEditKit.BetterSliderPositionDriver.DeltaSample validSamples;
_$sSd lastUpdateTime;
```

## Properties

```
@property (Td,N,R) distanceTraveled;
@property (Td,N,R) distanceToDecelerate;
@property (Td,N,R) velocity;
```

## Instance methods

```
-[_TtC13CameraEditKit26BetterSliderPositionDriver init];
-[_TtC13CameraEditKit26BetterSliderPositionDriver velocity];
-[_TtC13CameraEditKit26BetterSliderPositionDriver contactBeganWithAction:];
-[_TtC13CameraEditKit26BetterSliderPositionDriver contactEndedWithAction:];
-[_TtC13CameraEditKit26BetterSliderPositionDriver contactUpdatedWithAction:];
-[_TtC13CameraEditKit26BetterSliderPositionDriver distanceToDecelerate];
-[_TtC13CameraEditKit26BetterSliderPositionDriver distanceTraveled];
```
