# `CTCAConversationState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _committed;
B _endSessionOffered;
q _requestReason;
@"NSNumber" _conversationId;
q _fromService;
```

## Properties

```
@property (Tq,N,V_requestReason) requestReason;
@property (T@"NSNumber",&,N,V_conversationId) conversationId;
@property (TB,N,V_committed) committed;
@property (Tq,N,V_fromService) fromService;
@property (TB,N,V_endSessionOffered) endSessionOffered;
```

## Class methods

```
+[CTCAConversationState supportsSecureCoding];
```

## Instance methods

```
-[CTCAConversationState conversationId];
-[CTCAConversationState setCommitted:];
-[CTCAConversationState setConversationId:];
-[CTCAConversationState requestReason];
-[CTCAConversationState encodeWithCoder:];
-[CTCAConversationState description];
-[CTCAConversationState initWithCoder:];
-[CTCAConversationState copyWithZone:];
-[CTCAConversationState setRequestReason:];
-[CTCAConversationState setFromService:];
-[CTCAConversationState committed];
-[CTCAConversationState endSessionOffered];
-[CTCAConversationState fromService];
-[CTCAConversationState setEndSessionOffered:];
```
