# `CTStewieRoadsideTextMessage`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CTStewieMessageIncoming`, `CTStewieMessageOutgoing`
- 4 instance variables, 8 properties, 18 instance methods, 5 class methods

## Instance variables

```
q _conversationID;
q _providerId;
q _sequenceNum;
@"NSString" _text;
```

## Properties

```
@property (Tq,N,V_conversationID) conversationID;
@property (Tq,N,V_providerId) providerId;
@property (Tq,N,V_sequenceNum) sequenceNum;
@property (T@"NSString",&,N,V_text) text;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTStewieRoadsideTextMessage supportsSecureCoding];
+[CTStewieRoadsideTextMessage maxLengthInBytesForIncomingText];
+[CTStewieRoadsideTextMessage maxLengthInBytesForOutgoingText];
+[CTStewieRoadsideTextMessage estimatedSendTimeForRoadsideText:];
+[CTStewieRoadsideTextMessage maxSequenceNum];
```

## Instance methods

```
-[CTStewieRoadsideTextMessage setConversationID:];
-[CTStewieRoadsideTextMessage conversationID];
-[CTStewieRoadsideTextMessage text];
-[CTStewieRoadsideTextMessage encodeWithCoder:];
-[CTStewieRoadsideTextMessage description];
-[CTStewieRoadsideTextMessage initWithCoder:];
-[CTStewieRoadsideTextMessage setText:];
-[CTStewieRoadsideTextMessage copyWithZone:];
-[CTStewieRoadsideTextMessage isEqual:];
-[CTStewieRoadsideTextMessage providerId];
-[CTStewieRoadsideTextMessage setProviderId:];
-[CTStewieRoadsideTextMessage setSequenceNum:];
-[CTStewieRoadsideTextMessage estimatedSendTime];
-[CTStewieRoadsideTextMessage initIncomingTextMessageWithConversationID:providerId:sequenceNum:text:error:];
-[CTStewieRoadsideTextMessage initWithConversationID:providerId:sequenceNum:text:error:];
-[CTStewieRoadsideTextMessage initWithConversationIDInternal:providerId:sequenceNum:text:maxTextLength:error:];
-[CTStewieRoadsideTextMessage isEqualToRoadsideTextMessage:];
-[CTStewieRoadsideTextMessage sequenceNum];
```
