# `NWURLSessionRequestBodyFile`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLSessionRequestBodyProvider`
- 4 instance variables, 6 properties, 4 instance methods, 0 class methods

## Instance variables

```
i _error;
@"NSObject<OS_dispatch_io>" _io;
@"NSObject<OS_dispatch_queue>" _queue;
q _bytesSent;
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
-[NWURLSessionRequestBodyFile close];
-[NWURLSessionRequestBodyFile readMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLSessionRequestBodyFile countOfBytesSent];
-[NWURLSessionRequestBodyFile trailerFields];
```
