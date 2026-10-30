# `CWFAssetSetManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFAssetMgmtProtocol`, `CWFAssetRootMonitorDelegate`
- 25 instance variables, 29 properties, 74 instance methods, 1 class methods

## Instance variables

```
B _interestExpressed;
B _forTestingPeriodicCheckEnabled;
B _forTestingPeriodicCheckForDownloadEnabled;
B _periodicCheckForDownloadEnabled;
B _assetRootToProcess;
i _notifyTokenVersionDownloaded;
i _notifyTokenVersionDiscovered;
@? eventHandler;
@"CWFAssetRootMonitor" _assetRootMonitor;
@"NSObject<OS_dispatch_queue>" _eventQueue;
@? _assetDownloadedHandler;
@? _assetDiscoveredHandler;
@"MAAutoAssetSelector" _currentLockedAutoAssetSelector;
@"MAAutoAsset" _currentLockedAutoAsset;
@"NSString" _assetSpecifier;
@"NSObject<OS_dispatch_source>" _periodicCheckA11Timer;
@"NSString" _apiMajorVersion;
@"NSObject<OS_dispatch_source>" _forTestingPeriodicCheckTimer;
q _forTestingPeriodicityInSecs;
q _forTestingPeriodicityForDownloadInSecs;
Q _periodicCheckForDownloadCounts;
@"NSString" _atomicInstanceTrackedForDownloaded;
@"CWFAssetPowerTable" _assetPowerTable;
@"CWFAssetCreatorFromRoot" _assetFromRoot;
Q _readinessRetryCount;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_eventQueue) eventQueue;
@property (T@?,C,N,V_assetDownloadedHandler) assetDownloadedHandler;
@property (T@?,C,N,V_assetDiscoveredHandler) assetDiscoveredHandler;
@property (T@"MAAutoAssetSelector",&,N,V_currentLockedAutoAssetSelector) currentLockedAutoAssetSelector;
@property (T@"MAAutoAsset",&,N,V_currentLockedAutoAsset) currentLockedAutoAsset;
@property (TB,N,V_interestExpressed) interestExpressed;
@property (Ti,N,V_notifyTokenVersionDownloaded) notifyTokenVersionDownloaded;
@property (Ti,N,V_notifyTokenVersionDiscovered) notifyTokenVersionDiscovered;
@property (T@"NSString",&,N,V_assetSpecifier) assetSpecifier;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_periodicCheckA11Timer) periodicCheckA11Timer;
@property (T@"NSString",&,N,V_apiMajorVersion) apiMajorVersion;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_forTestingPeriodicCheckTimer) forTestingPeriodicCheckTimer;
@property (TB,N,V_forTestingPeriodicCheckEnabled) forTestingPeriodicCheckEnabled;
@property (Tq,N,V_forTestingPeriodicityInSecs) forTestingPeriodicityInSecs;
@property (TB,N,V_forTestingPeriodicCheckForDownloadEnabled) forTestingPeriodicCheckForDownloadEnabled;
@property (Tq,N,V_forTestingPeriodicityForDownloadInSecs) forTestingPeriodicityForDownloadInSecs;
@property (TB,N,V_periodicCheckForDownloadEnabled) periodicCheckForDownloadEnabled;
@property (TQ,N,V_periodicCheckForDownloadCounts) periodicCheckForDownloadCounts;
@property (T@"NSString",&,N,V_atomicInstanceTrackedForDownloaded) atomicInstanceTrackedForDownloaded;
@property (TB,N,V_assetRootToProcess) assetRootToProcess;
@property (T@"CWFAssetPowerTable",&,N,V_assetPowerTable) assetPowerTable;
@property (T@"CWFAssetCreatorFromRoot",&,N,V_assetFromRoot) assetFromRoot;
@property (TQ,N,V_readinessRetryCount) readinessRetryCount;
@property (T@"CWFAssetRootMonitor",&,N,V_assetRootMonitor) assetRootMonitor;
@property (T@?,C,VeventHandler) eventHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CWFAssetSetManager endAllPreviousLocks];
```

## Instance methods

