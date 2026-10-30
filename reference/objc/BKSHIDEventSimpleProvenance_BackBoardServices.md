# `BKSHIDEventSimpleProvenance`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`, `NSSecureCoding`, `BSDescriptionStreaming`, `NSCopying`, `NSMutableCopying`, `BKSHIDEventProvenance`
- 4 instance variables, 8 properties, 19 instance methods, 6 class methods

## Instance variables

```
@"NSData" _signature;
q _versionedPID;
I _eventType;
Q _timestamp;
```

## Properties

```
@property (T@"NSData",R,N) signature;
@property (Tq,R,N) versionedPID;
@property (TI,R,N) eventType;
@property (TQ,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventSimpleProvenance build:];
+[BKSHIDEventSimpleProvenance supportsBSXPCSecureCoding];
+[BKSHIDEventSimpleProvenance supportsSecureCoding];
+[BKSHIDEventSimpleProvenance protobufSchema];
+[BKSHIDEventSimpleProvenance new];
+[BKSHIDEventSimpleProvenance _withInternalKey:buildMessage:];
```

## Instance methods

```
-[BKSHIDEventSimpleProvenance eventType];
-[BKSHIDEventSimpleProvenance mutableCopyWithZone:];
-[BKSHIDEventSimpleProvenance initForProtobufDecoding];
-[BKSHIDEventSimpleProvenance init];
-[BKSHIDEventSimpleProvenance initWithXPCDictionary:];
-[BKSHIDEventSimpleProvenance timestamp];
-[BKSHIDEventSimpleProvenance _verifySignatureWithInternalKey:];
-[BKSHIDEventSimpleProvenance signature];
-[BKSHIDEventSimpleProvenance versionedPID];
-[BKSHIDEventSimpleProvenance encodeWithXPCDictionary:];
-[BKSHIDEventSimpleProvenance encodeWithCoder:];
-[BKSHIDEventSimpleProvenance hash];
-[BKSHIDEventSimpleProvenance description];
-[BKSHIDEventSimpleProvenance initWithCoder:];
-[BKSHIDEventSimpleProvenance appendDescriptionToStream:];
-[BKSHIDEventSimpleProvenance encodeWithBSXPCCoder:];
-[BKSHIDEventSimpleProvenance initWithBSXPCCoder:];
-[BKSHIDEventSimpleProvenance copyWithZone:];
-[BKSHIDEventSimpleProvenance isEqual:];
```
