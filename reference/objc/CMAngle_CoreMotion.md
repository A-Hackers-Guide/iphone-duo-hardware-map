# `CMAngle`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 8 instance variables, 8 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _angleValid;
B _velocityValid;
f _angleDegrees;
f _mechanicalAngleDegrees;
f _progress;
f _velocityDegreesPerSeconds;
q _state;
q _eventPhase;
```

## Properties

```
@property (Tf,R,N,V_angleDegrees) angleDegrees;
@property (Tf,R,N,V_mechanicalAngleDegrees) mechanicalAngleDegrees;
@property (Tf,R,N,V_progress) progress;
@property (TB,R,N,GisAngleValid,V_angleValid) angleValid;
@property (Tf,R,N,V_velocityDegreesPerSeconds) velocityDegreesPerSeconds;
@property (TB,R,N,GisVelocityValid,V_velocityValid) velocityValid;
@property (Tq,R,N,V_state) state;
@property (Tq,R,N,V_eventPhase) eventPhase;
```

## Class methods

```
+[CMAngle supportsSecureCoding];
```

## Instance methods

```
-[CMAngle dealloc];
-[CMAngle progress];
-[CMAngle encodeWithCoder:];
-[CMAngle description];
-[CMAngle initWithCoder:];
-[CMAngle copyWithZone:];
-[CMAngle isEqual:];
-[CMAngle state];
-[CMAngle angleDegrees];
-[CMAngle isVelocityValid];
-[CMAngle eventPhase];
-[CMAngle initWithAngle:timestamp:continuousTimestamp:];
-[CMAngle isAngleValid];
-[CMAngle mechanicalAngleDegrees];
-[CMAngle velocityDegreesPerSeconds];
```
