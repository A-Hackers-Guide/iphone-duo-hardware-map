# `BKSHIDEventDeliveryPolicy`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 3 instance variables, 7 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _finalStringTokenInChain;
q _generation;
q _deferringPolicyStatus;
```

## Properties

```
@property (Tq,R,N,V_deferringPolicyStatus) deferringPolicyStatus;
@property (TB,R,N) finalStringTokenInChain;
@property (Tq,R,N) generation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKSHIDEventDeliveryPolicy _initWithPolicyObservation:];
-[BKSHIDEventDeliveryPolicy deferringPolicyStatus];
-[BKSHIDEventDeliveryPolicy generation];
-[BKSHIDEventDeliveryPolicy hash];
-[BKSHIDEventDeliveryPolicy description];
-[BKSHIDEventDeliveryPolicy appendDescriptionToStream:];
-[BKSHIDEventDeliveryPolicy finalStringTokenInChain];
-[BKSHIDEventDeliveryPolicy isEqual:];
```
