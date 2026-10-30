# `_TtC13CameraEditKit32ContactAwareSliderPositionDriver`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKSliderPositionDriver`
- 4 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
CoreGraphics.CGFloat distanceTraveled;
CoreGraphics.CGFloat distanceToDecelerate;
CameraEditKit.OverwritingRingBuffer CameraEditKit.ContactAwareSliderPositionDriver.VelocitySample samples;
CameraEditKit.ContactAwareSliderPositionDriver.VelocitySample ? deadZoneSample;
```

## Properties

```
@property (Td,N,VdistanceTraveled) distanceTraveled;
@property (Td,N,VdistanceToDecelerate) distanceToDecelerate;
@property (Td,N,R) velocity;
```

## Instance methods

```
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver init];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver velocity];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver contactBeganWithAction:];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver contactEndedWithAction:];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver contactUpdatedWithAction:];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver distanceToDecelerate];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver distanceTraveled];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver setDistanceToDecelerate:];
-[_TtC13CameraEditKit32ContactAwareSliderPositionDriver setDistanceTraveled:];
```
