# `CTStewieSatSmsMessageIncoming`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageIncoming`
- 8 instance variables, 12 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"CTXPCServiceSubscriptionContext" _context;
@"NSNumber" _timestamp;
q _pendingTotalCount;
q _pendingCount;
@"NSString" _sourcePhoneNumber;
q _codecID;
@"NSData" _textPayload;
@"NSString" _uniqueID;
```

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_context) context;
@property (T@"NSNumber",&,N,V_timestamp) timestamp;
@property (Tq,N,V_pendingTotalCount) pendingTotalCount;
@property (Tq,N,V_pendingCount) pendingCount;
@property (T@"NSString",&,N,V_sourcePhoneNumber) sourcePhoneNumber;
@property (Tq,N,V_codecID) codecID;
@property (T@"NSData",&,N,V_textPayload) textPayload;
@property (T@"NSString",&,N,V_uniqueID) uniqueID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieSatSmsMessageIncoming supportsSecureCoding];
```

## Instance methods

```
-[CTStewieSatSmsMessageIncoming setTimestamp:];
-[CTStewieSatSmsMessageIncoming timestamp];
-[CTStewieSatSmsMessageIncoming setCodecID:];
-[CTStewieSatSmsMessageIncoming pendingCount];
-[CTStewieSatSmsMessageIncoming uniqueID];
-[CTStewieSatSmsMessageIncoming setContext:];
-[CTStewieSatSmsMessageIncoming encodeWithCoder:];
-[CTStewieSatSmsMessageIncoming description];
-[CTStewieSatSmsMessageIncoming initWithCoder:];
-[CTStewieSatSmsMessageIncoming copyWithZone:];
-[CTStewieSatSmsMessageIncoming codecID];
-[CTStewieSatSmsMessageIncoming context];
-[CTStewieSatSmsMessageIncoming isEqual:];
-[CTStewieSatSmsMessageIncoming setUniqueID:];
-[CTStewieSatSmsMessageIncoming pendingTotalCount];
-[CTStewieSatSmsMessageIncoming setPendingCount:];
-[CTStewieSatSmsMessageIncoming setPendingTotalCount:];
-[CTStewieSatSmsMessageIncoming setTextPayload:];
-[CTStewieSatSmsMessageIncoming isEqualToOther:];
-[CTStewieSatSmsMessageIncoming initWithContext:timestamp:pendingTotalCount:pendingCount:sourcePhoneNumber:codecID:textPayload:uniqueID:error:];
-[CTStewieSatSmsMessageIncoming setSourcePhoneNumber:];
-[CTStewieSatSmsMessageIncoming sourcePhoneNumber];
-[CTStewieSatSmsMessageIncoming textPayload];
```
