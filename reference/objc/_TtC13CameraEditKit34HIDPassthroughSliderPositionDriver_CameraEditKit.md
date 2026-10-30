# `_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKSliderPositionDriver`
- 8 instance variables, 9 properties, 21 instance methods, 2 class methods

## Instance variables

```
CoreGraphics.CGFloat distanceTraveled;
CoreGraphics.CGFloat distanceToDecelerate;
CoreGraphics.CGFloat liftoffVelocity;
Swift.Bool liftoffDidFlickUp;
Swift.Bool liftoffDidFlickDown;
_$sSd scrollMultiplier;
_$sSd velocityMultiplier;
Swift.Bool acceptsLowConfidenceScrolling;
```

## Properties

```
@property (Td,N,VdistanceTraveled) distanceTraveled;
@property (Td,N,VdistanceToDecelerate) distanceToDecelerate;
@property (Td,N,VliftoffVelocity) liftoffVelocity;
@property (TB,N,VliftoffDidFlickUp) liftoffDidFlickUp;
@property (TB,N,VliftoffDidFlickDown) liftoffDidFlickDown;
@property (Td,N,R) velocity;
@property (Td,N,VscrollMultiplier) scrollMultiplier;
@property (Td,N,VvelocityMultiplier) velocityMultiplier;
@property (TB,N,VacceptsLowConfidenceScrolling) acceptsLowConfidenceScrolling;
```

## Class methods

```
+[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver defaultScrollMultiplier];
+[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver defaultVelocityMultiplier];
```

## Instance methods

```
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver velocityMultiplier];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver init];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver velocity];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setVelocityMultiplier:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver liftoffVelocity];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver acceptsLowConfidenceScrolling];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver contactBeganWithAction:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver contactEndedWithAction:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver contactUpdatedWithAction:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver distanceToDecelerate];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver distanceTraveled];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver liftoffDidFlickDown];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver liftoffDidFlickUp];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver scrollMultiplier];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setAcceptsLowConfidenceScrolling:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setDistanceToDecelerate:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setDistanceTraveled:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setLiftoffDidFlickDown:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setLiftoffDidFlickUp:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setLiftoffVelocity:];
-[_TtC13CameraEditKit34HIDPassthroughSliderPositionDriver setScrollMultiplier:];
```
