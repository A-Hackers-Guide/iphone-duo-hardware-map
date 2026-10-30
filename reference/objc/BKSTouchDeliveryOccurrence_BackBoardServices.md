# `BKSTouchDeliveryOccurrence`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`, `NSSecureCoding`
- 6 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _detached;
I _touchIdentifier;
I _transducerType;
I _contextID;
i _pid;
q _kind;
```

## Properties

```
@property (Tq,R,N,V_kind) kind;
@property (TI,R,N,V_touchIdentifier) touchIdentifier;
@property (TI,R,N,V_transducerType) transducerType;
@property (TB,R,N,V_detached) detached;
@property (TI,R,N,V_contextID) contextID;
@property (Ti,R,N,V_pid) pid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchDeliveryOccurrence supportsSecureCoding];
```

## Instance methods

```
-[BKSTouchDeliveryOccurrence transducerType];
-[BKSTouchDeliveryOccurrence touchIdentifier];
-[BKSTouchDeliveryOccurrence pid];
-[BKSTouchDeliveryOccurrence encodeWithCoder:];
-[BKSTouchDeliveryOccurrence hash];
-[BKSTouchDeliveryOccurrence description];
-[BKSTouchDeliveryOccurrence detached];
-[BKSTouchDeliveryOccurrence initWithCoder:];
-[BKSTouchDeliveryOccurrence appendDescriptionToStream:];
-[BKSTouchDeliveryOccurrence contextID];
-[BKSTouchDeliveryOccurrence copyWithZone:];
-[BKSTouchDeliveryOccurrence isEqual:];
-[BKSTouchDeliveryOccurrence kind];
-[BKSTouchDeliveryOccurrence initWithKind:touchIdentifier:transducerType:detached:contextID:pid:];
```
