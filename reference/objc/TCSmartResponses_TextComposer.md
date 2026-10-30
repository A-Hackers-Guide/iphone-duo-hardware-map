# `TCSmartResponses`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"TCSmartRepliesResponse" _repliesResponse;
@"TCSmartActionsResponse" _actionsResponse;
```

## Properties

```
@property (T@"TCSmartRepliesResponse",R,C,N,V_repliesResponse) repliesResponse;
@property (T@"TCSmartActionsResponse",R,C,N,V_actionsResponse) actionsResponse;
```

## Class methods

```
+[TCSmartResponses supportsSecureCoding];
```

## Instance methods

```
-[TCSmartResponses encodeWithCoder:];
-[TCSmartResponses hash];
-[TCSmartResponses initWithCoder:];
-[TCSmartResponses copyWithZone:];
-[TCSmartResponses isEqual:];
-[TCSmartResponses actionsResponse];
-[TCSmartResponses repliesResponse];
-[TCSmartResponses initWithSmartReplyResponse:smartActionResponse:];
```
