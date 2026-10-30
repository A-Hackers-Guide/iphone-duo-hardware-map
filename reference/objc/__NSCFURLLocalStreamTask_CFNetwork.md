# `__NSCFURLLocalStreamTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionStreamTask`
- 55 instance variables, 18 properties, 82 instance methods, 0 class methods

## Instance variables

```
^{BaseSocketStreamClient=^^?} _socketStreamClient;
@"NSMutableArray" _extraWork;
i _connectionState;
@"NSObject<OS_dispatch_queue>" _workQueueForStreamTask;
^{__CFReadStream=} _readStream;
^{__CFWriteStream=} _writeStream;
@"NSMutableArray" _pendingWork;
B _doingWorkOnThisQueue;
@"NSData" _readBuffer;
B _readSignaled;
B _readEOF;
{?="domain"q"error"i} _readError;
@"NSData" _writeBuffer;
B _writeSignaled;
B _writeEOF;
B _deliveredConnectionEstablished;
{?="domain"q"error"i} _writeError;
q _writeBufferAlreadyWrittenForNextWrite;
@"NSMutableArray" _finalizationQueue;
@"NSMutableArray" _afterConnectQueue;
Q _taskIdentifier;
q _state;
@"NSString" _taskDescription;
@"NSError" _error;
q _countOfBytesReceived;
q _countOfBytesSent;
B _goneSecure;
@"NSObject<OS_dispatch_source>" _tickerTimeoutTimer;
@? _disavow;
@"NSURLRequest" _originalRequest;
@"NSURLRequest" _currentRequest;
@"NSURLResponse" _response;
q _countOfBytesClientExpectsToSend;
q _countOfBytesClientExpectsToReceive;
q _countOfBytesExpectedToSend;
q _countOfBytesExpectedToReceive;
d _timeWindowDelay;
d _timeWindowDuration;
d startTime;
q _priorityValue;
d _loadingPriorityValue;
@"NSString" _boundInterfaceIdentifier;
B _disallowCellular;
C _allowsExpensiveOverride;
C _allowsConstrainedOverride;
C _allowsUltraConstrainedOverride;
C _allowsCellularOverride;
i _networkServiceType;
@"NSDictionary" _legacySocketStreamProperties;
B _betterRouteDiscovered;
@"NSData" __TCPConnectionMetadata;
@"NSData" __initialDataPayload;
B _didIssueCancel;
@"NSUUID" _uniqueIdentifier;
f priority;
```

## Properties

```
@property (T@"NSData",C,V__TCPConnectionMetadata) _TCPConnectionMetadata;
@property (T@"NSData",C,V__initialDataPayload) _initialDataPayload;
@property (TQ,V_taskIdentifier) taskIdentifier;
@property (T@"NSURLRequest",C,V_originalRequest) originalRequest;
@property (T@"NSURLRequest",C,V_currentRequest) currentRequest;
@property (T@"NSURLResponse",C,V_response) response;
@property (Tq,V_countOfBytesClientExpectsToSend) countOfBytesClientExpectsToSend;
@property (Tq,V_countOfBytesClientExpectsToReceive) countOfBytesClientExpectsToReceive;
@property (Tq,V_countOfBytesExpectedToSend) countOfBytesExpectedToSend;
@property (Tq,V_countOfBytesExpectedToReceive) countOfBytesExpectedToReceive;
@property (Tq,V_countOfBytesReceived) countOfBytesReceived;
@property (Tq,V_countOfBytesSent) countOfBytesSent;
@property (Tq,V_state) state;
@property (T@"NSString",C,V_taskDescription) taskDescription;
@property (T@"NSError",C,V_error) error;
@property (TB,R,V_goneSecure) _goneSecure;
@property (Td,D) _timeoutIntervalForResource;
@property (T@"NSUUID",R,C,V_uniqueIdentifier) _uniqueIdentifier;
```

## Instance methods

