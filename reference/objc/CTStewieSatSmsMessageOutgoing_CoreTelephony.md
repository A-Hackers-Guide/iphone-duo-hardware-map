# `CTStewieSatSmsMessageOutgoing`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageOutgoing`
- 5 instance variables, 9 properties, 18 instance methods, 3 class methods

## Instance variables

```
B _notifyDowngrade;
@"CTXPCServiceSubscriptionContext" _context;
@"NSString" _destinationPhoneNumber;
q _codecID;
@"NSData" _textPayload;
```

## Properties

```
@property (T@"CTXPCServiceSubscriptionContext",&,N,V_context) context;
@property (T@"NSString",&,N,V_destinationPhoneNumber) destinationPhoneNumber;
@property (Tq,N,V_codecID) codecID;
@property (T@"NSData",&,N,V_textPayload) textPayload;
@property (TB,N,V_notifyDowngrade) notifyDowngrade;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieSatSmsMessageOutgoing supportsSecureCoding];
+[CTStewieSatSmsMessageOutgoing estimatedSendTimeForTextPayload:];
+[CTStewieSatSmsMessageOutgoing maxLengthInBytesForText];
```

## Instance methods

```
-[CTStewieSatSmsMessageOutgoing setCodecID:];
-[CTStewieSatSmsMessageOutgoing setContext:];
-[CTStewieSatSmsMessageOutgoing encodeWithCoder:];
-[CTStewieSatSmsMessageOutgoing description];
-[CTStewieSatSmsMessageOutgoing initWithCoder:];
-[CTStewieSatSmsMessageOutgoing copyWithZone:];
-[CTStewieSatSmsMessageOutgoing codecID];
-[CTStewieSatSmsMessageOutgoing context];
-[CTStewieSatSmsMessageOutgoing isEqual:];
-[CTStewieSatSmsMessageOutgoing setTextPayload:];
-[CTStewieSatSmsMessageOutgoing isEqualToOther:];
-[CTStewieSatSmsMessageOutgoing notifyDowngrade];
-[CTStewieSatSmsMessageOutgoing destinationPhoneNumber];
-[CTStewieSatSmsMessageOutgoing initWithContext:destinationPhoneNumber:codecID:textPayload:error:];
-[CTStewieSatSmsMessageOutgoing initWithContext:destinationPhoneNumber:codecID:textPayload:notifyDowngrade:error:];
-[CTStewieSatSmsMessageOutgoing setDestinationPhoneNumber:];
-[CTStewieSatSmsMessageOutgoing setNotifyDowngrade:];
-[CTStewieSatSmsMessageOutgoing textPayload];
```
