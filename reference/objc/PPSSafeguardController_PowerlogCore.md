# `PPSSafeguardController`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 36 instance methods, 1 class methods

## Instance variables

```
@"DRConfigMonitor" _drConfigMonitor;
@"PLNSNotificationOperatorComposition" _dayChangedNotification;
```

## Properties

```
@property (T@"DRConfigMonitor",&,V_drConfigMonitor) drConfigMonitor;
@property (T@"PLNSNotificationOperatorComposition",&,V_dayChangedNotification) dayChangedNotification;
```

## Class methods

```
+[PPSSafeguardController sharedInstance];
```

## Instance methods

```
-[PPSSafeguardController startDate];
-[PPSSafeguardController currentDate];
-[PPSSafeguardController init];
-[PPSSafeguardController installDate];
-[PPSSafeguardController workQueue];
-[PPSSafeguardController isEnabled];
-[PPSSafeguardController isEligible];
-[PPSSafeguardController stopDate];
-[PPSSafeguardController drConfigMonitor];
-[PPSSafeguardController upload:];
-[PPSSafeguardController configureWithDefaultValues];
-[PPSSafeguardController configureWithDictionary:];
-[PPSSafeguardController dataDuration];
-[PPSSafeguardController dayChangedNotification];
-[PPSSafeguardController debug_forceEligibility];
-[PPSSafeguardController debug_installDate];
-[PPSSafeguardController debug_treatAsTestDevice];
-[PPSSafeguardController eligibilityDuration];
-[PPSSafeguardController eligibilityRange];
-[PPSSafeguardController excludeTestDevices];
-[PPSSafeguardController handleTask:];
-[PPSSafeguardController isTestDeviceForSafeguard];
-[PPSSafeguardController lastSubmissionDate];
-[PPSSafeguardController minimumLiveOnTime];
-[PPSSafeguardController performSubmission];
-[PPSSafeguardController registerDataCollectionActivity];
-[PPSSafeguardController reportEventToCA:didUpload:];
-[PPSSafeguardController scheduleSubmission];
-[PPSSafeguardController setDayChangedNotification:];
-[PPSSafeguardController setDrConfigMonitor:];
-[PPSSafeguardController setupDRTasking];
-[PPSSafeguardController startHour];
-[PPSSafeguardController stopHour];
-[PPSSafeguardController todayRange];
-[PPSSafeguardController unregisterDataCollectionActivity];
-[PPSSafeguardController uploadRange];
```
