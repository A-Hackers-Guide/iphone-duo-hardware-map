# `_UIParallaxMotionEffect`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIMotionEffect`
- 5 instance variables, 6 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIMotionEffectGroup" _group;
{UIOffset="horizontal"d"vertical"d} _slideMagnitude;
@"UIInterpolatingMotionEffect" _horizontalSlideEffect;
@"UIInterpolatingMotionEffect" _verticalSlideEffect;
@"_UITiltMotionEffect" _tiltEffect;
```

## Properties

```
@property (T{UIOffset=dd},N,V_slideMagnitude) slideMagnitude;
@property (Td,N) horizontalSlideAccelerationBoostFactor;
@property (Td,N) verticalSlideAccelerationBoostFactor;
@property (Td,N) maximumHorizontalTiltAngle;
@property (Td,N) maximumVerticalTiltAngle;
@property (Td,N) rotatingSphereRadius;
```

## Instance methods

```
-[_UIParallaxMotionEffect init];
-[_UIParallaxMotionEffect encodeWithCoder:];
-[_UIParallaxMotionEffect description];
-[_UIParallaxMotionEffect initWithCoder:];
-[_UIParallaxMotionEffect copyWithZone:];
-[_UIParallaxMotionEffect _activateTiltEffectIfNecessary];
-[_UIParallaxMotionEffect _keyPathsAndRelativeValuesForPose:];
-[_UIParallaxMotionEffect _updateGroupMotionEffect];
-[_UIParallaxMotionEffect _updateSlideEffectsWithCurrentSlideMagnitude];
-[_UIParallaxMotionEffect horizontalSlideAccelerationBoostFactor];
-[_UIParallaxMotionEffect keyPathsAndRelativeValuesForViewerOffset:];
-[_UIParallaxMotionEffect maximumHorizontalTiltAngle];
-[_UIParallaxMotionEffect maximumVerticalTiltAngle];
-[_UIParallaxMotionEffect rotatingSphereRadius];
-[_UIParallaxMotionEffect setHorizontalSlideAccelerationBoostFactor:];
-[_UIParallaxMotionEffect setMaximumHorizontalTiltAngle:];
-[_UIParallaxMotionEffect setMaximumVerticalTiltAngle:];
-[_UIParallaxMotionEffect setRotatingSphereRadius:];
-[_UIParallaxMotionEffect setSlideMagnitude:];
-[_UIParallaxMotionEffect setVerticalSlideAccelerationBoostFactor:];
-[_UIParallaxMotionEffect slideMagnitude];
-[_UIParallaxMotionEffect verticalSlideAccelerationBoostFactor];
```
