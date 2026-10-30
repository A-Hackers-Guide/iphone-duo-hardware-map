# `TCMessage`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 11 instance variables, 11 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _isFromMe;
@"NSString" _text;
@"NSString" _senderIdentifier;
@"NSDate" _timestamp;
@"NSPersonNameComponents" _senderName;
@"NSString" _messageId;
@"NSSet" _primaryRecipientIdentifiers;
@"NSSet" _secondaryRecipientIdentifiers;
@"NSString" _threadIdentifier;
q _entryType;
@"NSString" _spotlightCacheKey;
```

## Properties

```
@property (T@"NSString",R,C,N,V_text) text;
@property (T@"NSString",R,C,N,V_senderIdentifier) senderIdentifier;
@property (T@"NSDate",R,C,N,V_timestamp) timestamp;
@property (T@"NSPersonNameComponents",R,C,N,V_senderName) senderName;
@property (T@"NSString",R,C,N,V_messageId) messageId;
@property (T@"NSSet",R,C,N,V_primaryRecipientIdentifiers) primaryRecipientIdentifiers;
@property (T@"NSSet",R,C,N,V_secondaryRecipientIdentifiers) secondaryRecipientIdentifiers;
@property (T@"NSString",R,C,N,V_threadIdentifier) threadIdentifier;
@property (Tq,R,N,V_entryType) entryType;
@property (T@"NSString",R,C,N,V_spotlightCacheKey) spotlightCacheKey;
@property (TB,R,N,V_isFromMe) isFromMe;
```

## Class methods

```
+[TCMessage sortedMessageEntriesFromInputContextHistory:];
```

## Instance methods

```
-[TCMessage entryType];
-[TCMessage isFromMe];
-[TCMessage text];
-[TCMessage compare:];
-[TCMessage timestamp];
-[TCMessage threadIdentifier];
-[TCMessage secondaryRecipientIdentifiers];
-[TCMessage senderName];
-[TCMessage messageId];
-[TCMessage copyWithZone:];
-[TCMessage primaryRecipientIdentifiers];
-[TCMessage senderIdentifier];
-[TCMessage spotlightCacheKey];
-[TCMessage initWithText:senderIdentifier:timestamp:senderName:messageId:threadIdentifier:entryType:primaryRecipientIdentifiers:secondaryRecipientIdentifiers:spotlightCacheKey:isFromMe:];
```
