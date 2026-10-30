# `LANMO`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UniqueMO`
- Protocols: `UniqueMoProtocol`, `DeploymentProtocol`
- 0 instance variables, 17 properties, 2 instance methods, 5 class methods

## Properties

```
@property (Ti,R,D,N) bssCount;
@property (TB,D,N) has2GHz;
@property (TB,D,N) has5GHz;
@property (TB,D,N) has6GHz;
@property (T@"NSString",C,D,N) ipv4NetworkSignature;
@property (T@"NSString",C,D,N) ipv6NetworkSignature;
@property (Ts,D,N) latestCompleteWeekUsageCumulativePercentage;
@property (Tq,D,N) latestCompleteWeekUsageCumulativeSeconds;
@property (Ts,D,N) latestCompleteWeekUsagePercentage;
@property (Tq,D,N) latestCompleteWeekUsageSeconds;
@property (Ti,D,N) t_networksCount;
@property (T@"NSSet",&,D,N) bsses;
@property (T@"NSSet",&,D,N) events;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LANMO fetchRequest];
+[LANMO predicateForLANsInNetwork:withError:];
+[LANMO constraintsWithDhcpServerInfo:];
+[LANMO predicateForLanContainingBSS:withError:];
+[LANMO verifyConstraints:withError:];
```

## Instance methods

```
-[LANMO isPublic];
-[LANMO isEnterprise];
```
