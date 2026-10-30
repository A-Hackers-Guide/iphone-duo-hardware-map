# `CTStewieIMessageLiteMessageIncoming`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageIncoming`
- 9 instance variables, 13 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _isRelay;
@"NSNumber" _timestamp;
q _pendingTotalCount;
q _pendingCount;
@"NSNumber" _myShortHandle;
@"NSNumber" _otherShortHandle;
q _partNumber;
q _totalParts;
@"NSData" _payload;
```

## Properties

```
@property (T@"NSNumber",&,N,V_timestamp) timestamp;
@property (Tq,N,V_pendingTotalCount) pendingTotalCount;
@property (Tq,N,V_pendingCount) pendingCount;
@property (T@"NSNumber",&,N,V_myShortHandle) myShortHandle;
@property (T@"NSNumber",&,N,V_otherShortHandle) otherShortHandle;
@property (Tq,N,V_partNumber) partNumber;
@property (Tq,N,V_totalParts) totalParts;
@property (T@"NSData",&,N,V_payload) payload;
@property (TB,N,V_isRelay) isRelay;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieIMessageLiteMessageIncoming supportsSecureCoding];
```

## Instance methods

```
-[CTStewieIMessageLiteMessageIncoming setIsRelay:];
-[CTStewieIMessageLiteMessageIncoming setTimestamp:];
-[CTStewieIMessageLiteMessageIncoming isRelay];
-[CTStewieIMessageLiteMessageIncoming timestamp];
-[CTStewieIMessageLiteMessageIncoming payload];
-[CTStewieIMessageLiteMessageIncoming pendingCount];
-[CTStewieIMessageLiteMessageIncoming setPayload:];
-[CTStewieIMessageLiteMessageIncoming encodeWithCoder:];
-[CTStewieIMessageLiteMessageIncoming description];
-[CTStewieIMessageLiteMessageIncoming initWithCoder:];
-[CTStewieIMessageLiteMessageIncoming copyWithZone:];
-[CTStewieIMessageLiteMessageIncoming isEqual:];
-[CTStewieIMessageLiteMessageIncoming partNumber];
-[CTStewieIMessageLiteMessageIncoming pendingTotalCount];
-[CTStewieIMessageLiteMessageIncoming setPendingCount:];
-[CTStewieIMessageLiteMessageIncoming setPendingTotalCount:];
-[CTStewieIMessageLiteMessageIncoming isEqualToOther:];
-[CTStewieIMessageLiteMessageIncoming initWithTimestamp:pendingTotalCount:pendingCount:myShortHandle:otherShortHandle:partNumber:totalParts:payload:isRelay:error:];
-[CTStewieIMessageLiteMessageIncoming myShortHandle];
-[CTStewieIMessageLiteMessageIncoming otherShortHandle];
-[CTStewieIMessageLiteMessageIncoming setMyShortHandle:];
-[CTStewieIMessageLiteMessageIncoming setOtherShortHandle:];
-[CTStewieIMessageLiteMessageIncoming setPartNumber:];
-[CTStewieIMessageLiteMessageIncoming setTotalParts:];
-[CTStewieIMessageLiteMessageIncoming totalParts];
```
