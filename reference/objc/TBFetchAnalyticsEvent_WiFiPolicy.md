# `TBFetchAnalyticsEvent`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TBAnalyticsEvent`
- 9 instance variables, 15 properties, 20 instance methods, 1 class methods

## Instance variables

```
Q _source;
Q _type;
Q _trigger;
@"NSNumber" _duration;
@"NSNumber" _requestCount;
@"NSNumber" _resultCount;
@"NSString" _tileKey;
@"NSError" _error;
@"NSDate" _date;
```

## Properties

```
@property (TQ,N,V_source) source;
@property (TQ,N,V_type) type;
@property (TQ,N,V_trigger) trigger;
@property (T@"NSNumber",&,N,V_duration) duration;
@property (T@"NSNumber",&,N,V_requestCount) requestCount;
@property (T@"NSNumber",&,N,V_resultCount) resultCount;
@property (T@"NSString",&,N,V_tileKey) tileKey;
@property (T@"NSError",&,N,V_error) error;
@property (T@"NSDate",&,N,V_date) date;
@property (T@"NSString",R,N) eventName;
@property (T@"NSDictionary",R,N) eventDictionary;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TBFetchAnalyticsEvent fetchEventWithSource:type:trigger:duration:requestCount:resultCount:error:tileKey:];
```

## Instance methods

```
-[TBFetchAnalyticsEvent requestCount];
-[TBFetchAnalyticsEvent trigger];
-[TBFetchAnalyticsEvent setError:];
-[TBFetchAnalyticsEvent eventDictionary];
-[TBFetchAnalyticsEvent setDate:];
-[TBFetchAnalyticsEvent setRequestCount:];
-[TBFetchAnalyticsEvent error];
-[TBFetchAnalyticsEvent date];
-[TBFetchAnalyticsEvent duration];
-[TBFetchAnalyticsEvent setTileKey:];
-[TBFetchAnalyticsEvent setSource:];
-[TBFetchAnalyticsEvent resultCount];
-[TBFetchAnalyticsEvent eventName];
-[TBFetchAnalyticsEvent tileKey];
-[TBFetchAnalyticsEvent setType:];
-[TBFetchAnalyticsEvent type];
-[TBFetchAnalyticsEvent setResultCount:];
-[TBFetchAnalyticsEvent setDuration:];
-[TBFetchAnalyticsEvent setTrigger:];
-[TBFetchAnalyticsEvent source];
```
