# `LACGlobalDomainAutoLock` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 10 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"NSNumber",&,N) autoLockMaxOfflineSeconds;
@property (T@"NSNumber",&,N) autoLockMaxUnlockedSeconds;
@property (T@"NSNumber",&,N) autoLockDailyReportHour;
@property (T@"NSNumber",&,N) autoLockSnatchGForceThreshold;
@property (T@"NSNumber",&,N) autoLockSnatchCooldownSeconds;
@property (T@"NSNumber",&,N) autoLockWatchThresholdSeconds;
@property (T@"NSNumber",&,N) autoLockBackoffStrikeThreshold;
@property (T@"NSNumber",&,N) autoLockBackoffCooldownDurationSeconds;
@property (T@"NSSet",&,N) autoLockUninterruptibleFirstPartyBundleIDs;
@property (T@"NSSet",&,N) autoLockUninterruptibleCategories;
```

## Instance methods

```
-[LACGlobalDomainAutoLock autoLockBackoffCooldownDurationSeconds];
-[LACGlobalDomainAutoLock autoLockBackoffStrikeThreshold];
-[LACGlobalDomainAutoLock autoLockDailyReportHour];
-[LACGlobalDomainAutoLock autoLockMaxOfflineSeconds];
-[LACGlobalDomainAutoLock autoLockMaxUnlockedSeconds];
-[LACGlobalDomainAutoLock autoLockSnatchCooldownSeconds];
-[LACGlobalDomainAutoLock autoLockSnatchGForceThreshold];
-[LACGlobalDomainAutoLock autoLockUninterruptibleCategories];
-[LACGlobalDomainAutoLock autoLockUninterruptibleFirstPartyBundleIDs];
-[LACGlobalDomainAutoLock autoLockWatchThresholdSeconds];
-[LACGlobalDomainAutoLock setAutoLockBackoffCooldownDurationSeconds:];
-[LACGlobalDomainAutoLock setAutoLockBackoffStrikeThreshold:];
-[LACGlobalDomainAutoLock setAutoLockDailyReportHour:];
-[LACGlobalDomainAutoLock setAutoLockMaxOfflineSeconds:];
-[LACGlobalDomainAutoLock setAutoLockMaxUnlockedSeconds:];
-[LACGlobalDomainAutoLock setAutoLockSnatchCooldownSeconds:];
-[LACGlobalDomainAutoLock setAutoLockSnatchGForceThreshold:];
-[LACGlobalDomainAutoLock setAutoLockUninterruptibleCategories:];
-[LACGlobalDomainAutoLock setAutoLockUninterruptibleFirstPartyBundleIDs:];
-[LACGlobalDomainAutoLock setAutoLockWatchThresholdSeconds:];
```
