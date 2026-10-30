# `NWURLSessionRequestBodyData`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLSessionRequestBodyProvider`
- 3 instance variables, 6 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_data>" _data;
Q _length;
Q _offset;
```

## Properties

```
@property (T@"NSDictionary",R,N) trailerFields;
@property (Tq,R,N) countOfBytesSent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWURLSessionRequestBodyData close];
-[NWURLSessionRequestBodyData readMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLSessionRequestBodyData countOfBytesSent];
-[NWURLSessionRequestBodyData trailerFields];
```
