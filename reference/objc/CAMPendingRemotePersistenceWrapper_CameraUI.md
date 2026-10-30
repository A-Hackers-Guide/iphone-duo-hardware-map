# `CAMPendingRemotePersistenceWrapper`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureRequest" _request;
@"NSDate" _creationDate;
@"NSMutableDictionary" _job;
@"NSString" _loggingIdentifier;
@"NSURL" _localDestinationURL;
@"NSString" _batchGroupIdentifier;
@? _completionHandler;
{?="value"q"timescale"i"flags"I"epoch"q} _captureTimestamp;
```

## Properties

```
@property (T@"CAMCaptureRequest",R,N,V_request) request;
@property (T@"NSDate",R,N,V_creationDate) creationDate;
@property (T@"NSMutableDictionary",R,N,V_job) job;
@property (T@"NSString",R,C,N,V_loggingIdentifier) loggingIdentifier;
@property (T{?=qiIq},R,N,V_captureTimestamp) captureTimestamp;
@property (T@"NSURL",R,C,N,V_localDestinationURL) localDestinationURL;
@property (T@"NSString",R,C,N,V_batchGroupIdentifier) batchGroupIdentifier;
@property (T@?,C,N,V_completionHandler) completionHandler;
```

## Instance methods

```
-[CAMPendingRemotePersistenceWrapper setCompletionHandler:];
-[CAMPendingRemotePersistenceWrapper completionHandler];
-[CAMPendingRemotePersistenceWrapper loggingIdentifier];
-[CAMPendingRemotePersistenceWrapper job];
-[CAMPendingRemotePersistenceWrapper creationDate];
-[CAMPendingRemotePersistenceWrapper request];
-[CAMPendingRemotePersistenceWrapper captureTimestamp];
-[CAMPendingRemotePersistenceWrapper localDestinationURL];
-[CAMPendingRemotePersistenceWrapper initWithRequest:creationDate:captureTimestamp:localDestinationURL:job:loggingIdentifier:batchGroupIdentifier:completionHandler:];
-[CAMPendingRemotePersistenceWrapper batchGroupIdentifier];
```
