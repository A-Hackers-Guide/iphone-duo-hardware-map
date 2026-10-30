# `WAEventRecovery`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 4 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i} _data;
i _apple80211Return;
@"NSString" _recoveryReason;
@"NSString" _recoveryType;
```

## Properties

```
@property (Ti,N,V_apple80211Return) apple80211Return;
@property (T@"NSString",C,N,V_recoveryReason) recoveryReason;
@property (T@"NSString",C,N,V_recoveryType) recoveryType;
```

## Class methods

```
+[WAEventRecovery stringRepresentationWith80211Return:];
```

## Instance methods

```
-[WAEventRecovery processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventRecovery updateRecord:];
-[WAEventRecovery data];
-[WAEventRecovery description];
-[WAEventRecovery recoveryReason];
-[WAEventRecovery setRecoveryReason:];
-[WAEventRecovery recoveryType];
-[WAEventRecovery setRecoveryType:];
-[WAEventRecovery apple80211Return];
-[WAEventRecovery initWithBssid:reason:type:apple80211Return:at:data:withLqmHistory:withError:];
-[WAEventRecovery setApple80211Return:];
```
