# `WFHealthManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 12 properties, 32 instance methods, 0 class methods

## Instance variables

```
B _isChinaDevice;
B _failNoInternetDiagnosticsTests;
B _shouldFileNewMetrics;
@"NSSet" _currentNetworkIssues;
@"WFInterface" _interface;
@"NWPathEvaluator" _evaluator;
@"CWFScanResult" _network;
@"NSOperationQueue" _noInternetTestQueue;
@"WFDiagnosticsManager" _diagnosticsManager;
q _completedVelocityTestTimes;
@"NSArray" _failedTestsIDs;
```

## Properties

```
@property (T@"WFInterface",&,N,V_interface) interface;
@property (T@"NSSet",&,N,V_currentNetworkIssues) currentNetworkIssues;
@property (T@"NWPathEvaluator",&,N,V_evaluator) evaluator;
@property (T@"CWFScanResult",&,N,V_network) network;
@property (T@"NSOperationQueue",&,N,V_noInternetTestQueue) noInternetTestQueue;
@property (T@"WFDiagnosticsManager",&,N,V_diagnosticsManager) diagnosticsManager;
@property (TB,N,V_failNoInternetDiagnosticsTests) failNoInternetDiagnosticsTests;
@property (Tq,N,V_completedVelocityTestTimes) completedVelocityTestTimes;
@property (TB,N,V_shouldFileNewMetrics) shouldFileNewMetrics;
@property (T@"NSArray",&,N,V_failedTestsIDs) failedTestsIDs;
@property (TB,R,N) currentNetworkHasNoInternetConnection;
@property (TB,N,V_isChinaDevice) isChinaDevice;
```

## Instance methods

```
-[WFHealthManager observeValueForKeyPath:ofObject:change:context:];
-[WFHealthManager network];
-[WFHealthManager linkQualityDidChange:];
-[WFHealthManager initWithInterface:];
-[WFHealthManager dealloc];
-[WFHealthManager currentNetworkIssues];
-[WFHealthManager setInterface:];
-[WFHealthManager interface];
-[WFHealthManager isChinaDevice];
-[WFHealthManager setCurrentNetworkIssues:];
-[WFHealthManager evaluator];
-[WFHealthManager setEvaluator:];
-[WFHealthManager setNetwork:];
-[WFHealthManager diagnosticsManager];
-[WFHealthManager setDiagnosticsManager:];
-[WFHealthManager _updateCurrentNetworkIssues];
-[WFHealthManager completedVelocityTestTimes];
-[WFHealthManager currentNetworkDidChange:];
-[WFHealthManager currentNetworkHasNoInternetConnection];
-[WFHealthManager failNoInternetDiagnosticsTests];
-[WFHealthManager failedTestsIDs];
-[WFHealthManager forceUpdateNetworkIssues];
-[WFHealthManager noInternetTestQueue];
-[WFHealthManager runNoInternetDiagnostics];
-[WFHealthManager runNoInternetDiagnosticsAfter:];
-[WFHealthManager setCompletedVelocityTestTimes:];
-[WFHealthManager setFailNoInternetDiagnosticsTests:];
-[WFHealthManager setFailedTestsIDs:];
-[WFHealthManager setIsChinaDevice:];
-[WFHealthManager setNoInternetTestQueue:];
-[WFHealthManager setShouldFileNewMetrics:];
-[WFHealthManager shouldFileNewMetrics];
```
