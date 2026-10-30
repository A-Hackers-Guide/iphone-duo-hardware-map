# `WFCredentialsProviderContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFProviderContext`
- 0 instance variables, 7 properties, 13 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisPasswordSharingSupported) passwordSharingSupported;
@property (T@"NSString",R,N) username;
@property (T@"NSArray",R,N) availableTLSIdentities;
@property (TB,R,N,GisEnterprise) enterprise;
@property (T@"WFHealthIssue",R,N) securityIssue;
@property (Tq,R,N) availableAuthTraits;
@property (TB,R,N) passwordReceivedFromPasswordSharing;
```

## Instance methods

```
-[WFCredentialsProviderContext isEnterprise];
-[WFCredentialsProviderContext username];
-[WFCredentialsProviderContext launchSettings];
-[WFCredentialsProviderContext isPasswordSharingSupported];
-[WFCredentialsProviderContext activatePasswordSharing];
-[WFCredentialsProviderContext availableAuthTraits];
-[WFCredentialsProviderContext availableTLSIdentities];
-[WFCredentialsProviderContext deactivatePasswordSharingWithReactivation:];
-[WFCredentialsProviderContext gatherCredentials:];
-[WFCredentialsProviderContext passwordReceivedFromPasswordSharing];
-[WFCredentialsProviderContext securityIssue];
-[WFCredentialsProviderContext validateCredentials];
-[WFCredentialsProviderContext validatePassword];
```
