# `CWFXPCClient`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFXPCEventProtocolPrivate`, `NSXPCProxyCreating`
- 29 instance variables, 23 properties, 91 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutex;
@"CWFRequestParameters" _checkinRequestParams;
@"NSMutableDictionary" _mutableEventIDMap;
@"NSMutableDictionary" _mutableActivityMap;
@"NSMutableDictionary" _mutableEventCallbackMap;
@"NSMutableDictionary" _mutableEventAckMap;
@"NSXPCConnection" _XPCConnection;
B _invalidated;
q _serviceType;
@"NSObject<OS_dispatch_queue>" _targetQueue;
@? _invalidationHandler;
@? _interruptionHandler;
@? _performWiFiNetworkSharingAccessoryScanHandler;
@? _presentWiFiNetworkSharingAskToShareProxCardHandler;
@? _cancelWiFiNetworkSharingAskToShareProxCardHandler;
@? _presentWiFiNetworkSharingAuthorizationProxCardHandler;
@? _cancelWiFiNetworkSharingAuthorizationProxCardHandler;
@? _presentWiFiNetworkSharingAskToShareUserNotificationHandler;
@? _cancelWiFiNetworkSharingAskToShareUserNotificationHandler;
@? _queryNearbyRecommendedNetworksHandler;
@? _rememberCloudNetworkHandler;
@? _forgetCloudNetworkHandler;
@? _queryCloudNetworksHandler;
@? _dumpLogsHandler;
@? _queryCaptivePortalCredentialsHandler;
@? _setCaptivePortalCredentialsHandler;
@? _nearbyConfirmBrokenBackhaulHandler;
@? _allowBrokenBackhaulPersonalHotspotFallbackHandler;
@"CWFXPCProxyConnection" _remoteXPCProxyConnection;
```

## Properties

```
@property (TB,V_invalidated) invalidated;
@property (T@"CWFXPCProxyConnection",&,N,V_remoteXPCProxyConnection) remoteXPCProxyConnection;
@property (Tq,R,V_serviceType) serviceType;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
@property (T@?,C,V_invalidationHandler) invalidationHandler;
@property (T@?,C,V_interruptionHandler) interruptionHandler;
@property (T@?,C,V_performWiFiNetworkSharingAccessoryScanHandler) performWiFiNetworkSharingAccessoryScanHandler;
@property (T@?,C,V_presentWiFiNetworkSharingAskToShareProxCardHandler) presentWiFiNetworkSharingAskToShareProxCardHandler;
@property (T@?,C,V_cancelWiFiNetworkSharingAskToShareProxCardHandler) cancelWiFiNetworkSharingAskToShareProxCardHandler;
@property (T@?,C,V_presentWiFiNetworkSharingAuthorizationProxCardHandler) presentWiFiNetworkSharingAuthorizationProxCardHandler;
@property (T@?,C,V_cancelWiFiNetworkSharingAuthorizationProxCardHandler) cancelWiFiNetworkSharingAuthorizationProxCardHandler;
@property (T@?,C,V_presentWiFiNetworkSharingAskToShareUserNotificationHandler) presentWiFiNetworkSharingAskToShareUserNotificationHandler;
@property (T@?,C,V_cancelWiFiNetworkSharingAskToShareUserNotificationHandler) cancelWiFiNetworkSharingAskToShareUserNotificationHandler;
@property (T@"CWFXPCProxyConnection",R,&,N) localXPCProxyConnection;
@property (T@?,C,V_queryNearbyRecommendedNetworksHandler) queryNearbyRecommendedNetworksHandler;
@property (T@?,C,V_rememberCloudNetworkHandler) rememberCloudNetworkHandler;
@property (T@?,C,V_forgetCloudNetworkHandler) forgetCloudNetworkHandler;
@property (T@?,C,V_queryCloudNetworksHandler) queryCloudNetworksHandler;
@property (T@?,C,V_dumpLogsHandler) dumpLogsHandler;
@property (T@?,C,V_queryCaptivePortalCredentialsHandler) queryCaptivePortalCredentialsHandler;
@property (T@?,C,V_setCaptivePortalCredentialsHandler) setCaptivePortalCredentialsHandler;
@property (T@?,C,V_nearbyConfirmBrokenBackhaulHandler) nearbyConfirmBrokenBackhaulHandler;
@property (T@?,C,V_allowBrokenBackhaulPersonalHotspotFallbackHandler) allowBrokenBackhaulPersonalHotspotFallbackHandler;
```

## Instance methods

```
-[CWFXPCClient queryCloudNetworksAndReply:];
-[CWFXPCClient setCancelWiFiNetworkSharingAskToShareProxCardHandler:];
-[CWFXPCClient setCaptivePortalCredentialsHandler];
-[CWFXPCClient presentWiFiNetworkSharingAskToShareProxCardHandler];
-[CWFXPCClient queryCloudNetworksHandler];
-[CWFXPCClient presentWiFiNetworkSharingAuthorizationProxCardHandler];
-[CWFXPCClient dumpLogsHandler];
-[CWFXPCClient nearbyConfirmBrokenBackhaulHandler];
-[CWFXPCClient setNearbyConfirmBrokenBackhaulHandler:];
-[CWFXPCClient setQueryCaptivePortalCredentialsHandler:];
-[CWFXPCClient queryCaptivePortalCredentialsHandler];
-[CWFXPCClient queryNearbyRecommendedNetworksHandler];
-[CWFXPCClient forgetCloudNetworkHandler];
-[CWFXPCClient setAllowBrokenBackhaulPersonalHotspotFallbackHandler:];
-[CWFXPCClient presentWiFiNetworkSharingAskToShareUserNotificationHandler];
-[CWFXPCClient cancelWiFiNetworkSharingAuthorizationProxCardHandler];
-[CWFXPCClient performWiFiNetworkSharingAccessoryScanHandler];
-[CWFXPCClient eventHandlerWithEventID:];
-[CWFXPCClient setPresentWiFiNetworkSharingAuthorizationProxCardHandler:];
-[CWFXPCClient setPresentWiFiNetworkSharingAskToShareUserNotificationHandler:];
-[CWFXPCClient rememberCloudNetworkHandler];
-[CWFXPCClient setForgetCloudNetworkHandler:];
-[CWFXPCClient initWithServiceType:endpoint:];
-[CWFXPCClient setSetCaptivePortalCredentialsHandler:];
-[CWFXPCClient setTargetQueue:];
-[CWFXPCClient setPresentWiFiNetworkSharingAskToShareProxCardHandler:];
-[CWFXPCClient setEventHandler:eventID:];
-[CWFXPCClient cancelWiFiNetworkSharingAskToShareUserNotificationHandler];
-[CWFXPCClient setPerformWiFiNetworkSharingAccessoryScanHandler:];
-[CWFXPCClient cancelWiFiNetworkSharingAskToShareProxCardForClientID:];
-[CWFXPCClient setCancelWiFiNetworkSharingAuthorizationProxCardHandler:];
-[CWFXPCClient setQueryNearbyRecommendedNetworksHandler:];
-[CWFXPCClient initWithServiceType:];
-[CWFXPCClient cancelWiFiNetworkSharingAskToShareProxCardHandler];
-[CWFXPCClient targetQueue];
-[CWFXPCClient setQueryCloudNetworksHandler:];
-[CWFXPCClient setDumpLogsHandler:];
-[CWFXPCClient setRememberCloudNetworkHandler:];
-[CWFXPCClient clearAllEventHandlers];
-[CWFXPCClient suspend];
-[CWFXPCClient allowRequestType:];
-[CWFXPCClient invalidated];
-[CWFXPCClient startMonitoringEvent:requestParameters:error:];
-[CWFXPCClient setInvalidationHandler:];
-[CWFXPCClient init];
-[CWFXPCClient receivedXPCEvent:];
-[CWFXPCClient stopMonitoringEvent:requestParameters:];
-[CWFXPCClient remoteXPCProxyConnection];
-[CWFXPCClient dealloc];
-[CWFXPCClient presentWiFiNetworkSharingAskToShareUserNotificationForClientID:network:accessoryName:reply:];
-[CWFXPCClient interruptionHandler];
-[CWFXPCClient presentWiFiNetworkSharingAskToShareProxCardForClientID:accessoryName:reply:];
-[CWFXPCClient synchronousRemoteObjectProxyWithErrorHandler:];
-[CWFXPCClient endAllActivities:];
-[CWFXPCClient __receivedEvent:];
-[CWFXPCClient setInvalidated:];
-[CWFXPCClient remoteObjectProxyWithErrorHandler:];
-[CWFXPCClient performWiFiNetworkSharingAccessoryScanWithReply:];
-[CWFXPCClient invalidate];
-[CWFXPCClient allowBrokenBackhaulPersonalHotspotFallbackHandler];
-[CWFXPCClient __startMonitoringEvent:requestParameters:reply:];
-[CWFXPCClient initWithServiceType:endpoint:remoteXPCProxyConnection:];
-[CWFXPCClient cancelWiFiNetworkSharingAuthorizationProxCardForClientID:];
-[CWFXPCClient activate];
-[CWFXPCClient setInterruptionHandler:];
-[CWFXPCClient endActivity:requestParameters:];
-[CWFXPCClient queryNearbyRecommendedNetworksAndReply:];
-[CWFXPCClient allowBrokenBackhaulPersonalHotspotFallbackForNetwork:reply:];
-[CWFXPCClient initWithServiceType:remoteXPCProxyConnection:];
-[CWFXPCClient localXPCProxyConnection];
-[CWFXPCClient invalidationHandler];
-[CWFXPCClient setRemoteXPCProxyConnection:];
-[CWFXPCClient dumpLogs:reply:];
-[CWFXPCClient beginActivity:requestParameters:error:];
-[CWFXPCClient stopMonitoringAllEvents:];
-[CWFXPCClient remoteObjectProxy];
-[CWFXPCClient forgetCloudNetworkProfile:reply:];
-[CWFXPCClient setCancelWiFiNetworkSharingAskToShareUserNotificationHandler:];
-[CWFXPCClient setCaptivePortalCredentials:knownNetworkProfile:reply:];
-[CWFXPCClient receivedAcknowledgedXPCEvent:reply:];
-[CWFXPCClient queryCaptivePortalCredentialsForKnownNetworkProfile:reply:];
-[CWFXPCClient checkinWithRequestParameters:error:];
-[CWFXPCClient checkinWithRequestParameters:reply:];
-[CWFXPCClient cancelWiFiNetworkSharingAskToShareUserNotificationForClientID:];
-[CWFXPCClient resume];
-[CWFXPCClient nearbyConfirmBrokenBackhaulUsingTimeout:count:network:minimumCacheTimestamp:reply:];
-[CWFXPCClient __beginActivity:requestParameters:reply:];
-[CWFXPCClient serviceType];
-[CWFXPCClient rememberCloudNetworkProfile:reply:];
-[CWFXPCClient presentWiFiNetworkSharingAuthorizationProxCardForClientID:accessoryName:reply:];
-[CWFXPCClient __acknowledgeEventWithUUID:];
```
