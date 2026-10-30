# `TBJoinAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBAnalyticsEvent`
- 8 instance variables, 14 properties, 18 instance methods, 2 class methods

## Instance variables

```
Q _type;
Q _source;
Q _action;
@"NSString" _bssid;
@"NSNumber" _latitude;
@"NSNumber" _longitude;
@"NSNumber" _score;
@"NSNumber" _visibleDuration;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (TQ,N,V_source) source;
@property (TQ,N,V_action) action;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (T@"NSNumber",&,N,V_latitude) latitude;
@property (T@"NSNumber",&,N,V_longitude) longitude;
@property (T@"NSNumber",&,N,V_score) score;
@property (T@"NSNumber",N,V_visibleDuration) visibleDuration;
@property (T@"NSString",R,N) eventName;
@property (T@"NSDictionary",R,N) eventDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBJoinAnalyticsEvent joinAlertEventWithSource:action:visibleDuration:];
+[TBJoinAnalyticsEvent joinRecommendationEventWithSource:action:BSSID:latitude:longitude:score:visibleDuration:];
```

## Instance methods

```
-[TBJoinAnalyticsEvent eventDictionary];
-[TBJoinAnalyticsEvent setLatitude:];
-[TBJoinAnalyticsEvent latitude];
-[TBJoinAnalyticsEvent setScore:];
-[TBJoinAnalyticsEvent longitude];
-[TBJoinAnalyticsEvent setLongitude:];
-[TBJoinAnalyticsEvent setBssid:];
-[TBJoinAnalyticsEvent setAction:];
-[TBJoinAnalyticsEvent action];
-[TBJoinAnalyticsEvent score];
-[TBJoinAnalyticsEvent setSource:];
-[TBJoinAnalyticsEvent eventName];
-[TBJoinAnalyticsEvent setType:];
-[TBJoinAnalyticsEvent type];
-[TBJoinAnalyticsEvent bssid];
-[TBJoinAnalyticsEvent source];
-[TBJoinAnalyticsEvent visibleDuration];
-[TBJoinAnalyticsEvent setVisibleDuration:];
```
