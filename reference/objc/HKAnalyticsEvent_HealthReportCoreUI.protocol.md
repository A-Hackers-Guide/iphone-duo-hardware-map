# `HKAnalyticsEvent` (protocol)

- Image: [`/System/Library/PrivateFrameworks/HealthReportCoreUI.framework/HealthReportCoreUI`](../userland/System__Library__PrivateFrameworks__HealthReportCoreUI.framework__HealthReportCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 2 properties, 4 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) isEventSubmissionIHAGated;
@property (T@"NSString",R,N) eventName;
```

## Instance methods

```
-[HKAnalyticsEvent eventName];
-[HKAnalyticsEvent isEventSubmissionIHAGated];
-[HKAnalyticsEvent makeIHAGatedEventPayloadWithDataSource:error:];
-[HKAnalyticsEvent makeUnrestrictedEventPayloadWithDataSource:error:];
```
