# `CTCARoadsideConversationState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _committed;
@"NSNumber" _conversationId;
@"NSNumber" _providerId;
q _fromService;
```

## Properties

```
@property (T@"NSNumber",&,N,V_conversationId) conversationId;
@property (TB,N,V_committed) committed;
@property (T@"NSNumber",&,N,V_providerId) providerId;
@property (Tq,N,V_fromService) fromService;
```

## Class methods

```
+[CTCARoadsideConversationState supportsSecureCoding];
```

## Instance methods

```
-[CTCARoadsideConversationState conversationId];
-[CTCARoadsideConversationState setCommitted:];
-[CTCARoadsideConversationState setConversationId:];
-[CTCARoadsideConversationState encodeWithCoder:];
-[CTCARoadsideConversationState description];
-[CTCARoadsideConversationState initWithCoder:];
-[CTCARoadsideConversationState copyWithZone:];
-[CTCARoadsideConversationState providerId];
-[CTCARoadsideConversationState setProviderId:];
-[CTCARoadsideConversationState setFromService:];
-[CTCARoadsideConversationState committed];
-[CTCARoadsideConversationState fromService];
```
