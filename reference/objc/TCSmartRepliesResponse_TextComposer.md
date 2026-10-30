# `TCSmartRepliesResponse`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
i _inferenceStatus;
@"NSArray" _responses;
@"NSDictionary" _options;
```

## Properties

```
@property (T@"NSArray",R,C,N) responseTexts;
@property (T@"NSArray",R,C,N,V_responses) responses;
@property (Ti,R,N,V_inferenceStatus) inferenceStatus;
@property (T@"NSDictionary",R,C,V_options) options;
```

## Class methods

```
+[TCSmartRepliesResponse supportsSecureCoding];
```

## Instance methods

```
-[TCSmartRepliesResponse encodeWithCoder:];
-[TCSmartRepliesResponse hash];
-[TCSmartRepliesResponse initWithCoder:];
-[TCSmartRepliesResponse options];
-[TCSmartRepliesResponse copyWithZone:];
-[TCSmartRepliesResponse isEqual:];
-[TCSmartRepliesResponse initWithResponses:];
-[TCSmartRepliesResponse responses];
-[TCSmartRepliesResponse responseTexts];
-[TCSmartRepliesResponse responsesArePersonalized];
-[TCSmartRepliesResponse inferenceStatus];
-[TCSmartRepliesResponse initWithResponses:inferenceStatus:];
-[TCSmartRepliesResponse initWithResponses:inferenceStatus:options:];
```
