# `TBCacheAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBAnalyticsEvent`
- 7 instance variables, 11 properties, 14 instance methods, 3 class methods

## Instance variables

```
Q _status;
@"NSNumber" _staleness;
@"NSNumber" _tileKey;
@"NSNumber" _type;
@"NSNumber" _errorCode;
@"NSString" _eventName;
@"NSDictionary" _eventDictionary;
```

## Properties

```
@property (TQ,N,V_status) status;
@property (T@"NSNumber",N,V_staleness) staleness;
@property (T@"NSNumber",N,V_tileKey) tileKey;
@property (T@"NSNumber",N,V_type) type;
@property (T@"NSNumber",N,V_errorCode) errorCode;
@property (T@"NSString",&,N,V_eventName) eventName;
@property (T@"NSDictionary",&,N,V_eventDictionary) eventDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBCacheAnalyticsEvent cacheAnalyticsEventWithStatus:staleness:tileKey:type:error:];
+[TBCacheAnalyticsEvent cacheAvailabilityEventWithStatus:];
+[TBCacheAnalyticsEvent cacheEventWithTotalCount:last24HoursCount:];
```

## Instance methods

```
-[TBCacheAnalyticsEvent setErrorCode:];
-[TBCacheAnalyticsEvent errorCode];
-[TBCacheAnalyticsEvent eventDictionary];
-[TBCacheAnalyticsEvent status];
-[TBCacheAnalyticsEvent setTileKey:];
-[TBCacheAnalyticsEvent eventName];
-[TBCacheAnalyticsEvent tileKey];
-[TBCacheAnalyticsEvent setType:];
-[TBCacheAnalyticsEvent type];
-[TBCacheAnalyticsEvent setStatus:];
-[TBCacheAnalyticsEvent setEventName:];
-[TBCacheAnalyticsEvent setEventDictionary:];
-[TBCacheAnalyticsEvent setStaleness:];
-[TBCacheAnalyticsEvent staleness];
```
