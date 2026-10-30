# `CTLazuliGroupChatInformation`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _secure;
@"CTLazuliGroupChatParticipantList" _participants;
@"CTLazuliGroupChatConversationID" _conversationID;
@"CTLazuliGroupChatContributionID" _contributionID;
@"CTLazuliGroupChatUri" _remoteUri;
@"CTLazuliGroupChatSubject" _subject;
q _subjectState;
@"CTLazuliGroupChatIcon" _icon;
@"CTLazuliGroupChatParticipant" _mastermind;
```

## Properties

```
@property (T@"CTLazuliGroupChatParticipantList",&,N,V_participants) participants;
@property (T@"CTLazuliGroupChatConversationID",&,N,V_conversationID) conversationID;
@property (T@"CTLazuliGroupChatContributionID",&,N,V_contributionID) contributionID;
@property (T@"CTLazuliGroupChatUri",&,N,V_remoteUri) remoteUri;
@property (T@"CTLazuliGroupChatSubject",&,N,V_subject) subject;
@property (Tq,N,V_subjectState) subjectState;
@property (T@"CTLazuliGroupChatIcon",&,N,V_icon) icon;
@property (T@"CTLazuliGroupChatParticipant",&,N,V_mastermind) mastermind;
@property (TB,N,V_secure) secure;
```

## Class methods

```
+[CTLazuliGroupChatInformation supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliGroupChatInformation setSubject:];
-[CTLazuliGroupChatInformation setConversationID:];
-[CTLazuliGroupChatInformation setSecure:];
-[CTLazuliGroupChatInformation conversationID];
-[CTLazuliGroupChatInformation subject];
-[CTLazuliGroupChatInformation setIcon:];
-[CTLazuliGroupChatInformation setParticipants:];
-[CTLazuliGroupChatInformation encodeWithCoder:];
-[CTLazuliGroupChatInformation description];
-[CTLazuliGroupChatInformation initWithCoder:];
-[CTLazuliGroupChatInformation copyWithZone:];
-[CTLazuliGroupChatInformation participants];
-[CTLazuliGroupChatInformation isEqual:];
-[CTLazuliGroupChatInformation icon];
-[CTLazuliGroupChatInformation secure];
-[CTLazuliGroupChatInformation contributionID];
-[CTLazuliGroupChatInformation initWithReflection:];
-[CTLazuliGroupChatInformation isEqualToCTLazuliGroupChatInformation:];
-[CTLazuliGroupChatInformation mastermind];
-[CTLazuliGroupChatInformation remoteUri];
-[CTLazuliGroupChatInformation setContributionID:];
-[CTLazuliGroupChatInformation setMastermind:];
-[CTLazuliGroupChatInformation setRemoteUri:];
-[CTLazuliGroupChatInformation setSubjectState:];
-[CTLazuliGroupChatInformation subjectState];
```
