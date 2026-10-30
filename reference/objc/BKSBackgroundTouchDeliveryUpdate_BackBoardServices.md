# `BKSBackgroundTouchDeliveryUpdate`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `NSCopying`
- 5 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
I _touchIdentifier;
{?="contextID"I} _targetID;
i _pid;
d _timestamp;
@"NSArray" _hostingContextsChain;
```

## Properties

```
@property (TI,N,V_touchIdentifier) touchIdentifier;
@property (Td,N,V_timestamp) timestamp;
@property (T{?=I},N,V_targetID) targetID;
@property (T@"NSArray",&,N,V_hostingContextsChain) hostingContextsChain;
@property (Ti,N,V_pid) pid;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSBackgroundTouchDeliveryUpdate setPid:];
-[BKSBackgroundTouchDeliveryUpdate setTimestamp:];
-[BKSBackgroundTouchDeliveryUpdate touchIdentifier];
-[BKSBackgroundTouchDeliveryUpdate setTouchIdentifier:];
-[BKSBackgroundTouchDeliveryUpdate setTargetID:];
-[BKSBackgroundTouchDeliveryUpdate timestamp];
-[BKSBackgroundTouchDeliveryUpdate pid];
-[BKSBackgroundTouchDeliveryUpdate targetID];
-[BKSBackgroundTouchDeliveryUpdate hash];
-[BKSBackgroundTouchDeliveryUpdate appendDescriptionToStream:];
-[BKSBackgroundTouchDeliveryUpdate copyWithZone:];
-[BKSBackgroundTouchDeliveryUpdate isEqual:];
-[BKSBackgroundTouchDeliveryUpdate hostingContextsChain];
-[BKSBackgroundTouchDeliveryUpdate setHostingContextsChain:];
```
