# `UIConversationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
q _conversationType;
@"NSString" _threadIdentifier;
@"NSArray" _entries;
@"NSSet" _selfIdentifiers;
@"NSSet" _responsePrimaryRecipientIdentifiers;
@"NSDictionary" _participantNameByIdentifier;
@"NSSet" _secondaryRecipientIdentifiers;
```

## Properties

```
@property (T@"NSSet",&,N,V_secondaryRecipientIdentifiers) secondaryRecipientIdentifiers;
@property (Tq,N,V_conversationType) conversationType;
@property (T@"NSString",C,N,V_threadIdentifier) threadIdentifier;
@property (T@"NSArray",C,N,V_entries) entries;
@property (T@"NSSet",C,N,V_selfIdentifiers) selfIdentifiers;
@property (T@"NSSet",C,N,V_responsePrimaryRecipientIdentifiers) responsePrimaryRecipientIdentifiers;
@property (T@"NSDictionary",C,N,V_participantNameByIdentifier) participantNameByIdentifier;
```

## Instance methods

```
-[UIConversationContext infoDictionary];
-[UIConversationContext entries];
-[UIConversationContext setEntries:];
-[UIConversationContext setThreadIdentifier:];
-[UIConversationContext threadIdentifier];
-[UIConversationContext secondaryRecipientIdentifiers];
-[UIConversationContext selfIdentifiers];
-[UIConversationContext setParticipantNameByIdentifier:];
-[UIConversationContext conversationType];
-[UIConversationContext inputContextHistoryRepresentation];
-[UIConversationContext participantNameByIdentifier];
-[UIConversationContext responsePrimaryRecipientIdentifiers];
-[UIConversationContext setConversationType:];
-[UIConversationContext setResponsePrimaryRecipientIdentifiers:];
-[UIConversationContext setSecondaryRecipientIdentifiers:];
-[UIConversationContext setSelfIdentifiers:];
```
