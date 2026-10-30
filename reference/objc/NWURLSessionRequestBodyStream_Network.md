# `NWURLSessionRequestBodyStream`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSStreamDelegate`, `NWURLSessionRequestBodyProvider`
- 6 instance variables, 6 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _streamIsSetup;
@"NSInputStream" _stream;
q _bytesSent;
@"NSObject<OS_dispatch_queue>" _queue;
@"NWURLSessionReadRequest" _readRequest;
@"NSDictionary" _internalTrailerFields;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSDictionary",R,N) trailerFields;
@property (Tq,R,N) countOfBytesSent;
```

## Instance methods

```
-[NWURLSessionRequestBodyStream close];
-[NWURLSessionRequestBodyStream readMinimumIncompleteLength:maximumLength:completionHandler:];
-[NWURLSessionRequestBodyStream countOfBytesSent];
-[NWURLSessionRequestBodyStream trailerFields];
-[NWURLSessionRequestBodyStream stream:handleEvent:];
```
