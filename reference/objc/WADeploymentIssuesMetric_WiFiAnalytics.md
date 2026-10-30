# `WADeploymentIssuesMetric`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
Q _eligibleNetworkCount;
Q _ineligibleNetworkCount;
Q _secondsSinceLastRun;
@"NSCountedSet" _issues;
@"NSCountedSet" _networks;
```

## Properties

```
@property (T@"NSCountedSet",&,N,V_issues) issues;
@property (T@"NSCountedSet",&,N,V_networks) networks;
@property (TQ,N,V_eligibleNetworkCount) eligibleNetworkCount;
@property (TQ,N,V_ineligibleNetworkCount) ineligibleNetworkCount;
@property (TQ,N,V_secondsSinceLastRun) secondsSinceLastRun;
```

## Instance methods

```
-[WADeploymentIssuesMetric setNetworks:];
-[WADeploymentIssuesMetric init];
-[WADeploymentIssuesMetric networks];
-[WADeploymentIssuesMetric submit];
-[WADeploymentIssuesMetric addIssue:];
-[WADeploymentIssuesMetric issues];
-[WADeploymentIssuesMetric coreAnalyticsRepresentation];
-[WADeploymentIssuesMetric setIssues:];
-[WADeploymentIssuesMetric countForIssueType:];
-[WADeploymentIssuesMetric eligibleNetworkCount];
-[WADeploymentIssuesMetric highCongestionCount];
-[WADeploymentIssuesMetric ineligibleNetworkCount];
-[WADeploymentIssuesMetric percentageForIssueType:];
-[WADeploymentIssuesMetric poorCoverageCount];
-[WADeploymentIssuesMetric recommendationCount];
-[WADeploymentIssuesMetric recommendationPercentage];
-[WADeploymentIssuesMetric secondsSinceLastRun];
-[WADeploymentIssuesMetric setEligibleNetworkCount:];
-[WADeploymentIssuesMetric setIneligibleNetworkCount:];
-[WADeploymentIssuesMetric setSecondsSinceLastRun:];
```
