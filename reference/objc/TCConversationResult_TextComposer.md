# `TCConversationResult`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSString" _conversation;
@"NSString" _lastMessage;
@"NSString" _preferredLanguage;
@"NSArray" _resultArray;
```

## Properties

```
@property (T@"NSString",R,C,N,V_conversation) conversation;
@property (T@"NSString",R,C,N,V_lastMessage) lastMessage;
@property (T@"NSString",R,C,N,V_preferredLanguage) preferredLanguage;
@property (T@"NSArray",R,C,N,V_resultArray) resultArray;
```

## Class methods

```
+[TCConversationResult resultWithConversation:lastMessage:preferredLanguage:resultArray:];
```

## Instance methods

```
-[TCConversationResult preferredLanguage];
-[TCConversationResult lastMessage];
-[TCConversationResult conversation];
-[TCConversationResult resultArray];
```
