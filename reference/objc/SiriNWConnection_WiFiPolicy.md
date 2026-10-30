# `SiriNWConnection`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 25 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"NSURL" _url;
@"NSString" _resolvedHost;
I _network_traffic_class;
@"NSObject<OS_nw_connection>" _connection;
@"NSObject<OS_nw_activity>" _activity;
@"NSObject<OS_nw_endpoint>" _endpoint;
@"NSObject<OS_nw_content_context>" _content_context;
@? _wfcompletion;
B _isCanceled;
B _isEstablishing;
B _isReady;
B _usingTLS;
@"NSString" _connectionId;
q _probeLabel;
i _interfaceIndex;
@? _openCompletion;
@"NSObject<OS_dispatch_source>" _openTimer;
@"NSObject<OS_dispatch_source>" _staleConnectionTimer;
Q _readWriteCounter;
@"NSObject<OS_dispatch_source>" _connectionUnviableTimer;
Q _betterPathAvailableNotificationMachTime;
@"NSArray" _attemptedEndpoints;
@"NSError" _mostRecentErrorFromNWConnection;
@"NSString" _reason;
```

## Instance methods

```
-[SiriNWConnection close];
-[SiriNWConnection dealloc];
-[SiriNWConnection _configureConnection:];
-[SiriNWConnection _queue];
-[SiriNWConnection _closeWithError:];
-[SiriNWConnection _setupOpenTimer];
-[SiriNWConnection _invokeOpenCompletionWithError:];
-[SiriNWConnection _cancelOpenTimer];
-[SiriNWConnection _getAttemptedEndpoints];
-[SiriNWConnection _getNWConnectionWithInitialData:completion:];
-[SiriNWConnection _setParametersForHost:useTLS:initialPayload:];
-[SiriNWConnection hasActiveConnection];
-[SiriNWConnection initWithQueueAndCompletion:reason:callback:];
-[SiriNWConnection openConnectionForURL:withConnectionId:initialPayload:completion:];
-[SiriNWConnection resolvedHost];
-[SiriNWConnection runSiriProbeWithDepth:trafficClass:];
```
