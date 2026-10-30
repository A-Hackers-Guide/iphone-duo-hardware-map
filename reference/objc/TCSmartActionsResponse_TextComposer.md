# `TCSmartActionsResponse`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
i _inferenceStatus;
@"NSArray" _responses;
@"NSDictionary" _options;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_responses) responses;
@property (Ti,R,N,V_inferenceStatus) inferenceStatus;
@property (T@"NSDictionary",R,C,V_options) options;
```

## Class methods

```
+[TCSmartActionsResponse supportsSecureCoding];
```

## Instance methods

```
-[TCSmartActionsResponse encodeWithCoder:];
-[TCSmartActionsResponse hash];
-[TCSmartActionsResponse initWithCoder:];
-[TCSmartActionsResponse options];
-[TCSmartActionsResponse copyWithZone:];
-[TCSmartActionsResponse isEqual:];
-[TCSmartActionsResponse responses];
-[TCSmartActionsResponse inferenceStatus];
-[TCSmartActionsResponse initWithResponses:inferenceStatus:options:];
```
