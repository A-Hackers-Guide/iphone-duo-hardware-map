# `LACGlobalDomain` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 12 properties, 0 instance methods, 23 class methods

## Properties

```
@property (class, T@"NSData",&,N) companionAuthentication;
@property (class, TB,N) isCompanionDeviceMocked;
@property (class, T@"NSNumber",&,N) isMacCompanionSessionActive;
@property (class, T@"NSNumber",&,N) isVisionCompanionSessionActive;
@property (class, TB,N) releaseUIDelegate;
@property (class, TB,N) disableSensitiveUIRedaction;
@property (class, T@"NSNumber",&,N) runningInBATS;
@property (class, T@"NSNumber",&,N) simulatorPasscodeType;
@property (class, TB,N) useTestAppleKeyStoreDaemon;
@property (class, T@"NSNumber",&,N) isSharedModeActive;
@property (class, T@"NSNumber",&,N) sharedModeLatency;
@property (class, TB,R,N) osVariantAllowsDomainOverrides;
```

## Class methods

```
+[LACGlobalDomain releaseUIDelegate];
+[LACGlobalDomain setDisableSensitiveUIRedaction:];
+[LACGlobalDomain setIsMacCompanionSessionActive:];
+[LACGlobalDomain companionAuthentication];
+[LACGlobalDomain disableSensitiveUIRedaction];
+[LACGlobalDomain isCompanionDeviceMocked];
+[LACGlobalDomain isMacCompanionSessionActive];
+[LACGlobalDomain isSharedModeActive];
+[LACGlobalDomain isVisionCompanionSessionActive];
+[LACGlobalDomain osVariantAllowsDomainOverrides];
+[LACGlobalDomain runningInBATS];
+[LACGlobalDomain setCompanionAuthentication:];
+[LACGlobalDomain setIsCompanionDeviceMocked:];
+[LACGlobalDomain setIsSharedModeActive:];
+[LACGlobalDomain setIsVisionCompanionSessionActive:];
+[LACGlobalDomain setReleaseUIDelegate:];
+[LACGlobalDomain setRunningInBATS:];
+[LACGlobalDomain setSharedModeLatency:];
+[LACGlobalDomain setSimulatorPasscodeType:];
+[LACGlobalDomain setUseTestAppleKeyStoreDaemon:];
+[LACGlobalDomain sharedModeLatency];
+[LACGlobalDomain simulatorPasscodeType];
+[LACGlobalDomain useTestAppleKeyStoreDaemon];
```
