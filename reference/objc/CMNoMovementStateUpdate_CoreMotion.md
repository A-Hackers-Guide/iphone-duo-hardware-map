# `CMNoMovementStateUpdate`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _state;
q _detectionType;
d _startTime;
```

## Properties

```
@property (Tq,R,N,V_state) state;
@property (Tq,R,N,V_detectionType) detectionType;
@property (Td,R,N,V_startTime) startTime;
```

## Class methods

```
+[CMNoMovementStateUpdate supportsSecureCoding];
```

## Instance methods

```
-[CMNoMovementStateUpdate startTime];
-[CMNoMovementStateUpdate encodeWithCoder:];
-[CMNoMovementStateUpdate initWithCoder:];
-[CMNoMovementStateUpdate copyWithZone:];
-[CMNoMovementStateUpdate isEqual:];
-[CMNoMovementStateUpdate state];
-[CMNoMovementStateUpdate detectionType];
-[CMNoMovementStateUpdate initWithState:detectionType:startTime:];
```
