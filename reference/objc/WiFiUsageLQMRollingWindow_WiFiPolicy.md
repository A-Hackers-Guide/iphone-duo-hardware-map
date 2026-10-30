# `WiFiUsageLQMRollingWindow`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 36 instance methods, 10 class methods

## Instance variables

```
@"NSString" _interfaceName;
@"NSString" _label;
@"NSDate" _createdTimestamp;
d _duration;
@"NSMutableArray" _samples;
@"WiFiUsageInterfaceCapabilities" _capabilities;
@"NSMutableArray" _triggerCriteriaFilterList;
@"NSMutableSet" _features;
@"NSMutableArray" _preceedingTriggers;
@"NSString" _fgApp;
@"NSString" _lastSampleBssid;
```

## Properties

```
@property (T@"NSDate",C,N,V_createdTimestamp) createdTimestamp;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (Td,N,V_duration) duration;
@property (T@"NSMutableArray",&,N,V_samples) samples;
@property (T@"NSMutableArray",&,N,V_triggerCriteriaFilterList) triggerCriteriaFilterList;
@property (T@"NSMutableSet",&,N,V_features) features;
@property (T@"NSString",&,N,V_lastSampleBssid) lastSampleBssid;
@property (T@"NSString",&,N,V_fgApp) fgApp;
@property (T@"NSString",C,N,V_label) label;
@property (T@"WiFiUsageInterfaceCapabilities",&,N,V_capabilities) capabilities;
@property (T@"NSMutableArray",R,N,V_preceedingTriggers) preceedingTriggers;
```

## Class methods

```
+[WiFiUsageLQMRollingWindow initialize];
+[WiFiUsageLQMRollingWindow updateConfig];
+[WiFiUsageLQMRollingWindow averageIntegerValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow getValue:ForField:ScaledByDuration:];
+[WiFiUsageLQMRollingWindow maximumIntegerValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow medianIntegerValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow minimumIntegerValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow modeValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow modesValueForField:ScaledByDuration:OnSamples:];
+[WiFiUsageLQMRollingWindow sumIntegerValueForField:ScaledByDuration:OnSamples:];
```

## Instance methods

```
-[WiFiUsageLQMRollingWindow samples];
-[WiFiUsageLQMRollingWindow features];
-[WiFiUsageLQMRollingWindow fgApp];
-[WiFiUsageLQMRollingWindow setCurrentApplicationName:withAttributes:];
-[WiFiUsageLQMRollingWindow setFeatures:];
-[WiFiUsageLQMRollingWindow addSample:];
-[WiFiUsageLQMRollingWindow setFgApp:];
-[WiFiUsageLQMRollingWindow setTriggerCriteriaFilterList:];
-[WiFiUsageLQMRollingWindow clearOngoingCriteriaDates];
-[WiFiUsageLQMRollingWindow triggerCriteriaFilterList];
-[WiFiUsageLQMRollingWindow addSamples:];
-[WiFiUsageLQMRollingWindow label];
-[WiFiUsageLQMRollingWindow setLabel:];
-[WiFiUsageLQMRollingWindow evaluateCriteriaWithStopUponFirstMatch:];
-[WiFiUsageLQMRollingWindow hasChanged:];
-[WiFiUsageLQMRollingWindow initWithInterfaceName:andInterfaceCapabilities:];
-[WiFiUsageLQMRollingWindow setInterfaceName:];
-[WiFiUsageLQMRollingWindow configureDataTriggeredCriteria];
-[WiFiUsageLQMRollingWindow interfaceName];
-[WiFiUsageLQMRollingWindow createdTimestamp];
-[WiFiUsageLQMRollingWindow duration];
-[WiFiUsageLQMRollingWindow lastSampleBssid];
-[WiFiUsageLQMRollingWindow checkCriteriaBSSIDWithSample:];
-[WiFiUsageLQMRollingWindow cleanUpStashedMedians];
-[WiFiUsageLQMRollingWindow endOngoingCriteria];
-[WiFiUsageLQMRollingWindow setCreatedTimestamp:];
-[WiFiUsageLQMRollingWindow addTrigger:];
-[WiFiUsageLQMRollingWindow updateWindow];
-[WiFiUsageLQMRollingWindow capabilities];
-[WiFiUsageLQMRollingWindow initWithInterfaceName:andDuration:andInterfaceCapabilities:];
-[WiFiUsageLQMRollingWindow setSamples:];
-[WiFiUsageLQMRollingWindow setDuration:];
-[WiFiUsageLQMRollingWindow preceedingTriggers];
-[WiFiUsageLQMRollingWindow setCapabilities:];
-[WiFiUsageLQMRollingWindow getTriggerCriteriaList];
-[WiFiUsageLQMRollingWindow setLastSampleBssid:];
```
