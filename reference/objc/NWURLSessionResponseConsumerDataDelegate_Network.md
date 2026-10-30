# `NWURLSessionResponseConsumerDataDelegate`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLSessionResponseConsumer`
- 4 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _hasCompleted;
@"NSURLResponse" _currentResponse;
@"NWURLError" _internalError;
q _countOfBytesReceivedInternal;
```

## Properties

```
@property (T@"NSURLResponse",R) response;
@property (T@"NWURLError",R) error;
@property (Tq,R) countOfBytesReceived;
@property (T@"NSURL",R) downloadFileURL;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NWURLSessionResponseConsumerDataDelegate countOfBytesReceived];
-[NWURLSessionResponseConsumerDataDelegate task:deliverData:complete:error:completionHandler:];
-[NWURLSessionResponseConsumerDataDelegate error];
-[NWURLSessionResponseConsumerDataDelegate populateDownloadResumeInfo:];
-[NWURLSessionResponseConsumerDataDelegate prepareNextRequest:forTask:error:];
-[NWURLSessionResponseConsumerDataDelegate downloadFileURL];
-[NWURLSessionResponseConsumerDataDelegate task:deliverResponse:completionHandler:];
-[NWURLSessionResponseConsumerDataDelegate response];
```
