# `BWCameraStreamingMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SDUDisplayRegionBlankingStateObserver`
- 13 instance variables, 4 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _activeStreamUniqueIDsByClientPID;
@"STMediaStatusDomainPublisher" _mediaStatusDomainPublisher;
@"NSObject<OS_dispatch_queue>" _cameraStreamingMonitorQueue;
B _msnReportingEnabled;
B _systemStatusReportingEnabled;
@"NSMutableDictionary" _clientInfoByPID;
@"NSMutableDictionary" _managedClientInfoByBundleID;
@"PAAccessLogger" _privacyAccountingAccessLogger;
@"NSMutableDictionary" _clientSessionsBySessionID;
@"NSMutableArray" _activeClientSessionIDs;
@"<BSInvalidatable>" _displayRegionBlankingAssertion;
@"<BSInvalidatable>" _displayRegionBlankingObserver;
@"NSString" _displayRegionBlankingAssertionClientID;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCameraStreamingMonitor initialize];
+[BWCameraStreamingMonitor sharedCameraStreamingMonitor];
```

## Instance methods

```
-[BWCameraStreamingMonitor dealloc];
-[BWCameraStreamingMonitor displayRegion:blankingStateDidChangeFrom:to:];
-[BWCameraStreamingMonitor displayRegion:blankingStateWillChangeFrom:to:];
-[BWCameraStreamingMonitor initWithMediaStatusDomainPublisher:msnReportingEnabled:systemStatusReportingEnabled:privacyAccountingAccessLogger:];
-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:];
-[BWCameraStreamingMonitor setSessionStateForSessionID:running:containsVideoSource:clientAuditToken:tccIdentity:mediaEnvironment:sessionIsPrewarming:activePortTypes:completionHandler:];
-[BWCameraStreamingMonitor setStreaming:deviceType:maxFrameRate:streamUniqueID:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:];
```
