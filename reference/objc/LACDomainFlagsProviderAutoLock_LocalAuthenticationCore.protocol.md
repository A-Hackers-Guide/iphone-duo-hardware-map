# `LACDomainFlagsProviderAutoLock` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 20 properties, 20 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,N) flagAutoLockMaxOfflineSecondsKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockMaxOfflineSeconds;
@property (T@"NSString",R,N) flagAutoLockMaxUnlockedSecondsKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockMaxUnlockedSeconds;
@property (T@"NSString",R,N) flagAutoLockDailyReportHourKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockDailyReportHour;
@property (T@"NSString",R,N) flagAutoLockSnatchGForceThresholdKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockSnatchGForceThreshold;
@property (T@"NSString",R,N) flagAutoLockSnatchCooldownSecondsKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockSnatchCooldownSeconds;
@property (T@"NSString",R,N) flagAutoLockWatchThresholdSecondsKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockWatchThresholdSeconds;
@property (T@"NSString",R,N) flagAutoLockBackoffStrikeThresholdKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockBackoffStrikeThreshold;
@property (T@"NSString",R,N) flagAutoLockBackoffCooldownDurationSecondsKey;
@property (T@"NSNumber",R,N) valueForFlagAutoLockBackoffCooldownDurationSeconds;
@property (T@"NSString",R,N) flagAutoLockUninterruptibleFirstPartyBundleIDsKey;
@property (T@"NSString",R,N) valueForFlagAutoLockUninterruptibleFirstPartyBundleIDs;
@property (T@"NSString",R,N) flagAutoLockUninterruptibleCategoriesKey;
@property (T@"NSString",R,N) valueForFlagAutoLockUninterruptibleCategories;
```

## Instance methods

```
-[LACDomainFlagsProviderAutoLock flagAutoLockBackoffCooldownDurationSecondsKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockBackoffStrikeThresholdKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockDailyReportHourKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockMaxOfflineSecondsKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockMaxUnlockedSecondsKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockSnatchCooldownSecondsKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockSnatchGForceThresholdKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockUninterruptibleCategoriesKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockUninterruptibleFirstPartyBundleIDsKey];
-[LACDomainFlagsProviderAutoLock flagAutoLockWatchThresholdSecondsKey];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockBackoffCooldownDurationSeconds];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockBackoffStrikeThreshold];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockDailyReportHour];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockMaxOfflineSeconds];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockMaxUnlockedSeconds];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockSnatchCooldownSeconds];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockSnatchGForceThreshold];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockUninterruptibleCategories];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockUninterruptibleFirstPartyBundleIDs];
-[LACDomainFlagsProviderAutoLock valueForFlagAutoLockWatchThresholdSeconds];
```
