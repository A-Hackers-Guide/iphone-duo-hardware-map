# `UIConversationEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSString" _text;
@"NSString" _senderIdentifier;
@"NSDate" _sentDate;
@"NSString" _entryIdentifier;
@"NSString" _replyThreadIdentifier;
@"NSSet" _primaryRecipientIdentifiers;
```

## Properties

```
@property (T@"NSString",C,N,V_text) text;
@property (T@"NSString",C,N,V_senderIdentifier) senderIdentifier;
@property (T@"NSDate",C,N,V_sentDate) sentDate;
@property (T@"NSString",C,N,V_entryIdentifier) entryIdentifier;
@property (T@"NSString",C,N,V_replyThreadIdentifier) replyThreadIdentifier;
@property (T@"NSSet",C,N,V_primaryRecipientIdentifiers) primaryRecipientIdentifiers;
```

## Instance methods

```
-[UIConversationEntry text];
-[UIConversationEntry sentDate];
-[UIConversationEntry entryIdentifier];
-[UIConversationEntry setText:];
-[UIConversationEntry primaryRecipientIdentifiers];
-[UIConversationEntry senderIdentifier];
-[UIConversationEntry inputContextEntryRepresentation];
-[UIConversationEntry setPrimaryRecipientIdentifiers:];
-[UIConversationEntry replyThreadIdentifier];
-[UIConversationEntry setEntryIdentifier:];
-[UIConversationEntry setReplyThreadIdentifier:];
-[UIConversationEntry setSenderIdentifier:];
-[UIConversationEntry setSentDate:];
```
