# `CTStewieEmergencyStartMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageOutgoing`
- 4 instance variables, 8 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _shareEED;
q _conversationID;
@"NSData" _serializedQuestionnaireAnswers;
q _notifyOption;
```

## Properties

```
@property (Tq,N,V_conversationID) conversationID;
@property (T@"NSData",&,N,V_serializedQuestionnaireAnswers) serializedQuestionnaireAnswers;
@property (Tq,N,V_notifyOption) notifyOption;
@property (TB,N,V_shareEED) shareEED;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieEmergencyStartMessage supportsSecureCoding];
```

## Instance methods

```
-[CTStewieEmergencyStartMessage setConversationID:];
-[CTStewieEmergencyStartMessage initWithDictionary:error:];
-[CTStewieEmergencyStartMessage conversationID];
-[CTStewieEmergencyStartMessage encodeWithCoder:];
-[CTStewieEmergencyStartMessage description];
-[CTStewieEmergencyStartMessage initWithCoder:];
-[CTStewieEmergencyStartMessage copyWithZone:];
-[CTStewieEmergencyStartMessage isEqual:];
-[CTStewieEmergencyStartMessage isEqualToEmergencyStartMessage:];
-[CTStewieEmergencyStartMessage estimatedSendTime];
-[CTStewieEmergencyStartMessage notifyOption];
-[CTStewieEmergencyStartMessage serializedQuestionnaireAnswers];
-[CTStewieEmergencyStartMessage setNotifyOption:];
-[CTStewieEmergencyStartMessage setSerializedQuestionnaireAnswers:];
-[CTStewieEmergencyStartMessage setShareEED:];
-[CTStewieEmergencyStartMessage shareEED];
```