```
-[__NSCFURLLocalStreamTask currentRequest];
-[__NSCFURLLocalStreamTask taskIdentifier];
-[__NSCFURLLocalStreamTask priority];
-[__NSCFURLLocalStreamTask _onqueue_resume];
-[__NSCFURLLocalStreamTask setError:];
-[__NSCFURLLocalStreamTask setResponse:];
-[__NSCFURLLocalStreamTask setState:];
-[__NSCFURLLocalStreamTask _task_onqueue_didReceiveDispatchData:completionHandler:];
-[__NSCFURLLocalStreamTask _disallowCellular];
-[__NSCFURLLocalStreamTask _task_onqueue_didFinish];
-[__NSCFURLLocalStreamTask suspend];
-[__NSCFURLLocalStreamTask _onSessionQueue_disavow];
-[__NSCFURLLocalStreamTask _timeWindowDelay];
-[__NSCFURLLocalStreamTask _allowsCellularOverride];
-[__NSCFURLLocalStreamTask countOfBytesReceived];
-[__NSCFURLLocalStreamTask setPriority:];
-[__NSCFURLLocalStreamTask workQueue];
-[__NSCFURLLocalStreamTask _timeWindowDuration];
-[__NSCFURLLocalStreamTask dealloc];
-[__NSCFURLLocalStreamTask originalRequest];
-[__NSCFURLLocalStreamTask _adoptEffectiveConfiguration:];
-[__NSCFURLLocalStreamTask _allowsExpensiveOverride];
-[__NSCFURLLocalStreamTask countOfBytesExpectedToSend];
-[__NSCFURLLocalStreamTask _uniqueIdentifier];
-[__NSCFURLLocalStreamTask error];
-[__NSCFURLLocalStreamTask _TCPConnectionMetadata];
-[__NSCFURLLocalStreamTask _cacheOnly];
-[__NSCFURLLocalStreamTask countOfBytesSent];
-[__NSCFURLLocalStreamTask set_TCPConnectionMetadata:];
-[__NSCFURLLocalStreamTask setCurrentRequest:];
-[__NSCFURLLocalStreamTask _networkServiceType];
-[__NSCFURLLocalStreamTask captureStreams];
-[__NSCFURLLocalStreamTask description];
-[__NSCFURLLocalStreamTask countOfBytesExpectedToReceive];
-[__NSCFURLLocalStreamTask _boundInterfaceIdentifier];
-[__NSCFURLLocalStreamTask copyWithZone:];
-[__NSCFURLLocalStreamTask cancel];
-[__NSCFURLLocalStreamTask taskDescription];
-[__NSCFURLLocalStreamTask _allowsUltraConstrainedOverride];
-[__NSCFURLLocalStreamTask _effectiveConfiguration];
-[__NSCFURLLocalStreamTask _allowsConstrainedOverride];
-[__NSCFURLLocalStreamTask resume];
-[__NSCFURLLocalStreamTask state];
-[__NSCFURLLocalStreamTask response];
-[__NSCFURLLocalStreamTask _copySocketStreamProperties];
-[__NSCFURLLocalStreamTask countOfBytesClientExpectsToSend];
-[__NSCFURLLocalStreamTask closeRead];
-[__NSCFURLLocalStreamTask closeWrite];
-[__NSCFURLLocalStreamTask countOfBytesClientExpectsToReceive];
-[__NSCFURLLocalStreamTask readDataOfMinLength:maxLength:timeout:completionHandler:];
-[__NSCFURLLocalStreamTask setCountOfBytesClientExpectsToReceive:];
-[__NSCFURLLocalStreamTask setCountOfBytesClientExpectsToSend:];
-[__NSCFURLLocalStreamTask setOriginalRequest:];
-[__NSCFURLLocalStreamTask setTaskDescription:];
-[__NSCFURLLocalStreamTask setTaskIdentifier:];
-[__NSCFURLLocalStreamTask startSecureConnection];
-[__NSCFURLLocalStreamTask writeData:timeout:completionHandler:];
-[__NSCFURLLocalStreamTask _goneSecure];
-[__NSCFURLLocalStreamTask _initWithExistingTask:disavow:];
-[__NSCFURLLocalStreamTask _initialDataPayload];
-[__NSCFURLLocalStreamTask _legacySocketStreamProperties];
-[__NSCFURLLocalStreamTask _onSessionQueue_cleanupAndBreakCycles];
-[__NSCFURLLocalStreamTask computeAdjustedPoolPriority];
-[__NSCFURLLocalStreamTask copyStreamProperty:completionHandler:];
-[__NSCFURLLocalStreamTask initWithHost:port:taskGroup:disavow:];
-[__NSCFURLLocalStreamTask initWithNetService:taskGroup:disavow:];
-[__NSCFURLLocalStreamTask setCountOfBytesExpectedToReceive:];
-[__NSCFURLLocalStreamTask setCountOfBytesExpectedToSend:];
-[__NSCFURLLocalStreamTask setCountOfBytesReceived:];
-[__NSCFURLLocalStreamTask setCountOfBytesSent:];
-[__NSCFURLLocalStreamTask set_allowsCellularOverride:];
-[__NSCFURLLocalStreamTask set_allowsConstrainedOverride:];
-[__NSCFURLLocalStreamTask set_allowsExpensiveOverride:];
-[__NSCFURLLocalStreamTask set_allowsUltraConstrainedOverride:];
-[__NSCFURLLocalStreamTask set_boundInterfaceIdentifier:];
-[__NSCFURLLocalStreamTask set_disallowCellular:];
-[__NSCFURLLocalStreamTask set_initialDataPayload:];
-[__NSCFURLLocalStreamTask set_legacySocketStreamProperties:];
-[__NSCFURLLocalStreamTask set_networkServiceType:];
-[__NSCFURLLocalStreamTask set_timeWindowDelay:];
-[__NSCFURLLocalStreamTask set_timeWindowDuration:];
-[__NSCFURLLocalStreamTask stopSecureConnection];
```
