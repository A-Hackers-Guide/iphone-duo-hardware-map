# `TPSRequestController`

- Image: [`/System/Library/PrivateFrameworks/TelephonyPreferences.framework/TelephonyPreferences`](../userland/System__Library__PrivateFrameworks__TelephonyPreferences.framework__TelephonyPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"TPSRequest" _pendingRequest;
@"NSMapTable" _delegateToQueue;
@"NSMutableOrderedSet" _requests;
@"NSObject<OS_dispatch_queue>" _serialDispatchQueue;
@"CoreTelephonyClient" _telephonyClient;
```

## Properties

```
@property (T@"NSMapTable",R,N,V_delegateToQueue) delegateToQueue;
@property (T@"TPSRequest",&,N,V_pendingRequest) pendingRequest;
@property (T@"NSMutableOrderedSet",&,N,V_requests) requests;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_serialDispatchQueue) serialDispatchQueue;
@property (T@"CoreTelephonyClient",R,N,V_telephonyClient) telephonyClient;
```

## Instance methods

```
-[TPSRequestController removeDelegate:];
-[TPSRequestController addDelegate:queue:];
-[TPSRequestController delegateToQueue];
-[TPSRequestController addRequest:];
-[TPSRequestController init];
-[TPSRequestController requests];
-[TPSRequestController setRequests:];
-[TPSRequestController execute];
-[TPSRequestController telephonyClient];
-[TPSRequestController pendingRequest];
-[TPSRequestController setPendingRequest:];
-[TPSRequestController serialDispatchQueue];
-[TPSRequestController executeRequest:];
-[TPSRequestController postResponse:];
```
