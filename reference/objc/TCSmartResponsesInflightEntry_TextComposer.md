# `TCSmartResponsesInflightEntry`

- Image: [`/System/Library/PrivateFrameworks/TextComposer.framework/TextComposer`](../userland/System__Library__PrivateFrameworks__TextComposer.framework__TextComposer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _callbacks;
@"NSDate" _timestamp;
Q _token;
@? _onEviction;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_callbacks) callbacks;
@property (T@"NSDate",&,N,V_timestamp) timestamp;
@property (TQ,N,V_token) token;
@property (T@?,C,N,V_onEviction) onEviction;
```

## Instance methods

```
-[TCSmartResponsesInflightEntry setTimestamp:];
-[TCSmartResponsesInflightEntry timestamp];
-[TCSmartResponsesInflightEntry callbacks];
-[TCSmartResponsesInflightEntry token];
-[TCSmartResponsesInflightEntry setToken:];
-[TCSmartResponsesInflightEntry addCallback:];
-[TCSmartResponsesInflightEntry initWithCallback:token:onEviction:];
-[TCSmartResponsesInflightEntry onEviction];
-[TCSmartResponsesInflightEntry setOnEviction:];
```
