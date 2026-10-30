# `CMAngleManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 8 instance methods, 5 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (TB,R,N,GisAngleActive) angleActive;
@property (Td,N) angleUpdateInterval;
```

## Class methods

```
+[CMAngleManager isAvailable];
+[CMAngleManager maxAngleDegrees];
+[CMAngleManager minAngleDegrees];
+[CMAngleManager setShouldEmitWakeLatencySignpostsOnStateChangeForTesting:];
+[CMAngleManager shouldEmitWakeLatencySignpostsOnStateChangeForTesting];
```

## Instance methods

```
-[CMAngleManager init];
-[CMAngleManager dealloc];
-[CMAngleManager angleUpdateInterval];
-[CMAngleManager isAngleActive];
-[CMAngleManager setAngleHandler:interval:];
-[CMAngleManager setAngleUpdateInterval:];
-[CMAngleManager startAngleUpdatesToQueue:handler:];
-[CMAngleManager stopAngleUpdates];
```
