# `WADeploymentAnalyzer`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"WADeploymentAnalyzerDefaults" _defaults;
@"WAPersistentContainer" _persistentContainer;
```

## Properties

```
@property (T@"WADeploymentAnalyzerDefaults",&,N,V_defaults) defaults;
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
```

## Instance methods

```
-[WADeploymentAnalyzer setDefaults:];
-[WADeploymentAnalyzer defaults];
-[WADeploymentAnalyzer init];
-[WADeploymentAnalyzer setPersistentContainer:];
-[WADeploymentAnalyzer persistentContainer];
-[WADeploymentAnalyzer initWithDefaults:];
-[WADeploymentAnalyzer initWithPersistentContainer:];
-[WADeploymentAnalyzer _analyzeResultsForCongestion:withMetric:];
-[WADeploymentAnalyzer _analyzeResultsForCoverage:withMetric:];
-[WADeploymentAnalyzer _fetchIneligibleNetworkCount];
-[WADeploymentAnalyzer _fetchUsageForNetworks:timeSpan:withError:];
-[WADeploymentAnalyzer _updateCongestionIfNeededForNetwork:newCongestion:pastWeekUsage:];
-[WADeploymentAnalyzer _updateCoverageIfNeededForNetwork:newCoverage:pastWeekUsage:];
-[WADeploymentAnalyzer _verifyMinStayAtGoodCoverageForSSID:pastWeekUsage:];
-[WADeploymentAnalyzer _verifyMinStayAtLowCongestionForSSID:pastWeekUsage:];
-[WADeploymentAnalyzer updateHomeNetworksForDeploymentIssuesWithReason:withError:];
-[WADeploymentAnalyzer updateNetworksForCoverageIssues:withReason:withError:];
```
