# `CTStewieEmergencyTextMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageIncoming`, `CTStewieMessageOutgoing`
- 4 instance variables, 8 properties, 18 instance methods, 5 class methods

## Instance variables

```
q _conversationID;
q _sequenceNum;
@"NSString" _text;
q _incomingTextNotifyOption;
```

## Properties

```
@property (Tq,N,V_conversationID) conversationID;
@property (Tq,N,V_sequenceNum) sequenceNum;
@property (T@"NSString",&,N,V_text) text;
@property (Tq,N,V_incomingTextNotifyOption) incomingTextNotifyOption;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieEmergencyTextMessage supportsSecureCoding];
+[CTStewieEmergencyTextMessage maxLengthInBytesForIncomingText];
+[CTStewieEmergencyTextMessage maxLengthInBytesForOutgoingText];
+[CTStewieEmergencyTextMessage estimatedSendTimeForEmergencyText:];
+[CTStewieEmergencyTextMessage maxSequenceNum];
```

## Instance methods

```
-[CTStewieEmergencyTextMessage setConversationID:];
-[CTStewieEmergencyTextMessage conversationID];
-[CTStewieEmergencyTextMessage text];
-[CTStewieEmergencyTextMessage encodeWithCoder:];
-[CTStewieEmergencyTextMessage description];
-[CTStewieEmergencyTextMessage initWithCoder:];
-[CTStewieEmergencyTextMessage setText:];
-[CTStewieEmergencyTextMessage copyWithZone:];
-[CTStewieEmergencyTextMessage isEqual:];
-[CTStewieEmergencyTextMessage setSequenceNum:];
-[CTStewieEmergencyTextMessage estimatedSendTime];
-[CTStewieEmergencyTextMessage incomingTextNotifyOption];
-[CTStewieEmergencyTextMessage initIncomingTextMessageWithConversationID:sequenceNum:emergencyText:notifyOption:error:];
-[CTStewieEmergencyTextMessage initWithConversationID:sequenceNum:emergencyText:error:];
-[CTStewieEmergencyTextMessage initWithConversationIDInternal:sequenceNum:emergencyText:maxTextLength:error:];
-[CTStewieEmergencyTextMessage isEqualToEmergencyTextMessage:];
-[CTStewieEmergencyTextMessage sequenceNum];
-[CTStewieEmergencyTextMessage setIncomingTextNotifyOption:];
```
