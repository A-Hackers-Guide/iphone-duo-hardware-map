# `CWFWiFiUserAgent`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CWFInterface`
- Protocols: `UNUserNotificationCenterDelegate`, `UNUserNotificationCenterDelegatePrivate`
- 18 instance variables, 15 properties, 45 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"CWFCloudSyncManager" _cloudSyncManager;
@"CWFNearbySyncManager" _nearbySyncManager;
@"CWFKeyValueStore" _recentlyRemovedNetworkKVS;
@"CWFKeyValueStore" _nearbyRecommendedNetworksKVS;
@"NSArray" _nearbyRecommendedNetworks;
@"NSObject<OS_dispatch_source>" _nearbyRecommendedNetworksExpirationTimer;
@"NSObject<OS_dispatch_source>" _captiveCredentialsExpirationTimer;
@? _allowCloudSyncableNetworkHandler;
@? _allowNearbySyncableNetworkHandler;
@"UNNotificationRequest" _askToShareUserNotificationRequest;
@"UNUserNotificationCenter" _userNotificationCenter;
@? _presentAskToShareUserNotificationCompletionHandler;
@"BSServiceConnection" _launchAngelConnection;
@"CWFWiFiNetworkSharingClientID" _askToShareProxCardClientID;
@? _presentAskToShareProxCardCompletionHandler;
@? _presentAuthorizationProxCardCompletionHandler;
@"CWFWiFiNetworkSharingClientID" _authorizationProxCardClientID;
```

## Properties

```
@property (T@"NSArray",C,D) nearbyRecommendedNetworks;
@property (T@"UNNotificationRequest",C,V_askToShareUserNotificationRequest) askToShareUserNotificationRequest;
@property (T@"UNUserNotificationCenter",&,V_userNotificationCenter) userNotificationCenter;
@property (T@?,C,V_presentAskToShareUserNotificationCompletionHandler) presentAskToShareUserNotificationCompletionHandler;
@property (T@"BSServiceConnection",&,V_launchAngelConnection) launchAngelConnection;
@property (T@"CWFWiFiNetworkSharingClientID",C,V_askToShareProxCardClientID) askToShareProxCardClientID;
@property (T@?,C,V_presentAskToShareProxCardCompletionHandler) presentAskToShareProxCardCompletionHandler;
@property (T@?,C,V_presentAuthorizationProxCardCompletionHandler) presentAuthorizationProxCardCompletionHandler;
@property (T@"CWFWiFiNetworkSharingClientID",C,V_authorizationProxCardClientID) authorizationProxCardClientID;
@property (T@?,C,V_allowCloudSyncableNetworkHandler) allowCloudSyncableNetworkHandler;
@property (T@?,C,V_allowNearbySyncableNetworkHandler) allowNearbySyncableNetworkHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CWFWiFiUserAgent __receivedNearbySyncableNetwork:];
-[CWFWiFiUserAgent __updateKeychainPassword:network:];
-[CWFWiFiUserAgent nearbyRecommendedNetworks];
-[CWFWiFiUserAgent userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:];
-[CWFWiFiUserAgent allowCloudSyncableNetworkHandler];
-[CWFWiFiUserAgent setNearbyRecommendedNetworks:];
-[CWFWiFiUserAgent launchAngelConnection];
-[CWFWiFiUserAgent __purgeExpiredCaptiveNetworkCredentials];
-[CWFWiFiUserAgent setAllowCloudSyncableNetworkHandler:];
-[CWFWiFiUserAgent initWithXPCClient:requestParameters:];
-[CWFWiFiUserAgent defaultServiceType];
-[CWFWiFiUserAgent __showWiFiNetworkSharingAskToShareNotificationForClientID:network:accessoryDisplayName:completion:];
-[CWFWiFiUserAgent userNotificationCenter];
-[CWFWiFiUserAgent pickerDidDismiss:];
-[CWFWiFiUserAgent setUserNotificationCenter:];
-[CWFWiFiUserAgent setAllowNearbySyncableNetworkHandler:];
-[CWFWiFiUserAgent __setupNearbySyncManager];
-[CWFWiFiUserAgent pickerDidPresent];
-[CWFWiFiUserAgent __updateNearbyRecommendedNetworksExpirationTimer];
-[CWFWiFiUserAgent askToShareProxCardClientID];
-[CWFWiFiUserAgent __receivedNearbyRecommendedNetwork:];
-[CWFWiFiUserAgent __removeAskToShareNotificationWithError:status:debugReason:];
-[CWFWiFiUserAgent setAskToShareUserNotificationRequest:];
-[CWFWiFiUserAgent setAuthorizationProxCardClientID:];
-[CWFWiFiUserAgent setLaunchAngelConnection:];
-[CWFWiFiUserAgent __purgeExpiredNearbyRecommendedNetworks];
-[CWFWiFiUserAgent askToShareUserNotificationRequest];
-[CWFWiFiUserAgent presentAuthorizationProxCardCompletionHandler];
-[CWFWiFiUserAgent presentAskToShareUserNotificationCompletionHandler];
-[CWFWiFiUserAgent invalidate];
-[CWFWiFiUserAgent presentAskToShareProxCardCompletionHandler];
-[CWFWiFiUserAgent __setupCloudSyncManager];
-[CWFWiFiUserAgent activate];
-[CWFWiFiUserAgent __updateNearbyRecommendedNetworks];
-[CWFWiFiUserAgent setPresentAskToShareProxCardCompletionHandler:];
-[CWFWiFiUserAgent setPresentAuthorizationProxCardCompletionHandler:];
-[CWFWiFiUserAgent __setupEventHandler];
-[CWFWiFiUserAgent __launchWiFiNetworkSharingAuthorizationProxCardForAccessoryID:accessoryName:appBundleID:completion:];
-[CWFWiFiUserAgent allowNearbySyncableNetworkHandler];
-[CWFWiFiUserAgent relayPickerCompletion:];
-[CWFWiFiUserAgent __loadNearbyRecommendedNetworksFromKVS];
-[CWFWiFiUserAgent setAskToShareProxCardClientID:];
-[CWFWiFiUserAgent setPresentAskToShareUserNotificationCompletionHandler:];
-[CWFWiFiUserAgent __launchWiFiNetworkSharingAskToShareProxCardForAccessoryID:accessoryName:appBundleID:completion:];
-[CWFWiFiUserAgent authorizationProxCardClientID];
```
