# `CMSuppressionEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 4 instance variables, 4 properties, 12 instance methods, 4 class methods

## Instance variables

```
q fType;
Q fReason;
Q fFacedownState;
d fTimeSinceLastFacedownStatic;
```

## Properties

```
@property (Tq,R,N) type;
@property (TQ,R,N) reason;
@property (TQ,R,N) facedownState;
@property (Td,R,N) timeSinceLastFacedownStatic;
```

## Class methods

```
+[CMSuppressionEvent supportsSecureCoding];
+[CMSuppressionEvent stringForEventFacedownState:];
+[CMSuppressionEvent stringForEventReason:];
+[CMSuppressionEvent stringForEventType:];
```

## Instance methods

```
-[CMSuppressionEvent dealloc];
-[CMSuppressionEvent type];
-[CMSuppressionEvent encodeWithCoder:];
-[CMSuppressionEvent description];
-[CMSuppressionEvent initWithCoder:];
-[CMSuppressionEvent reason];
-[CMSuppressionEvent copyWithZone:];
-[CMSuppressionEvent facedownState];
-[CMSuppressionEvent initWithEventType:reason:facedownState:timestamp:];
-[CMSuppressionEvent initWithEventType:reason:facedownState:timestamp:timeSinceLastFacedownStatic:];
-[CMSuppressionEvent initWithEventType:reason:timestamp:];
-[CMSuppressionEvent timeSinceLastFacedownStatic];
```
