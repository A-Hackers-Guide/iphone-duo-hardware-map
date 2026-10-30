# `NWURLSessionResponseConsumerDataCompletionHandler`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLSessionResponseConsumer`
- 5 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _hasCompleted;
@? _completionHandler;
@"NSURLResponse" _currentResponse;
@"NWURLError" _internalError;
@"NSObject<OS_dispatch_data>" _data;
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
-[NWURLSessionResponseConsumerDataCompletionHandler countOfBytesReceived];
-[NWURLSessionResponseConsumerDataCompletionHandler task:deliverData:complete:error:completionHandler:];
-[NWURLSessionResponseConsumerDataCompletionHandler error];
-[NWURLSessionResponseConsumerDataCompletionHandler populateDownloadResumeInfo:];
-[NWURLSessionResponseConsumerDataCompletionHandler prepareNextRequest:forTask:error:];
-[NWURLSessionResponseConsumerDataCompletionHandler downloadFileURL];
-[NWURLSessionResponseConsumerDataCompletionHandler task:deliverResponse:completionHandler:];
-[NWURLSessionResponseConsumerDataCompletionHandler response];
```
