# `SBDoNotDisturbMetric`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DNDStateUpdateListener`, `SBFAnalyticsBackendEventHandling`
- 7 instance variables, 11 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _doNotDisturbActive;
@"DNDStateService" _dndStateService;
@"SBFAnalyticsClient" _analyticsClient;
Q _location;
@"NSString" _primaryBundleIdentifier;
@"NSString" _sideBundleIdentifier;
@"NSString" _floatingBundleIdentifier;
```

## Properties

```
@property (T@"DNDStateService",R,N,V_dndStateService) dndStateService;
@property (T@"SBFAnalyticsClient",R,N,V_analyticsClient) analyticsClient;
@property (TQ,N,V_location) location;
@property (T@"NSString",C,N,V_primaryBundleIdentifier) primaryBundleIdentifier;
@property (T@"NSString",C,N,V_sideBundleIdentifier) sideBundleIdentifier;
@property (T@"NSString",C,N,V_floatingBundleIdentifier) floatingBundleIdentifier;
@property (TB,R,N,GisDoNotDisturbActive,V_doNotDisturbActive) doNotDisturbActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDoNotDisturbMetric stateService:didReceiveDoNotDisturbStateUpdate:];
-[SBDoNotDisturbMetric init];
-[SBDoNotDisturbMetric location];
-[SBDoNotDisturbMetric dndStateService];
-[SBDoNotDisturbMetric dealloc];
-[SBDoNotDisturbMetric setLocation:];
-[SBDoNotDisturbMetric analyticsClient];
-[SBDoNotDisturbMetric handleEvent:withContext:];
-[SBDoNotDisturbMetric _bundleIdentifierForElementWithLayoutRole:fromContext:];
-[SBDoNotDisturbMetric floatingBundleIdentifier];
-[SBDoNotDisturbMetric initWithAnalyticsClient:];
-[SBDoNotDisturbMetric initWithAnalyticsClient:dndStateService:];
-[SBDoNotDisturbMetric isDoNotDisturbActive];
-[SBDoNotDisturbMetric primaryBundleIdentifier];
-[SBDoNotDisturbMetric sendCoreAnalyticsEventWithName:payload:];
-[SBDoNotDisturbMetric setFloatingBundleIdentifier:];
-[SBDoNotDisturbMetric setPrimaryBundleIdentifier:];
-[SBDoNotDisturbMetric setSideBundleIdentifier:];
-[SBDoNotDisturbMetric sideBundleIdentifier];
```
