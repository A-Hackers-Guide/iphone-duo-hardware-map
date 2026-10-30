# `CTStewieIMessageLiteMessageOutgoing`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageOutgoing`
- 6 instance variables, 10 properties, 20 instance methods, 4 class methods

## Instance variables

```
B _isRelay;
@"NSNumber" _myShortHandle;
@"NSNumber" _otherShortHandle;
q _partNumber;
q _totalParts;
@"NSData" _payload;
```

## Properties

```
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
+[CTStewieIMessageLiteMessageOutgoing supportsSecureCoding];
+[CTStewieIMessageLiteMessageOutgoing estimatedSendTimeForPayload:];
+[CTStewieIMessageLiteMessageOutgoing maxLengthInBytesForPayload];
+[CTStewieIMessageLiteMessageOutgoing maxNumberOfParts];
```

## Instance methods

```
-[CTStewieIMessageLiteMessageOutgoing setIsRelay:];
-[CTStewieIMessageLiteMessageOutgoing isRelay];
-[CTStewieIMessageLiteMessageOutgoing payload];
-[CTStewieIMessageLiteMessageOutgoing setPayload:];
-[CTStewieIMessageLiteMessageOutgoing encodeWithCoder:];
-[CTStewieIMessageLiteMessageOutgoing description];
-[CTStewieIMessageLiteMessageOutgoing initWithCoder:];
-[CTStewieIMessageLiteMessageOutgoing copyWithZone:];
-[CTStewieIMessageLiteMessageOutgoing isEqual:];
-[CTStewieIMessageLiteMessageOutgoing partNumber];
-[CTStewieIMessageLiteMessageOutgoing isEqualToOther:];
-[CTStewieIMessageLiteMessageOutgoing initWithMyShortHandle:otherShortHandle:partNumber:totalParts:payload:error:];
-[CTStewieIMessageLiteMessageOutgoing initWithMyShortHandle:otherShortHandle:partNumber:totalParts:payload:isRelay:error:];
-[CTStewieIMessageLiteMessageOutgoing myShortHandle];
-[CTStewieIMessageLiteMessageOutgoing otherShortHandle];
-[CTStewieIMessageLiteMessageOutgoing setMyShortHandle:];
-[CTStewieIMessageLiteMessageOutgoing setOtherShortHandle:];
-[CTStewieIMessageLiteMessageOutgoing setPartNumber:];
-[CTStewieIMessageLiteMessageOutgoing setTotalParts:];
-[CTStewieIMessageLiteMessageOutgoing totalParts];
```
