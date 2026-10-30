# `SBFAnimationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- Protocols: `PTSettingsKeyPathObserver`
- 15 instance variables, 19 properties, 35 instance methods, 4 class methods

## Instance variables

```
@"BSAnimationSettings" _exportedSettings;
q _animationType;
d _delay;
Q _frameRate;
Q _curve;
@"PTPointSettings" _controlPoint1Settings;
@"PTPointSettings" _controlPoint2Settings;
@"PTFrameRateRangeSettings" _preferredFrameRateRange;
d _duration;
d _mass;
d _stiffness;
d _damping;
d _epsilon;
d _initialVelocity;
d _speed;
```

## Properties

```
@property (Tq,N,V_animationType) animationType;
@property (Td,N,V_delay) delay;
@property (TQ,N,V_frameRate) frameRate;
@property (TQ,N,V_curve) curve;
@property (T@"PTPointSettings",&,N,V_controlPoint1Settings) controlPoint1Settings;
@property (T@"PTPointSettings",&,N,V_controlPoint2Settings) controlPoint2Settings;
@property (T@"PTFrameRateRangeSettings",&,N,V_preferredFrameRateRange) preferredFrameRateRange;
@property (Td,N,V_duration) duration;
@property (Td,N,V_mass) mass;
@property (Td,N,V_stiffness) stiffness;
@property (Td,N,V_damping) damping;
@property (Td,N,V_epsilon) epsilon;
@property (Td,N,V_initialVelocity) initialVelocity;
@property (Td,R,N) calculatedDuration;
@property (Td,N,V_speed) speed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBFAnimationSettings ignoresKey:];
+[SBFAnimationSettings settingsControllerModule];
+[SBFAnimationSettings _moduleWithSectionTitle:];
+[SBFAnimationSettings _moduleWithSectionTitle:delay:frameRate:];
```

## Instance methods

```
-[SBFAnimationSettings setDamping:];
-[SBFAnimationSettings setSpeed:];
-[SBFAnimationSettings setInitialVelocity:];
-[SBFAnimationSettings speed];
-[SBFAnimationSettings setMass:];
-[SBFAnimationSettings animationType];
-[SBFAnimationSettings setPreferredFrameRateRange:];
-[SBFAnimationSettings damping];
-[SBFAnimationSettings dealloc];
-[SBFAnimationSettings setAnimationType:];
-[SBFAnimationSettings setStiffness:];
-[SBFAnimationSettings BSAnimationSettings];
-[SBFAnimationSettings setFrameRateRange:highFrameRateReason:];
-[SBFAnimationSettings preferredFrameRateRange];
-[SBFAnimationSettings duration];
-[SBFAnimationSettings delay];
-[SBFAnimationSettings initialVelocity];
-[SBFAnimationSettings stiffness];
-[SBFAnimationSettings setDefaultValues];
-[SBFAnimationSettings setDelay:];
-[SBFAnimationSettings initWithDefaultValues];
-[SBFAnimationSettings calculatedDuration];
-[SBFAnimationSettings mass];
-[SBFAnimationSettings setDuration:];
-[SBFAnimationSettings setEpsilon:];
-[SBFAnimationSettings epsilon];
-[SBFAnimationSettings curve];
-[SBFAnimationSettings controlPoint1Settings];
-[SBFAnimationSettings setCurve:];
-[SBFAnimationSettings settings:changedValueForKeyPath:];
-[SBFAnimationSettings controlPoint2Settings];
-[SBFAnimationSettings setControlPoint1Settings:];
-[SBFAnimationSettings setControlPoint2Settings:];
-[SBFAnimationSettings setFrameRate:];
-[SBFAnimationSettings frameRate];
```
