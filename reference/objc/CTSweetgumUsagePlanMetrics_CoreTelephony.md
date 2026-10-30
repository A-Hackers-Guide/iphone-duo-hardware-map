# `CTSweetgumUsagePlanMetrics`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 9 instance variables, 9 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _currentUsedPlan;
B _throttled;
@"NSString" _planLabel;
q _planCategory;
@"CTSweetgumUsagePlanItemData" _dataUsage;
@"CTSweetgumUsagePlanItemMessages" _messages;
@"CTSweetgumUsagePlanItemVoice" _voice;
@"NSString" _remainingBalance;
@"NSDate" _lastUpdatedAt;
```

## Properties

```
@property (T@"NSString",&,N,V_planLabel) planLabel;
@property (Tq,N,V_planCategory) planCategory;
@property (TB,N,V_currentUsedPlan) currentUsedPlan;
@property (T@"CTSweetgumUsagePlanItemData",&,N,V_dataUsage) dataUsage;
@property (T@"CTSweetgumUsagePlanItemMessages",&,N,V_messages) messages;
@property (T@"CTSweetgumUsagePlanItemVoice",&,N,V_voice) voice;
@property (T@"NSString",&,N,V_remainingBalance) remainingBalance;
@property (TB,N,V_throttled) throttled;
@property (T@"NSDate",&,N,V_lastUpdatedAt) lastUpdatedAt;
```

## Class methods

```
+[CTSweetgumUsagePlanMetrics supportsSecureCoding];
```

## Instance methods

```
-[CTSweetgumUsagePlanMetrics setMessages:];
-[CTSweetgumUsagePlanMetrics setThrottled:];
-[CTSweetgumUsagePlanMetrics messages];
-[CTSweetgumUsagePlanMetrics voice];
-[CTSweetgumUsagePlanMetrics init];
-[CTSweetgumUsagePlanMetrics throttled];
-[CTSweetgumUsagePlanMetrics dataUsage];
-[CTSweetgumUsagePlanMetrics encodeWithCoder:];
-[CTSweetgumUsagePlanMetrics setVoice:];
-[CTSweetgumUsagePlanMetrics description];
-[CTSweetgumUsagePlanMetrics initWithCoder:];
-[CTSweetgumUsagePlanMetrics isEqual:];
-[CTSweetgumUsagePlanMetrics lastUpdatedAt];
-[CTSweetgumUsagePlanMetrics setLastUpdatedAt:];
-[CTSweetgumUsagePlanMetrics currentUsedPlan];
-[CTSweetgumUsagePlanMetrics planCategory];
-[CTSweetgumUsagePlanMetrics planLabel];
-[CTSweetgumUsagePlanMetrics remainingBalance];
-[CTSweetgumUsagePlanMetrics setCurrentUsedPlan:];
-[CTSweetgumUsagePlanMetrics setDataUsage:];
-[CTSweetgumUsagePlanMetrics setPlanCategory:];
-[CTSweetgumUsagePlanMetrics setPlanLabel:];
-[CTSweetgumUsagePlanMetrics setRemainingBalance:];
```
