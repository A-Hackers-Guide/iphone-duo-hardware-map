# `WADeploymentAnalyzerDefaults`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
d _poorCoverageThreshold;
q _poorCoverageRSSI;
Q _poorCoverageMinimumStay;
q _highCongestionRSSIThreshold;
Q _highCongestionCCAThreshold;
d _highCongestionThreshold;
Q _highCongestionMinimumStay;
```

## Properties

```
@property (Td,N,V_poorCoverageThreshold) poorCoverageThreshold;
@property (Tq,N,V_poorCoverageRSSI) poorCoverageRSSI;
@property (TQ,N,V_poorCoverageMinimumStay) poorCoverageMinimumStay;
@property (Tq,N,V_highCongestionRSSIThreshold) highCongestionRSSIThreshold;
@property (TQ,N,V_highCongestionCCAThreshold) highCongestionCCAThreshold;
@property (Td,N,V_highCongestionThreshold) highCongestionThreshold;
@property (TQ,N,V_highCongestionMinimumStay) highCongestionMinimumStay;
```

## Class methods

```
+[WADeploymentAnalyzerDefaults _numberDefaultForKey:];
```

## Instance methods

```
-[WADeploymentAnalyzerDefaults init];
-[WADeploymentAnalyzerDefaults setHighCongestionRSSIThreshold:];
-[WADeploymentAnalyzerDefaults highCongestionCCAThreshold];
-[WADeploymentAnalyzerDefaults highCongestionMinimumStay];
-[WADeploymentAnalyzerDefaults highCongestionRSSIThreshold];
-[WADeploymentAnalyzerDefaults highCongestionThreshold];
-[WADeploymentAnalyzerDefaults poorCoverageMinimumStay];
-[WADeploymentAnalyzerDefaults poorCoverageRSSI];
-[WADeploymentAnalyzerDefaults poorCoverageThreshold];
-[WADeploymentAnalyzerDefaults setHighCongestionCCAThreshold:];
-[WADeploymentAnalyzerDefaults setHighCongestionMinimumStay:];
-[WADeploymentAnalyzerDefaults setHighCongestionThreshold:];
-[WADeploymentAnalyzerDefaults setPoorCoverageMinimumStay:];
-[WADeploymentAnalyzerDefaults setPoorCoverageRSSI:];
-[WADeploymentAnalyzerDefaults setPoorCoverageThreshold:];
```
