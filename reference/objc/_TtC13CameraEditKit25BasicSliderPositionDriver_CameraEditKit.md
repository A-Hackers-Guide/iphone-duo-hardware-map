# `_TtC13CameraEditKit25BasicSliderPositionDriver`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKSliderPositionDriver`
- 4 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
CoreGraphics.CGFloat distanceTraveled;
CoreGraphics.CGFloat distanceToDecelerate;
CameraEditKit.BasicSliderPositionDriver.VelocitySample ? latestSample;
CameraEditKit.BasicSliderPositionDriver.VelocitySample ? previousSample;
```

## Properties

```
@property (Td,N,VdistanceTraveled) distanceTraveled;
@property (Td,N,VdistanceToDecelerate) distanceToDecelerate;
@property (Td,N,R) velocity;
```

## Instance methods

```
-[_TtC13CameraEditKit25BasicSliderPositionDriver init];
-[_TtC13CameraEditKit25BasicSliderPositionDriver velocity];
-[_TtC13CameraEditKit25BasicSliderPositionDriver contactBeganWithAction:];
-[_TtC13CameraEditKit25BasicSliderPositionDriver contactEndedWithAction:];
-[_TtC13CameraEditKit25BasicSliderPositionDriver contactUpdatedWithAction:];
-[_TtC13CameraEditKit25BasicSliderPositionDriver distanceToDecelerate];
-[_TtC13CameraEditKit25BasicSliderPositionDriver distanceTraveled];
-[_TtC13CameraEditKit25BasicSliderPositionDriver setDistanceToDecelerate:];
-[_TtC13CameraEditKit25BasicSliderPositionDriver setDistanceTraveled:];
```
