# `CMStaticCameraPose`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _isStatic;
f _portraitAngleDeg;
f _portraitUpsideDownAngleDeg;
f _landscapeLeftAngleDeg;
f _landscapeRightAngleDeg;
f _faceUpAngleDeg;
f _faceDownAngleDeg;
d _timeInStaticState;
d _timeInMovingState;
```

## Properties

```
@property (TB,N,V_isStatic) isStatic;
@property (Td,N,V_timeInStaticState) timeInStaticState;
@property (Td,N,V_timeInMovingState) timeInMovingState;
@property (Tf,N,V_portraitAngleDeg) portraitAngleDeg;
@property (Tf,N,V_portraitUpsideDownAngleDeg) portraitUpsideDownAngleDeg;
@property (Tf,N,V_landscapeLeftAngleDeg) landscapeLeftAngleDeg;
@property (Tf,N,V_landscapeRightAngleDeg) landscapeRightAngleDeg;
@property (Tf,N,V_faceUpAngleDeg) faceUpAngleDeg;
@property (Tf,N,V_faceDownAngleDeg) faceDownAngleDeg;
```

## Instance methods

```
-[CMStaticCameraPose description];
-[CMStaticCameraPose isStatic];
-[CMStaticCameraPose faceDownAngleDeg];
-[CMStaticCameraPose faceUpAngleDeg];
-[CMStaticCameraPose initWithIsStatic:timeInStaticState:timeInMovingState:portraitAngle:portraitUpsideDownAngle:landscapeLeftAngle:landscapeRightAngle:faceUpAngle:faceDownAngle:];
-[CMStaticCameraPose landscapeLeftAngleDeg];
-[CMStaticCameraPose landscapeRightAngleDeg];
-[CMStaticCameraPose portraitAngleDeg];
-[CMStaticCameraPose portraitUpsideDownAngleDeg];
-[CMStaticCameraPose setFaceDownAngleDeg:];
-[CMStaticCameraPose setFaceUpAngleDeg:];
-[CMStaticCameraPose setIsStatic:];
-[CMStaticCameraPose setLandscapeLeftAngleDeg:];
-[CMStaticCameraPose setLandscapeRightAngleDeg:];
-[CMStaticCameraPose setPortraitAngleDeg:];
-[CMStaticCameraPose setPortraitUpsideDownAngleDeg:];
-[CMStaticCameraPose setTimeInMovingState:];
-[CMStaticCameraPose setTimeInStaticState:];
-[CMStaticCameraPose timeInMovingState];
-[CMStaticCameraPose timeInStaticState];
```
