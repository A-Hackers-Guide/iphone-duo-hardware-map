# `SBDeviceApplicationScenePlaceholderContentContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBScenePlaceholderContentContext`, `NSMutableCopying`
- 8 instance variables, 13 properties, 21 instance methods, 0 class methods

## Instance variables

```
q _layoutEnvironment;
@"<SBActivationSettings>" _settings;
@"NSString" _requestedLaunchIdentifier;
@"NSURL" _url;
B _prefersLiveXIB;
Q _preferredContentType;
B _hasOrientationMismatchForClassicApp;
q _sizingPolicy;
```

## Properties

```
@property (T@"<SBActivationSettings>",C,N,V_settings) activationSettings;
@property (Tq,N,V_layoutEnvironment) layoutEnvironment;
@property (T@"NSString",C,N,V_requestedLaunchIdentifier) requestedLaunchIdentifier;
@property (T@"NSURL",C,N,V_url) url;
@property (TB,N,V_prefersLiveXIB) prefersLiveXIB;
@property (TQ,N,V_preferredContentType) preferredContentType;
@property (TB,N,V_hasOrientationMismatchForClassicApp) hasOrientationMismatchForClassicApp;
@property (Tq,N,V_sizingPolicy) sizingPolicy;
@property (TB,R,N) canShowUserContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationScenePlaceholderContentContext mutableCopyWithZone:];
-[SBDeviceApplicationScenePlaceholderContentContext init];
-[SBDeviceApplicationScenePlaceholderContentContext setUrl:];
-[SBDeviceApplicationScenePlaceholderContentContext copyWithZone:];
-[SBDeviceApplicationScenePlaceholderContentContext url];
-[SBDeviceApplicationScenePlaceholderContentContext layoutEnvironment];
-[SBDeviceApplicationScenePlaceholderContentContext setLayoutEnvironment:];
-[SBDeviceApplicationScenePlaceholderContentContext activationSettings];
-[SBDeviceApplicationScenePlaceholderContentContext canShowUserContent];
-[SBDeviceApplicationScenePlaceholderContentContext hasOrientationMismatchForClassicApp];
-[SBDeviceApplicationScenePlaceholderContentContext initWithActivationSettings:];
-[SBDeviceApplicationScenePlaceholderContentContext preferredContentType];
-[SBDeviceApplicationScenePlaceholderContentContext prefersLiveXIB];
-[SBDeviceApplicationScenePlaceholderContentContext requestedLaunchIdentifier];
-[SBDeviceApplicationScenePlaceholderContentContext setActivationSettings:];
-[SBDeviceApplicationScenePlaceholderContentContext setHasOrientationMismatchForClassicApp:];
-[SBDeviceApplicationScenePlaceholderContentContext setPreferredContentType:];
-[SBDeviceApplicationScenePlaceholderContentContext setPrefersLiveXIB:];
-[SBDeviceApplicationScenePlaceholderContentContext setRequestedLaunchIdentifier:];
-[SBDeviceApplicationScenePlaceholderContentContext setSizingPolicy:];
-[SBDeviceApplicationScenePlaceholderContentContext sizingPolicy];
```
