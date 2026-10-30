# `UsageWeeklyMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UsageMO`
- Protocols: `UsageMOProtocol`
- 0 instance variables, 23 properties, 0 instance methods, 3 class methods

## Properties

```
@property (Ts,D,N) band;
@property (T@"NSString",C,D,N) bssid;
@property (Ts,D,N) ccaTotal_gt;
@property (Ts,D,N) ccaTotal_le;
@property (T@"NSDate",C,D,N) date_ge;
@property (T@"NSDate",C,D,N) date_lt;
@property (T@"NSString",C,D,N) ipv4NetworkSignature;
@property (T@"NSString",C,D,N) ipv6NetworkSignature;
@property (TB,D,N) isAnyAppInFG;
@property (TB,D,N) isFTactive;
@property (TB,D,N) isTimeSensitiveAppRunning;
@property (Ts,D,N) rssi_ge;
@property (Ts,D,N) rssi_lt;
@property (Tq,D,N) rxtxFrames_gt;
@property (Tq,D,N) rxtxFrames_le;
@property (Tq,D,N) seconds;
@property (T@"NSString",C,D,N) ssid;
@property (Ts,D,N) subband;
@property (T@"BSSMO",&,D,N) bss;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UsageWeeklyMO fetchRequest];
+[UsageWeeklyMO timeSpan];
+[UsageWeeklyMO jumpBackOneSpan];
```
