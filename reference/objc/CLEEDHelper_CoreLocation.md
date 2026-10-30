# `CLEEDHelper`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CLEEDInterface`, `CLEEDRequestDelegate`
- 3 instance variables, 3 properties, 24 instance methods, 1 class methods

## Instance variables

```
@"<CLEEDRequestDelegate>" _helperDelegate;
@"NSXPCConnection" _fConnection;
@"NSObject<OS_dispatch_queue>" _fClientQueue;
```

## Properties

```
@property (T@"<CLEEDRequestDelegate>",W,N,V_helperDelegate) helperDelegate;
@property (T@"NSXPCConnection",&,N,V_fConnection) fConnection;
@property (T@"NSObject<OS_dispatch_queue>",R,W,N,V_fClientQueue) fClientQueue;
```

## Class methods

```
+[CLEEDHelper validateServerCertificateChallenge:];
```

## Instance methods

```
-[CLEEDHelper cleanup];
-[CLEEDHelper initWithDelegate:queue:];
-[CLEEDHelper dealloc];
-[CLEEDHelper handleInterruption];
-[CLEEDHelper fetchCloakingKeyWithCompletion:];
-[CLEEDHelper fetchMitigationsWithCompletion:];
-[CLEEDHelper setFConnection:];
-[CLEEDHelper fClientQueue];
-[CLEEDHelper fConnection];
-[CLEEDHelper fetchAdrPreCachingStatusWithCompletion:];
-[CLEEDHelper fetchAllPendingRequestsWithCompletion:];
-[CLEEDHelper fetchCurrentMediaUploadRequestWithCompletion:];
-[CLEEDHelper fetchCurrentStreamingRequestWithCompletion:];
-[CLEEDHelper fetchEmergencyContactNamesWithCompletion:];
-[CLEEDHelper fetchPreCachedAdrEnablementStatusWithCompletion:];
-[CLEEDHelper handleRemoteProxyError:forProcessIdentifier:];
-[CLEEDHelper handleResponse:forRequest:completion:];
-[CLEEDHelper helperDelegate];
-[CLEEDHelper mediaUploadList:forRequestID:completion:];
-[CLEEDHelper notifyHelperInvalidation];
-[CLEEDHelper notifyMitigationNeeded:];
-[CLEEDHelper notifyNewRequestAvailable];
-[CLEEDHelper setHelperDelegate:];
-[CLEEDHelper streamingSessionEndedForRequestID:completion:];
```
