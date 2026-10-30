# `CMBody`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CMViewBodyIdentifiable`
- 2 instance variables, 6 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" __motionBodyID;
d __interfaceAngle;
```

## Properties

```
@property (T@"NSUUID",&,N,V__motionBodyID) _motionBodyID;
@property (Td,N,V__interfaceAngle) _interfaceAngle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CMBody bodyWithUUID:];
+[CMBody bodyWithUUID:interfaceAngle:];
```

## Instance methods

```
-[CMBody dealloc];
-[CMBody _interfaceAngle];
-[CMBody _motionBodyID];
-[CMBody _startUpdatingBodyToken:];
-[CMBody _stopUpdatingBodyToken:];
-[CMBody set_motionBodyID:];
-[CMBody set_interfaceAngle:];
```
