# `__NSCFURLLocalSessionConnection`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFURLSessionConnection`
- Protocols: `NSURLAuthenticationChallengeSender`, `NSCopying`
- 19 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
^{SessionConnectionLoadable=^^?^^?^^?@} _loaderClient;
^{URLConnectionLoader=^^?^{__CFAllocator}^^?CC^{InterfaceRequiredForLoader}@^^?^^?@@q^{RedirectionRecorder}CCC@CddC^{URLProtocol}@{os_unfair_lock_s=I}C^{CoreSchedulingSet}ddQ{ConfigFlags=b1b1b1b1b1b1b1b1}CCCCQICB} _loader;
B _canceled;
q _suspended;
@"NSObject<OS_dispatch_data>" _pendingData;
q _pendingCompletion;
Q _didReceiveResponseDisposition;
@"NSError" _pendingError;
i _state;
q _clientBufferLength;
@"NSObject<OS_dispatch_data>" _sniffData;
@"NSURLResponse" _sniffResponse;
B _isMixedReplace;
B _didCheckMixedReplace;
B _didCheckCredentialsSuppliedInURL;
B _actuallyTriedCredentialsSuppliedInURL;
Q _maxDataSegmentCoalesceThreshhold;
Q _maxDataSegmentCount;
I _didReceiveDataCount;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFURLLocalSessionConnection setBytesPerSecondLimit:];
-[__NSCFURLLocalSessionConnection setIsDownload:];
-[__NSCFURLLocalSessionConnection _alternatePathAvailable:];
-[__NSCFURLLocalSessionConnection suspend];
-[__NSCFURLLocalSessionConnection _didReceiveResponse:sniff:];
-[__NSCFURLLocalSessionConnection setPoolPriority:];
-[__NSCFURLLocalSessionConnection expectedProgressTargetChanged];
-[__NSCFURLLocalSessionConnection setPriorityHint:incremental:];
-[__NSCFURLLocalSessionConnection withLoaderAsync:];
-[__NSCFURLLocalSessionConnection initWithTask:delegate:delegateQueue:];
-[__NSCFURLLocalSessionConnection _conditionalRequirementsChanged:];
-[__NSCFURLLocalSessionConnection _needNewBodyStream];
-[__NSCFURLLocalSessionConnection dealloc];
-[__NSCFURLLocalSessionConnection _didSendBodyData:];
-[__NSCFURLLocalSessionConnection continueWithoutCredentialForAuthenticationChallenge:];
-[__NSCFURLLocalSessionConnection _didFinishWithError:];
-[__NSCFURLLocalSessionConnection _ackBytes:];
-[__NSCFURLLocalSessionConnection _didReceiveData:];
-[__NSCFURLLocalSessionConnection useCredential:forAuthenticationChallenge:];
-[__NSCFURLLocalSessionConnection _didUseCachedResponse];
-[__NSCFURLLocalSessionConnection cancelAuthenticationChallenge:];
-[__NSCFURLLocalSessionConnection _didReceiveChallenge:];
-[__NSCFURLLocalSessionConnection _capturedSocketInputStream:outputStream:];
-[__NSCFURLLocalSessionConnection _redirectRequest:redirectResponse:completion:];
-[__NSCFURLLocalSessionConnection _willSendRequestForEstablishedConnection:completion:];
-[__NSCFURLLocalSessionConnection cancel];
-[__NSCFURLLocalSessionConnection _needNewBodyStreamFromOffset:];
-[__NSCFURLLocalSessionConnection _didReceiveInformationalResponse:];
-[__NSCFURLLocalSessionConnection _captureTransportConnection:extraBytes:];
-[__NSCFURLLocalSessionConnection _connectionIsWaitingWithReason:];
-[__NSCFURLLocalSessionConnection resume];
```
