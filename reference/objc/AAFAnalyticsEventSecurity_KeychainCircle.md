# `AAFAnalyticsEventSecurity`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 20 instance methods, 5 class methods

## Instance variables

```
B _canSendMetrics;
B _isAAAFoundationAvailable;
B _isAuthKitAvailable;
B _metricSent;
@"NSObject<OS_dispatch_queue>" _queue;
@"AAFAnalyticsEvent" _event;
```

## Properties

```
@property (T@"AAFAnalyticsEvent",&,V_event) event;
@property (TB,V_canSendMetrics) canSendMetrics;
@property (TB,V_isAAAFoundationAvailable) isAAAFoundationAvailable;
@property (TB,V_isAuthKitAvailable) isAuthKitAvailable;
@property (TB,V_metricSent) metricSent;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
```

## Class methods

```
+[AAFAnalyticsEventSecurity isAuthKitAvailable];
+[AAFAnalyticsEventSecurity isAAAFoundationAvailable];
+[AAFAnalyticsEventSecurity fetchDeviceSessionIDFromAuthKit:];
+[AAFAnalyticsEventSecurity reporterRTCAdapter];
+[AAFAnalyticsEventSecurity setReporterRTCAdapter:];
```

## Instance methods

```
-[AAFAnalyticsEventSecurity setEvent:];
-[AAFAnalyticsEventSecurity metricSent];
-[AAFAnalyticsEventSecurity permittedToSendMetrics];
-[AAFAnalyticsEventSecurity isAuthKitAvailable];
-[AAFAnalyticsEventSecurity dealloc];
-[AAFAnalyticsEventSecurity setIsAAAFoundationAvailable:];
-[AAFAnalyticsEventSecurity event];
-[AAFAnalyticsEventSecurity queue];
-[AAFAnalyticsEventSecurity setIsAuthKitAvailable:];
-[AAFAnalyticsEventSecurity canSendMetrics];
-[AAFAnalyticsEventSecurity setCanSendMetrics:];
-[AAFAnalyticsEventSecurity addMetrics:];
-[AAFAnalyticsEventSecurity initWithMetrics:session:eventName:canSendMetrics:];
-[AAFAnalyticsEventSecurity initWithMetrics:session:eventName:];
-[AAFAnalyticsEventSecurity sendMetricWithResult:error:];
-[AAFAnalyticsEventSecurity isAAAFoundationAvailable];
-[AAFAnalyticsEventSecurity setMetricSent:];
-[AAFAnalyticsEventSecurity initWithSession:eventName:];
-[AAFAnalyticsEventSecurity populateUnderlyingErrorsStartingWithRootError:];
-[AAFAnalyticsEventSecurity setQueue:];
```
