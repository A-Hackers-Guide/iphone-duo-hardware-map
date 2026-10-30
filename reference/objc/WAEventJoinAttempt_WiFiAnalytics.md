# `WAEventJoinAttempt`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WAEvent`
- 4 instance variables, 4 properties, 14 instance methods, 2 class methods

## Instance variables

```
{?="band"s"channel"s"channelWidth"s"motionState"s"reason"i"rssi"s"status"i"subreason"i"isUsrPreference"B"networkAuthFlags"s"networkFlags"i"networkIsHome"B"networkIsWork"B"deauth_source_oui"[3C]"bssid_oui"[3C]} _data;
@"NSString" _ssid;
@"NSString" _apProfileID;
@"NSString" _security;
```

## Properties

```
@property (T@"NSString",&,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_apProfileID) apProfileID;
@property (T@"NSString",C,N,V_security) security;
@property (T@"NSString",R,D,N) bssid;
```

## Class methods

```
+[WAEventJoinAttempt joinReasonAsString:];
+[WAEventJoinAttempt joinFailureAsString:];
```

## Instance methods

```
-[WAEventJoinAttempt processEventOnPersistentContainer:andRunPostprocessing:withError:];
-[WAEventJoinAttempt dictionaryForCA];
-[WAEventJoinAttempt eventNameForCA];
-[WAEventJoinAttempt ssid];
-[WAEventJoinAttempt setSsid:];
-[WAEventJoinAttempt updateRecord:];
-[WAEventJoinAttempt initWithBssid:ssid:apProfile:security:at:data:withLqmHistory:withError:];
-[WAEventJoinAttempt data];
-[WAEventJoinAttempt status];
-[WAEventJoinAttempt setApProfileID:];
-[WAEventJoinAttempt apProfileID];
-[WAEventJoinAttempt security];
-[WAEventJoinAttempt description];
-[WAEventJoinAttempt setSecurity:];
```
