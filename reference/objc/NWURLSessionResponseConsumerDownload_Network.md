# `NWURLSessionResponseConsumerDownload`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NWURLSessionResponseConsumer`
- 13 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _hasCompleted;
B _isResuming;
B _firstPrepareCalled;
B _calledDidResumeAtOffset;
i _fd;
@? _completionHandler;
@"NSURLResponse" _currentResponse;
@"NSURL" _fileURL;
@"NSString" _tempFileName;
@"NSObject<OS_dispatch_io>" _io;
@? _pendingCompletionBlock;
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
-[NWURLSessionResponseConsumerDownload countOfBytesReceived];
-[NWURLSessionResponseConsumerDownload task:deliverData:complete:error:completionHandler:];
-[NWURLSessionResponseConsumerDownload error];
-[NWURLSessionResponseConsumerDownload populateDownloadResumeInfo:];
-[NWURLSessionResponseConsumerDownload prepareNextRequest:forTask:error:];
-[NWURLSessionResponseConsumerDownload downloadFileURL];
-[NWURLSessionResponseConsumerDownload task:deliverResponse:completionHandler:];
-[NWURLSessionResponseConsumerDownload response];
```
