# `SBBacklightServicesPlatformProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHServicePlatformProvider`, `SBWindowSceneAttachmentObserving`
- 1 instance variables, 6 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightPlatformProvider" _backlightPlatformProvider;
```

## Properties

```
@property (T@"SBAlwaysOnPolicyCoordinator",R,N) alwaysOnPolicyCoordinator;
@property (T@"<BLSHBacklightPlatformProvider>",R,N,V_backlightPlatformProvider) backlightPlatformProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBacklightServicesPlatformProvider alwaysOnPolicyCoordinator];
-[SBBacklightServicesPlatformProvider init];
-[SBBacklightServicesPlatformProvider windowSceneDidDisconnect:];
-[SBBacklightServicesPlatformProvider initWithBacklightEnvironmentSessionProvider:];
-[SBBacklightServicesPlatformProvider windowSceneDidConnect:];
-[SBBacklightServicesPlatformProvider addSignificantUserInteractionMonitor:];
-[SBBacklightServicesPlatformProvider backlightPlatformProvider];
-[SBBacklightServicesPlatformProvider completeInitializationAfterBLSStartup];
-[SBBacklightServicesPlatformProvider noteSignificantEvent];
-[SBBacklightServicesPlatformProvider removeSignificantUserInteractionMonitor:];
```
