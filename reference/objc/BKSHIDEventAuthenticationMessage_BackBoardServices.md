# `BKSHIDEventAuthenticationMessage`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `NSSecureCoding`, `NSCopying`, `BSProtobufSerializable`, `BSXPCCoding`, `BSXPCSecureCoding`, `BKSHIDEventProvenance`
- 15 instance variables, 18 properties, 27 instance methods, 4 class methods

## Instance variables

```
q _versionedPID;
I _eventType;
I _touchIdentifier;
I _targetSlotID;
I _targetContextID;
I _targetWindowID;
@"BKSHIDEventHitTestLayerInformation" _hitTestInformationFromStartEvent;
@"BKSHIDEventHitTestLayerInformation" _hitTestInformationFromEndEvent;
Q _timestamp;
Q _originIdentifier;
Q _context;
q _secureNameStatus;
B _registrantEntitled;
Q _senderID;
@"NSData" _signature;
```

## Properties

```
@property (Tq,R,N,V_versionedPID) versionedPID;
@property (TI,R,N,V_eventType) eventType;
@property (TI,R,N,V_touchIdentifier) touchIdentifier;
@property (TI,R,N,V_targetContextID) targetContextID;
@property (TI,R,N,V_targetWindowID) targetWindowID;
@property (TI,R,N,V_targetSlotID) targetSlotID;
@property (T@"BKSHIDEventHitTestLayerInformation",R,N,V_hitTestInformationFromStartEvent) hitTestInformationFromStartEvent;
@property (T@"BKSHIDEventHitTestLayerInformation",R,N,V_hitTestInformationFromEndEvent) hitTestInformationFromEndEvent;
@property (TQ,R,N,V_timestamp) timestamp;
@property (TQ,R,N,V_originIdentifier) originIdentifier;
@property (TQ,R,N,V_context) context;
@property (Tq,R,N,V_secureNameStatus) secureNameStatus;
@property (TB,R,N,V_registrantEntitled) registrantEntitled;
@property (TQ,R,N,V_senderID) senderID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventAuthenticationMessage supportsBSXPCSecureCoding];
+[BKSHIDEventAuthenticationMessage supportsSecureCoding];
+[BKSHIDEventAuthenticationMessage protobufSchema];
+[BKSHIDEventAuthenticationMessage new];
```

## Instance methods

```
-[BKSHIDEventAuthenticationMessage eventType];
-[BKSHIDEventAuthenticationMessage touchIdentifier];
-[BKSHIDEventAuthenticationMessage initForProtobufDecoding];
-[BKSHIDEventAuthenticationMessage init];
-[BKSHIDEventAuthenticationMessage targetSlotID];
-[BKSHIDEventAuthenticationMessage initWithXPCDictionary:];
-[BKSHIDEventAuthenticationMessage appendDescriptionToFormatter:];
-[BKSHIDEventAuthenticationMessage timestamp];
-[BKSHIDEventAuthenticationMessage versionedPID];
-[BKSHIDEventAuthenticationMessage secureNameStatus];
-[BKSHIDEventAuthenticationMessage originIdentifier];
-[BKSHIDEventAuthenticationMessage senderID];
-[BKSHIDEventAuthenticationMessage hitTestInformationFromStartEvent];
-[BKSHIDEventAuthenticationMessage targetContextID];
-[BKSHIDEventAuthenticationMessage encodeWithXPCDictionary:];
-[BKSHIDEventAuthenticationMessage targetWindowID];
-[BKSHIDEventAuthenticationMessage encodeWithCoder:];
-[BKSHIDEventAuthenticationMessage registrantEntitled];
-[BKSHIDEventAuthenticationMessage hash];
-[BKSHIDEventAuthenticationMessage description];
-[BKSHIDEventAuthenticationMessage initWithCoder:];
-[BKSHIDEventAuthenticationMessage encodeWithBSXPCCoder:];
-[BKSHIDEventAuthenticationMessage initWithBSXPCCoder:];
-[BKSHIDEventAuthenticationMessage copyWithZone:];
-[BKSHIDEventAuthenticationMessage context];
-[BKSHIDEventAuthenticationMessage isEqual:];
-[BKSHIDEventAuthenticationMessage hitTestInformationFromEndEvent];
```
