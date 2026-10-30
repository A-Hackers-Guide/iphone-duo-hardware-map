# `BKSTouchDeliveryUpdate`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isDetached;
I _touchIdentifier;
I _transducerType;
{?="contextID"I} _targetID;
i _pid;
q _type;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (TI,N,V_touchIdentifier) touchIdentifier;
@property (TB,N,V_isDetached) isDetached;
@property (TI,N,V_transducerType) transducerType;
@property (T{?=I},N,V_targetID) targetID;
@property (Ti,N,V_pid) pid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSTouchDeliveryUpdate supportsSecureCoding];
```

## Instance methods

```
-[BKSTouchDeliveryUpdate transducerType];
-[BKSTouchDeliveryUpdate setTransducerType:];
-[BKSTouchDeliveryUpdate setPid:];
-[BKSTouchDeliveryUpdate touchIdentifier];
-[BKSTouchDeliveryUpdate isDetached];
-[BKSTouchDeliveryUpdate setTouchIdentifier:];
-[BKSTouchDeliveryUpdate setTargetID:];
-[BKSTouchDeliveryUpdate pid];
-[BKSTouchDeliveryUpdate setType:];
-[BKSTouchDeliveryUpdate type];
-[BKSTouchDeliveryUpdate encodeWithCoder:];
-[BKSTouchDeliveryUpdate targetID];
-[BKSTouchDeliveryUpdate hash];
-[BKSTouchDeliveryUpdate initWithCoder:];
-[BKSTouchDeliveryUpdate appendDescriptionToStream:];
-[BKSTouchDeliveryUpdate copyWithZone:];
-[BKSTouchDeliveryUpdate setIsDetached:];
-[BKSTouchDeliveryUpdate isEqual:];
```
