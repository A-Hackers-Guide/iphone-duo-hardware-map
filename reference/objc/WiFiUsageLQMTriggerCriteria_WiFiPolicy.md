# `WiFiUsageLQMTriggerCriteria`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 27 instance methods, 4 class methods

## Instance variables

```
B _valid;
B _matched;
Q _type;
@"NSPredicate" _predicate;
@"NSPredicate" _requiredFieldsValid;
@"NSDate" _firstTriggered;
@"NSDate" _lastTriggered;
@"NSDate" _currentSample;
@"NSString" _bssid;
@"NSString" _filterCriteria;
```

## Properties

```
@property (TQ,N,V_type) type;
@property (T@"NSPredicate",&,N,V_predicate) predicate;
@property (T@"NSPredicate",&,N,V_requiredFieldsValid) requiredFieldsValid;
@property (T@"NSString",&,N,V_filterCriteria) filterCriteria;
@property (TB,N,V_valid) valid;
@property (TB,N,V_matched) matched;
@property (T@"NSDate",&,N,V_firstTriggered) firstTriggered;
@property (T@"NSDate",&,N,V_lastTriggered) lastTriggered;
@property (T@"NSDate",&,N,V_currentSample) currentSample;
@property (T@"NSString",&,N,V_bssid) bssid;
```

## Class methods

```
+[WiFiUsageLQMTriggerCriteria initialize];
+[WiFiUsageLQMTriggerCriteria dataTriggeredTypes];
+[WiFiUsageLQMTriggerCriteria parseCriteria:intoRequiredFields:andFeatures:forFields:withType:isFilter:];
+[WiFiUsageLQMTriggerCriteria predicateNoQuotes:];
```

## Instance methods

```
-[WiFiUsageLQMTriggerCriteria valid];
-[WiFiUsageLQMTriggerCriteria setFilterCriteria:];
-[WiFiUsageLQMTriggerCriteria setValid:];
-[WiFiUsageLQMTriggerCriteria setBssid:];
-[WiFiUsageLQMTriggerCriteria setMatched:];
-[WiFiUsageLQMTriggerCriteria typeAsString];
-[WiFiUsageLQMTriggerCriteria redactedDescription];
-[WiFiUsageLQMTriggerCriteria setPredicate:];
-[WiFiUsageLQMTriggerCriteria setType:];
-[WiFiUsageLQMTriggerCriteria type];
-[WiFiUsageLQMTriggerCriteria description];
-[WiFiUsageLQMTriggerCriteria bssid];
-[WiFiUsageLQMTriggerCriteria predicate];
-[WiFiUsageLQMTriggerCriteria copyWithZone:];
-[WiFiUsageLQMTriggerCriteria filterCriteria];
-[WiFiUsageLQMTriggerCriteria matched];
-[WiFiUsageLQMTriggerCriteria initWith:forFields:andFeatures:];
-[WiFiUsageLQMTriggerCriteria currentSample];
-[WiFiUsageLQMTriggerCriteria firstTriggered];
-[WiFiUsageLQMTriggerCriteria lastTriggered];
-[WiFiUsageLQMTriggerCriteria requiredFieldsValid];
-[WiFiUsageLQMTriggerCriteria setCurrentSample:];
-[WiFiUsageLQMTriggerCriteria setFirstTriggered:];
-[WiFiUsageLQMTriggerCriteria setLastTriggered:];
-[WiFiUsageLQMTriggerCriteria setRequiredFieldsValid:];
-[WiFiUsageLQMTriggerCriteria shortPredicate];
-[WiFiUsageLQMTriggerCriteria shortPredicateNoSpaces];
```
