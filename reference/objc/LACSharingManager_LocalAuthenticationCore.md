# `LACSharingManager`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFAuthenticationManagerDelegate`, `LACSharingManaging`
- 5 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _canAuthenticateSessions;
@"SFAuthenticationManager" _sharingManager;
@"NSObject<OS_dispatch_queue>" _replyQueue;
@"NSObject<OS_dispatch_queue>" _workQueue;
@"<LACSharingManagerDelegate>" delegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<LACSharingManagerDelegate>",W,N,Vdelegate) delegate;
```

## Class methods

```
+[LACSharingManager isSharingError:];
```

## Instance methods

```
-[LACSharingManager setDelegate:];
-[LACSharingManager delegate];
-[LACSharingManager initWithReplyQueue:];
-[LACSharingManager manager:didCompleteAuthenticationForSessionWithID:];
-[LACSharingManager manager:didFailAuthenticationForSessionWithID:error:];
-[LACSharingManager manager:didStartAuthenticationForSessionWithID:];
-[LACSharingManager _authenticateWithRequest:completion:];
-[LACSharingManager _authenticationBackgroundTaskForRequest:];
-[LACSharingManager _authenticationTypeForCompanion:];
-[LACSharingManager _canAuthenticateBackgroundTaskWithCompanion:];
-[LACSharingManager _canAuthenticateWithCompanion:completion:];
-[LACSharingManager _failSessionWithID:error:];
-[LACSharingManager _pairedDeviceTypeForCompanion:];
-[LACSharingManager _pairedDevicesForCompanion:completion:];
-[LACSharingManager _runPairedDevicesBackgroundTaskForCompanion:completion:];
-[LACSharingManager authenticateWithRequest:];
-[LACSharingManager canAuthenticateWithCompanion:completion:];
-[LACSharingManager cancelSessionWithID:];
-[LACSharingManager getPairedDevicesBackgroundTaskForCompanion:];
-[LACSharingManager pairedDevicesForCompanion:completion:];
```
