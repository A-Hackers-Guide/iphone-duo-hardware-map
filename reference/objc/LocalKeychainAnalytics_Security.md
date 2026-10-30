# `LocalKeychainAnalytics`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SFAnalytics`
- 6 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
B _probablyInClassD;
@"NSMutableArray" _pendingReports;
@"NSObject<OS_dispatch_queue>" _queue;
i _notificationToken;
@"NSDate" _backupStartTime;
i _backupType;
```

## Class methods

```
+[LocalKeychainAnalytics databasePath];
```

## Instance methods

```
-[LocalKeychainAnalytics init];
-[LocalKeychainAnalytics canPersistMetrics];
-[LocalKeychainAnalytics processPendingMessages];
-[LocalKeychainAnalytics reportKeychainBackupEnd:error:];
-[LocalKeychainAnalytics reportKeychainBackupStartWithType:];
-[LocalKeychainAnalytics reportKeychainUpgradeFrom:to:outcome:error:];
-[LocalKeychainAnalytics reportKeychainUpgradeOutcome:attributes:];
```
