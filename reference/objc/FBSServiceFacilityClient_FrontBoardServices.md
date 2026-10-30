# `FBSServiceFacilityClient`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSServiceFacilityClientConfiguring`, `FBSServiceFacilityClientMessaging`, `BSInvalidatable`
- 13 instance variables, 8 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
@"NSString" _facilityID;
@"BSServiceQuality" _serviceQuality;
@"BSServiceInterface" _interface;
@ _configOnly_interfaceTarget;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
B _configured;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceConnection" _lock_connection;
B _lock_connectionDenied;
B _lock_activated;
B _lock_invalidated;
B _uisHack;
```

## Properties

```
@property (TB,R,N,GisConfigured,V_configured) configured;
@property (T@"NSString",R,C,N) identifier;
@property (T@"BSServiceQuality",R,N,V_serviceQuality) serviceQuality;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_calloutQueue) calloutQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSServiceFacilityClient defaultShellEndpoint];
```

## Instance methods

```
-[FBSServiceFacilityClient handleError:];
-[FBSServiceFacilityClient _isValid];
-[FBSServiceFacilityClient setCalloutQueue:];
-[FBSServiceFacilityClient calloutQueue];
-[FBSServiceFacilityClient setEndpoint:];
-[FBSServiceFacilityClient identifier];
-[FBSServiceFacilityClient setServiceQuality:];
-[FBSServiceFacilityClient init];
-[FBSServiceFacilityClient handleMessage:withType:];
-[FBSServiceFacilityClient dealloc];
-[FBSServiceFacilityClient setInterface:];
-[FBSServiceFacilityClient invalidate];
-[FBSServiceFacilityClient setIdentifier:];
-[FBSServiceFacilityClient activate];
-[FBSServiceFacilityClient _lock_activate];
-[FBSServiceFacilityClient description];
-[FBSServiceFacilityClient serviceQuality];
-[FBSServiceFacilityClient setInterfaceTarget:];
-[FBSServiceFacilityClient _lock_invalidate];
-[FBSServiceFacilityClient initWithConfigurator:];
-[FBSServiceFacilityClient initWithIdentifier:calloutQueue:];
-[FBSServiceFacilityClient sendMessage:withType:];
-[FBSServiceFacilityClient sendMessage:withType:replyHandler:waitForReply:timeout:];
-[FBSServiceFacilityClient _queue_handleError:];
-[FBSServiceFacilityClient _queue_handleMessage:];
-[FBSServiceFacilityClient configureConnectMessage:];
-[FBSServiceFacilityClient isConfigured];
```
