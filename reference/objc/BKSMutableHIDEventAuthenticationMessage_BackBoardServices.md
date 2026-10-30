# `BKSMutableHIDEventAuthenticationMessage`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventAuthenticationMessage`
- 0 instance variables, 13 properties, 15 instance methods, 0 class methods

## Properties

```
@property (Tq,D,N) versionedPID;
@property (TI,D,N) eventType;
@property (TI,D,N) touchIdentifier;
@property (TI,D,N) targetContextID;
@property (TI,D,N) targetWindowID;
@property (TI,D,N) targetSlotID;
@property (T@"BKSHIDEventHitTestLayerInformation",&,D,N) hitTestInformationFromStartEvent;
@property (T@"BKSHIDEventHitTestLayerInformation",&,D,N) hitTestInformationFromEndEvent;
@property (TQ,D,N) originIdentifier;
@property (TQ,D,N) context;
@property (Tq,D,N) secureNameStatus;
@property (TB,D,N) registrantEntitled;
@property (TQ,D,N) senderID;
```

## Instance methods

```
-[BKSMutableHIDEventAuthenticationMessage setDestinationAuditToken:];
-[BKSMutableHIDEventAuthenticationMessage setEventType:];
-[BKSMutableHIDEventAuthenticationMessage setTouchIdentifier:];
-[BKSMutableHIDEventAuthenticationMessage setContext:];
-[BKSMutableHIDEventAuthenticationMessage setVersionedPID:];
-[BKSMutableHIDEventAuthenticationMessage setSenderID:];
-[BKSMutableHIDEventAuthenticationMessage copyWithZone:];
-[BKSMutableHIDEventAuthenticationMessage setHitTestInformationFromEndEvent:];
-[BKSMutableHIDEventAuthenticationMessage setHitTestInformationFromStartEvent:];
-[BKSMutableHIDEventAuthenticationMessage setOriginIdentifier:];
-[BKSMutableHIDEventAuthenticationMessage setRegistrantEntitled:];
-[BKSMutableHIDEventAuthenticationMessage setSecureNameStatus:];
-[BKSMutableHIDEventAuthenticationMessage setTargetSlotID:];
-[BKSMutableHIDEventAuthenticationMessage setTargetWindowID:];
-[BKSMutableHIDEventAuthenticationMessage setTargetContextID:];
```
