# `NWURLSessionResponseConsumer` (protocol)

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"NSURLResponse",R) response;
@property (T@"NWURLError",R) error;
@property (Tq,R) countOfBytesReceived;
@property (T@"NSURL",R) downloadFileURL;
```

## Instance methods

```
-[NWURLSessionResponseConsumer countOfBytesReceived];
-[NWURLSessionResponseConsumer task:deliverData:complete:error:completionHandler:];
-[NWURLSessionResponseConsumer error];
-[NWURLSessionResponseConsumer populateDownloadResumeInfo:];
-[NWURLSessionResponseConsumer prepareNextRequest:forTask:error:];
-[NWURLSessionResponseConsumer downloadFileURL];
-[NWURLSessionResponseConsumer task:deliverResponse:completionHandler:];
-[NWURLSessionResponseConsumer response];
```
