# `LACGlobalDomain`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACGlobalDomain`, `LACGlobalDomainDTO`, `LACGlobalDomainPreboard`, `LACGlobalDomainAutoLock`
- 0 instance variables, 13 properties, 26 instance methods, 24 class methods

## Properties

```
@property (T@"NSNumber",N,&) isDTOStrictModeEnabled;
@property (T@"NSNumber",N,&) dtoBiometricLivenessEnrollmentAgeThreshold;
@property (T@"NSNumber",N,&) autoLockMaxOfflineSeconds;
@property (T@"NSNumber",N,&) autoLockMaxUnlockedSeconds;
@property (T@"NSNumber",N,&) autoLockDailyReportHour;
@property (T@"NSNumber",N,&) autoLockSnatchGForceThreshold;
@property (T@"NSNumber",N,&) autoLockSnatchCooldownSeconds;
@property (T@"NSNumber",N,&) autoLockWatchThresholdSeconds;
@property (T@"NSNumber",N,&) autoLockBackoffStrikeThreshold;
@property (T@"NSNumber",N,&) autoLockBackoffCooldownDurationSeconds;
@property (T@"NSSet",N,C) autoLockUninterruptibleFirstPartyBundleIDs;
@property (T@"NSSet",N,C) autoLockUninterruptibleCategories;
@property (T@"NSNumber",N,&) preboardMode;
```

## Class methods

```
+[LACGlobalDomain sharedInstance];
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

## Instance methods

```
-[LACGlobalDomain autoLockBackoffCooldownDurationSeconds];
-[LACGlobalDomain autoLockBackoffStrikeThreshold];
-[LACGlobalDomain autoLockDailyReportHour];
-[LACGlobalDomain autoLockMaxOfflineSeconds];
-[LACGlobalDomain autoLockMaxUnlockedSeconds];
-[LACGlobalDomain autoLockSnatchCooldownSeconds];
-[LACGlobalDomain autoLockSnatchGForceThreshold];
-[LACGlobalDomain autoLockUninterruptibleCategories];
-[LACGlobalDomain autoLockUninterruptibleFirstPartyBundleIDs];
-[LACGlobalDomain autoLockWatchThresholdSeconds];
-[LACGlobalDomain dtoBiometricLivenessEnrollmentAgeThreshold];
-[LACGlobalDomain isDTOStrictModeEnabled];
-[LACGlobalDomain preboardMode];
-[LACGlobalDomain setAutoLockBackoffCooldownDurationSeconds:];
-[LACGlobalDomain setAutoLockBackoffStrikeThreshold:];
-[LACGlobalDomain setAutoLockDailyReportHour:];
-[LACGlobalDomain setAutoLockMaxOfflineSeconds:];
-[LACGlobalDomain setAutoLockMaxUnlockedSeconds:];
-[LACGlobalDomain setAutoLockSnatchCooldownSeconds:];
-[LACGlobalDomain setAutoLockSnatchGForceThreshold:];
-[LACGlobalDomain setAutoLockUninterruptibleCategories:];
-[LACGlobalDomain setAutoLockUninterruptibleFirstPartyBundleIDs:];
-[LACGlobalDomain setAutoLockWatchThresholdSeconds:];
-[LACGlobalDomain setDtoBiometricLivenessEnrollmentAgeThreshold:];
-[LACGlobalDomain setIsDTOStrictModeEnabled:];
-[LACGlobalDomain setPreboardMode:];
```
