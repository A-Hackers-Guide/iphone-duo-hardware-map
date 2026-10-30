# `_TtC12TextComposer34WritingAssistantRequestXPCEnvelope`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 5 properties, 13 instance methods, 2 class methods

## Instance variables

```
_$sSo22TCTextCompositionInputCSg _documentContext;
TextComposer.WritingAssistantServerConversationContext ? _conversationContext;
TextComposer.WritingAssistantServerInput ? _serverInput;
Foundation.Data ? _sessionData;
_$sSS _providedUserPrompt;
_$sSo21TCInputContextHistoryCSg _inputContextHistory;
_$sSSSg _externalContextString;
```

## Properties

```
@property (T@"TCTextCompositionInput",N,&,V_documentContext) _documentContext;
@property (T@"NSData",N,C) _sessionData;
@property (T@"NSString",N,C) _providedUserPrompt;
@property (T@"TCInputContextHistory",N,&,V_inputContextHistory) _inputContextHistory;
@property (T@"NSString",N,C) _externalContextString;
```

## Class methods

```
+[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope supportsSecureCoding];
+[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope setSupportsSecureCoding:];
```

## Instance methods

```
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope init];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope encodeWithCoder:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope initWithCoder:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope _documentContext];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope _externalContextString];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope _inputContextHistory];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope _providedUserPrompt];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope _sessionData];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope set_documentContext:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope set_externalContextString:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope set_inputContextHistory:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope set_providedUserPrompt:];
-[_TtC12TextComposer34WritingAssistantRequestXPCEnvelope set_sessionData:];
```
