# `CTStewieRoadsideStartMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageOutgoing`
- 5 instance variables, 9 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _isPayPerUse;
q _conversationID;
q _providerId;
@"NSString" _phoneNumber;
@"NSData" _serializedQuestionnaireAnswers;
```

## Properties

```
@property (Tq,N,V_conversationID) conversationID;
@property (Tq,N,V_providerId) providerId;
@property (TB,N,V_isPayPerUse) isPayPerUse;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSData",&,N,V_serializedQuestionnaireAnswers) serializedQuestionnaireAnswers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieRoadsideStartMessage supportsSecureCoding];
```

## Instance methods

```
-[CTStewieRoadsideStartMessage phoneNumber];
-[CTStewieRoadsideStartMessage setConversationID:];
-[CTStewieRoadsideStartMessage initWithDictionary:error:];
-[CTStewieRoadsideStartMessage conversationID];
-[CTStewieRoadsideStartMessage setPhoneNumber:];
-[CTStewieRoadsideStartMessage encodeWithCoder:];
-[CTStewieRoadsideStartMessage description];
-[CTStewieRoadsideStartMessage initWithCoder:];
-[CTStewieRoadsideStartMessage copyWithZone:];
-[CTStewieRoadsideStartMessage isEqual:];
-[CTStewieRoadsideStartMessage providerId];
-[CTStewieRoadsideStartMessage setProviderId:];
-[CTStewieRoadsideStartMessage setIsPayPerUse:];
-[CTStewieRoadsideStartMessage estimatedSendTime];
-[CTStewieRoadsideStartMessage isEqualToRoadsideStartMessage:];
-[CTStewieRoadsideStartMessage isPayPerUse];
-[CTStewieRoadsideStartMessage serializedQuestionnaireAnswers];
-[CTStewieRoadsideStartMessage setSerializedQuestionnaireAnswers:];
```
