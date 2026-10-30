# `WFCredentialsContext`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SFPasswordSharingServiceDelegate`, `WFCredentialsProviderContext`, `WFContextPresenting`
- 15 instance variables, 21 properties, 51 instance methods, 0 class methods

## Instance variables

```
B _enterprise;
B _passwordSharingSupported;
B _shouldReactivatePasswordSharing;
B _passwordReceivedFromPasswordSharing;
@"UIViewController<WFNetworkView>" _provider;
q _availableAuthTraits;
@? _completionHandler;
@? _cancellationHandler;
@"WFNetworkProfile" _profile;
@"WFNetworkScanRecord" _network;
q _requestedFields;
@? _providerCallback;
@"NSArray" _availableTLSIdentities;
@"SFPasswordSharingService" _passwordSharingService;
@"WFHealthIssue" _securityIssue;
```

## Properties

```
@property (T@"WFNetworkProfile",&,N,V_profile) profile;
@property (T@"WFNetworkScanRecord",&,N,V_network) network;
@property (Tq,N,V_requestedFields) requestedFields;
@property (T@?,C,N,V_providerCallback) providerCallback;
@property (T@"NSArray",&,N,V_availableTLSIdentities) availableTLSIdentities;
@property (TB,N,GisEnterprise,V_enterprise) enterprise;
@property (T@"SFPasswordSharingService",&,N,V_passwordSharingService) passwordSharingService;
@property (TB,N,V_shouldReactivatePasswordSharing) shouldReactivatePasswordSharing;
@property (Tq,N,V_availableAuthTraits) availableAuthTraits;
@property (T@"WFHealthIssue",&,N,V_securityIssue) securityIssue;
@property (TB,N,V_passwordReceivedFromPasswordSharing) passwordReceivedFromPasswordSharing;
@property (TB,N,GisPasswordSharingSupported,V_passwordSharingSupported) passwordSharingSupported;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@?,C,N,V_cancellationHandler) cancellationHandler;
@property (T@"NSString",R,N) username;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIViewController<WFNetworkView>",W,N,V_provider) provider;
@property (TB,R,N) needsDismissal;
```

## Instance methods

```
-[WFCredentialsContext appWillResignActive:];
-[WFCredentialsContext isEnterprise];
-[WFCredentialsContext setCompletionHandler:];
-[WFCredentialsContext completionHandler];
-[WFCredentialsContext network];
-[WFCredentialsContext finishWithError:];
-[WFCredentialsContext dealloc];
-[WFCredentialsContext cancellationHandler];
-[WFCredentialsContext username];
-[WFCredentialsContext setProfile:];
-[WFCredentialsContext provider];
-[WFCredentialsContext requestedFields];
-[WFCredentialsContext profile];
-[WFCredentialsContext appDidEnterBackground:];
-[WFCredentialsContext appWillEnterForeground:];
-[WFCredentialsContext setCancellationHandler:];
-[WFCredentialsContext cancel];
-[WFCredentialsContext setProvider:];
-[WFCredentialsContext appDidBecomeActive:];
-[WFCredentialsContext setRequestedFields:];
-[WFCredentialsContext securityMode];
-[WFCredentialsContext setNetwork:];
-[WFCredentialsContext service:receivedNetworkInfo:];
-[WFCredentialsContext launchSettings];
-[WFCredentialsContext isPasswordSharingSupported];
-[WFCredentialsContext service:shouldPromptForNetwork:];
-[WFCredentialsContext shouldReactivatePasswordSharing];
-[WFCredentialsContext activatePasswordSharing];
-[WFCredentialsContext availableAuthTraits];
-[WFCredentialsContext availableTLSIdentities];
-[WFCredentialsContext deactivatePasswordSharingWithReactivation:];
-[WFCredentialsContext finishWithError:forNetwork:profile:];
-[WFCredentialsContext gatherCredentials:];
-[WFCredentialsContext initWithNetwork:profile:];
-[WFCredentialsContext initWithNetwork:profile:authTraits:];
-[WFCredentialsContext needsDismissal];
-[WFCredentialsContext passwordReceivedFromPasswordSharing];
-[WFCredentialsContext passwordSharingService];
-[WFCredentialsContext providerCallback];
-[WFCredentialsContext securityIssue];
-[WFCredentialsContext setAvailableAuthTraits:];
-[WFCredentialsContext setAvailableTLSIdentities:];
-[WFCredentialsContext setEnterprise:];
-[WFCredentialsContext setPasswordReceivedFromPasswordSharing:];
-[WFCredentialsContext setPasswordSharingService:];
-[WFCredentialsContext setPasswordSharingSupported:];
-[WFCredentialsContext setProviderCallback:];
-[WFCredentialsContext setSecurityIssue:];
-[WFCredentialsContext setShouldReactivatePasswordSharing:];
-[WFCredentialsContext validateCredentials];
-[WFCredentialsContext validatePassword];
```
