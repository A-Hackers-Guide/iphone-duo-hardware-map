# `CBCMAngleEvent`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAngleEventProtocol`
- 5 instance variables, 9 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"CMAngle" _cmAngle;
@"CBCMAngleService" _node;
I eventType;
^{__IOHIDServiceClient=} service;
^{__IOHIDEvent=} event;
```

## Properties

```
@property (T@"<CBAngleServiceProtocol>",R,GgetNode) node;
@property (Tf,R,GgetAngleDegrees) angleDegrees;
@property (T^{__IOHIDEvent=},R,N,Vevent) event;
@property (T^{__IOHIDServiceClient=},R,N,Vservice) service;
@property (TI,R,N,VeventType) eventType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBCMAngleEvent eventType];
-[CBCMAngleEvent dealloc];
-[CBCMAngleEvent event];
-[CBCMAngleEvent conformsToEvent:];
-[CBCMAngleEvent service];
-[CBCMAngleEvent getAngleDegrees];
-[CBCMAngleEvent getNode];
-[CBCMAngleEvent initWithCMAngle:andNode:];
```
