# `DeploymentMetricHandler`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _isInternalInstall;
@"AnalyticsStoreMOHandler" _storeMOHandler;
```

## Properties

```
@property (T@"AnalyticsStoreMOHandler",&,N,V_storeMOHandler) storeMOHandler;
@property (TB,N,V_isInternalInstall) isInternalInstall;
```

## Instance methods

```
-[DeploymentMetricHandler isInternalInstall];
-[DeploymentMetricHandler setIsInternalInstall:];
-[DeploymentMetricHandler appendBssAnalyticsToMetric:bssMo:maxAgeInDays:];
-[DeploymentMetricHandler appendJoinsSummaryToMetric:ssid:maxAgeInDays:];
-[DeploymentMetricHandler appendNetworkAnalyticsToMetric:ssid:deploymentUuid:maxAgeInDays:];
-[DeploymentMetricHandler initWithAnalyticsStore:];
-[DeploymentMetricHandler leavesSummary:bssid:maxAgeInDays:];
-[DeploymentMetricHandler metricNeedsSubmission:deploymentUuid:interval:];
-[DeploymentMetricHandler networkDeploymentMetricCheckAndSubmit:interval:];
-[DeploymentMetricHandler roamsSummary:bssid:maxAgeInDays:];
-[DeploymentMetricHandler setStoreMOHandler:];
-[DeploymentMetricHandler storeMOHandler];
-[DeploymentMetricHandler submitBssAnalyticsMetrics:deploymentUuid:stitchIndex:];
```
