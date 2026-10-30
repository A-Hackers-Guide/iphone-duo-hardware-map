# `_TtC12TextComposer35WritingAssistantResponseXPCEnvelope`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 7 properties, 17 instance methods, 2 class methods

## Instance variables

```
Foundation.Data ? _sessionData;
Foundation.Data ? _statusData;
TextComposer.WritingAssistantServerDraft ? _draft;
_$sSo23TCTextCompositionOutputCSg _message;
Foundation.Data ? _responseMetadataData;
Foundation.Data ? _followUpsData;
Foundation.Data ? _citationsData;
Foundation.Data ? _contentAdvisoriesData;
```

## Properties

```
@property (T@"NSData",N,C) _sessionData;
@property (T@"NSData",N,C) _statusData;
@property (T@"TCTextCompositionOutput",N,&,V_message) _message;
@property (T@"NSData",N,C) _responseMetadataData;
@property (T@"NSData",N,C) _followUpsData;
@property (T@"NSData",N,C) _citationsData;
@property (T@"NSData",N,C) _contentAdvisoriesData;
```

## Class methods

```
+[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope supportsSecureCoding];
+[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope setSupportsSecureCoding:];
```

## Instance methods

```
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _message];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope init];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope encodeWithCoder:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope initWithCoder:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_message:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_statusData:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _citationsData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _contentAdvisoriesData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _followUpsData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _responseMetadataData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _sessionData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope _statusData];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_citationsData:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_contentAdvisoriesData:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_followUpsData:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_responseMetadataData:];
-[_TtC12TextComposer35WritingAssistantResponseXPCEnvelope set_sessionData:];
```
