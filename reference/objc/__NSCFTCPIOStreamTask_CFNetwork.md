# `__NSCFTCPIOStreamTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTask`
- 27 instance variables, 1 properties, 52 instance methods, 0 class methods

## Instance variables

```
@? _disavow;
{shared_ptr<TCPIO_EstablishBase>="__ptr_"^{TCPIO_EstablishBase}"__cntrl_"^{__shared_weak_count}} _establish;
{shared_ptr<TransportConnectionObjCPP>="__ptr_"^{TransportConnectionObjCPP}"__cntrl_"^{__shared_weak_count}} _ios;
C _captureStreamsUponCompletion;
C _secure;
@"NSData" __initialDataPayload;
{shared_ptr<HTTPProtocol>="__ptr_"^{HTTPProtocol}"__cntrl_"^{__shared_weak_count}} _httpProtocol;
@"NSMutableArray" _pendingWork;
@"NSMutableArray" _completedSuspendedWork;
B _doingWorkOnThisQueue;
i _connectionState;
B _goneSecure;
B _streamsCaptured;
{?="domain"q"error"i} _readError;
B _readInProgress;
B _readClosed;
{?="domain"q"error"i} _writeError;
B _writeEOF;
B _writeInProgress;
B _writeClosed;
B _receivedServerTrustChallenge;
B _receivedEof;
@"CFNetworkTimer" _writeTimer;
@"CFNetworkTimer" _readTimer;
@"__NSCFURLLocalStreamTaskWorkWrite" _currentWriteTask;
@"__NSCFURLLocalStreamTaskWorkRead" _currentReadTask;
@"NSObject<OS_dispatch_queue>" _workQueueForStreamTask;
```

## Properties

```
@property (T@"NSData",C,V__initialDataPayload) _initialDataPayload;
```

## Instance methods

```
-[__NSCFTCPIOStreamTask _onqueue_adjustLoadingPoolPriority];
-[__NSCFTCPIOStreamTask _onqueue_cancel];
-[__NSCFTCPIOStreamTask _onqueue_resume];
-[__NSCFTCPIOStreamTask _onqueue_suspend];
-[__NSCFTCPIOStreamTask _onqueue_adjustPoolPriority];
-[__NSCFTCPIOStreamTask _task_onqueue_didFinish];
-[__NSCFTCPIOStreamTask _onSessionQueue_disavow];
-[__NSCFTCPIOStreamTask workQueue];
-[__NSCFTCPIOStreamTask dealloc];
-[__NSCFTCPIOStreamTask captureStreams];
-[__NSCFTCPIOStreamTask isKindOfClass:];
-[__NSCFTCPIOStreamTask copyWithZone:];
-[__NSCFTCPIOStreamTask cancel];
-[__NSCFTCPIOStreamTask closeRead];
-[__NSCFTCPIOStreamTask closeWrite];
-[__NSCFTCPIOStreamTask readDataOfMinLength:maxLength:timeout:completionHandler:];
-[__NSCFTCPIOStreamTask startSecureConnection];
-[__NSCFTCPIOStreamTask writeData:timeout:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_dealWithSessionTrustAuth:credential:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_ioTick];
-[__NSCFTCPIOStreamTask _onqueue_postConnectConfiguration:parameters:completionHandler:];
-[__NSCFTCPIOStreamTask shouldDoWorkConsideringTlsState];
-[__NSCFTCPIOStreamTask _initialDataPayload];
-[__NSCFTCPIOStreamTask _onSessionQueue_cleanupAndBreakCycles];
-[__NSCFTCPIOStreamTask _onqueue_addBlockOp:description:];
-[__NSCFTCPIOStreamTask _onqueue_addBlockOp:description:shouldWaitForTls:];
-[__NSCFTCPIOStreamTask _onqueue_callbackCompletedWork];
-[__NSCFTCPIOStreamTask _onqueue_captureStreams];
-[__NSCFTCPIOStreamTask _onqueue_checkForCompletion];
-[__NSCFTCPIOStreamTask _onqueue_cleanUpConnectionEstablishmentState];
-[__NSCFTCPIOStreamTask _onqueue_closeRead];
-[__NSCFTCPIOStreamTask _onqueue_closeWrite];
-[__NSCFTCPIOStreamTask _onqueue_connectionEstablishedWithError:callbackReferent:];
-[__NSCFTCPIOStreamTask _onqueue_dealWithSessionClientCertAuth:credential:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_errorOrCancelError];
-[__NSCFTCPIOStreamTask _onqueue_needClientCert:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_needServerTrust:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_preConnectionConfiguration:parameters:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_processReadWork:];
-[__NSCFTCPIOStreamTask _onqueue_processWriteWork:];
-[__NSCFTCPIOStreamTask _onqueue_sendSessionChallenge:completionHandler:];
-[__NSCFTCPIOStreamTask _onqueue_setTransportConnection:];
-[__NSCFTCPIOStreamTask _onqueue_startSecureConnection];
-[__NSCFTCPIOStreamTask _onqueue_stopSecureConnection];
-[__NSCFTCPIOStreamTask _onqueue_timeoutOccured];
-[__NSCFTCPIOStreamTask _onqueue_tlsCompletion];
-[__NSCFTCPIOStreamTask _onqueue_tlsDisabled];
-[__NSCFTCPIOStreamTask copyStreamProperty:completionHandler:];
-[__NSCFTCPIOStreamTask initWithHost:port:taskGroup:disavow:];
-[__NSCFTCPIOStreamTask initWithTask:connection:extraBytes:disavow:];
-[__NSCFTCPIOStreamTask set_initialDataPayload:];
-[__NSCFTCPIOStreamTask stopSecureConnection];
```