```
-[CWFAssetSetManager assetSpecifier];
-[CWFAssetSetManager forTestingPeriodicityForDownloadInSecs];
-[CWFAssetSetManager periodicCheckForDownloadCounts];
-[CWFAssetSetManager eventQueue];
-[CWFAssetSetManager setEventQueue:];
-[CWFAssetSetManager _handleAssetDownloadedNotification];
-[CWFAssetSetManager scheduleReadinessRetry];
-[CWFAssetSetManager setAssetPowerTable:];
-[CWFAssetSetManager eventHandler];
-[CWFAssetSetManager setAssetFromRoot:];
-[CWFAssetSetManager setAssetSpecifier:];
-[CWFAssetSetManager setEventHandler:];
-[CWFAssetSetManager setCurrentLockedAutoAsset:];
-[CWFAssetSetManager setAssetDiscoveredHandler:];
-[CWFAssetSetManager makeAutoAssetSetWithEntry:];
-[CWFAssetSetManager setForTestingPeriodicCheckTimer:];
-[CWFAssetSetManager unlockAssetWithReason:];
-[CWFAssetSetManager init];
-[CWFAssetSetManager atomicInstanceTrackedForDownloaded];
-[CWFAssetSetManager _registerForAssetDiscoveredNotification:];
-[CWFAssetSetManager __startAssetTracking];
-[CWFAssetSetManager _forTestingPeriodicCheck];
-[CWFAssetSetManager interestExpressed];
-[CWFAssetSetManager setAssetRootToProcess:];
-[CWFAssetSetManager setApiMajorVersion:];
-[CWFAssetSetManager currentLockedAutoAssetSelector];
-[CWFAssetSetManager notifyTokenVersionDownloaded];
-[CWFAssetSetManager assetPowerTable];
-[CWFAssetSetManager forTestingPeriodicCheckEnabled];
-[CWFAssetSetManager forTestingPeriodicCheckTimer];
-[CWFAssetSetManager lockAutoAssetWithReason:isBlocking:forcedFetch:];
-[CWFAssetSetManager readinessRetryCount];
-[CWFAssetSetManager invalidate];
-[CWFAssetSetManager apiMajorVersion];
-[CWFAssetSetManager setNotifyTokenVersionDiscovered:];
-[CWFAssetSetManager notifyTokenVersionDiscovered];
-[CWFAssetSetManager forTestingPeriodicCheckForDownloadEnabled];
-[CWFAssetSetManager setForTestingPeriodicityInSecs:];
-[CWFAssetSetManager assetDiscoveredHandler];
-[CWFAssetSetManager assetDownloadedHandler];
-[CWFAssetSetManager __periodicCheckA11];
-[CWFAssetSetManager isMobileAssetDaemonReady];
-[CWFAssetSetManager setCurrentLockedAutoAssetSelector:];
-[CWFAssetSetManager lockAndHandOffCanBlock:forcedFetch:];
-[CWFAssetSetManager _handleAssetDiscoveredNotification];
-[CWFAssetSetManager activate];
-[CWFAssetSetManager setForTestingPeriodicCheckEnabled:];
-[CWFAssetSetManager checkAssetsWithReason:CanBlock:forAtomicInstance:];
-[CWFAssetSetManager _configureIntervalForTestingForPeriodicCheckForDownload];
-[CWFAssetSetManager setPeriodicCheckForDownloadCounts:];
-[CWFAssetSetManager forTestingEnablePeriodicCheck];
-[CWFAssetSetManager setForTestingPeriodicityForDownloadInSecs:];
-[CWFAssetSetManager assetFromRoot];
-[CWFAssetSetManager _periodicCheckForDownloaded];
-[CWFAssetSetManager _registerForAssetDownloadedNotification:];
-[CWFAssetSetManager setReadinessRetryCount:];
-[CWFAssetSetManager setAtomicInstanceTrackedForDownloaded:];
-[CWFAssetSetManager periodicCheckForDownloadEnabled];
-[CWFAssetSetManager rootMonitorDetectedAdd:deleted:updated:];
-[CWFAssetSetManager forTestingPeriodicityInSecs];
-[CWFAssetSetManager periodicCheckA11Timer];
-[CWFAssetSetManager assetRootMonitor];
-[CWFAssetSetManager processQueryResults:withError:];
-[CWFAssetSetManager setPeriodicCheckA11Timer:];
-[CWFAssetSetManager setInterestExpressed:];
-[CWFAssetSetManager setAssetRootMonitor:];
-[CWFAssetSetManager assetRootToProcess];
-[CWFAssetSetManager setForTestingPeriodicCheckForDownloadEnabled:];
-[CWFAssetSetManager setAssetDownloadedHandler:];
-[CWFAssetSetManager setNotifyTokenVersionDownloaded:];
-[CWFAssetSetManager setPeriodicCheckForDownloadEnabled:];
-[CWFAssetSetManager makeAutoAssetWithSelector:];
-[CWFAssetSetManager currentLockedAutoAsset];
-[CWFAssetSetManager __stopPeriodicCheckA11];
```
