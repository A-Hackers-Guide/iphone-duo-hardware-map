# `WFScanManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 18 properties, 65 instance methods, 0 class methods

## Instance variables

```
B _doUnFilteredScanning;
B _supportsHotspotHelper;
B _supportsUnfilteredScanning;
B _hotspotHelperScanning;
B _useUIScanAPI;
q _state;
Q _consecutiveZeroFilteredScanResults;
Q _consecutiveZeroUnFilteredScanResults;
@"<WFScanManagerDelegate>" _delegate;
d _scanInterval;
@"<WFScanManagerScanProxy>" _scanProxy;
@"NSMutableSet" _networks;
@"NSMutableArray" _scanQueue;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSObject<OS_dispatch_queue>" _scanDispatchQueue;
@? _singleScanBlock;
@"NSMutableSet" _hotspotPluginNetworks;
q _numberOfScansPerformed;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (T@"<WFScanManagerDelegate>",W,N,V_delegate) delegate;
@property (Td,N,V_scanInterval) scanInterval;
@property (T@"<WFScanManagerScanProxy>",&,N,V_scanProxy) scanProxy;
@property (T@"NSMutableSet",&,N,V_networks) networks;
@property (T@"NSMutableArray",&,N,V_scanQueue) scanQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_internalQueue) internalQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_scanDispatchQueue) scanDispatchQueue;
@property (T@?,C,N,V_singleScanBlock) singleScanBlock;
@property (T@"NSMutableSet",&,N,V_hotspotPluginNetworks) hotspotPluginNetworks;
@property (TB,N,V_supportsHotspotHelper) supportsHotspotHelper;
@property (TB,N,V_supportsUnfilteredScanning) supportsUnfilteredScanning;
@property (TB,N,V_hotspotHelperScanning) hotspotHelperScanning;
@property (TB,N,V_useUIScanAPI) useUIScanAPI;
@property (Tq,V_numberOfScansPerformed) numberOfScansPerformed;
@property (TQ,V_consecutiveZeroFilteredScanResults) consecutiveZeroFilteredScanResults;
@property (TQ,V_consecutiveZeroUnFilteredScanResults) consecutiveZeroUnFilteredScanResults;
@property (TB,V_doUnFilteredScanning) doUnFilteredScanning;
```

## Instance methods

```
-[WFScanManager pause];
-[WFScanManager setNetworks:];
-[WFScanManager setState:];
-[WFScanManager scanInterval];
-[WFScanManager init];
-[WFScanManager stop];
-[WFScanManager networks];
-[WFScanManager dealloc];
-[WFScanManager start];
-[WFScanManager setDelegate:];
-[WFScanManager delegate];
-[WFScanManager setInternalQueue:];
-[WFScanManager setScanInterval:];
-[WFScanManager internalQueue];
-[WFScanManager resume];
-[WFScanManager state];
-[WFScanManager scanQueue];
-[WFScanManager setScanQueue:];
-[WFScanManager singleScanBlock];
-[WFScanManager _canResumeScanning];
-[WFScanManager _cancelQueuedScan];
-[WFScanManager _checkForNoNetworksFound];
-[WFScanManager _handleUIScanResultsDidChange:];
-[WFScanManager _handleUIScanResultsDidFinish:];
-[WFScanManager _isScanning];
-[WFScanManager _knownHiddenNetworkNames];
-[WFScanManager _performLegacyScan];
-[WFScanManager _performUIScan];
-[WFScanManager _processNextScan];
-[WFScanManager _queueScan];
-[WFScanManager _removeQueuedScans];
-[WFScanManager _resetNoNetworksFoundCounters];
-[WFScanManager _scan];
-[WFScanManager _scanningDidFinishWithError:];
-[WFScanManager _scanningWillStart];
-[WFScanManager _startHotspotPluginScan];
-[WFScanManager _stopNetworkPluginScan];
-[WFScanManager _updatePartialScanResults:];
-[WFScanManager consecutiveZeroFilteredScanResults];
-[WFScanManager consecutiveZeroUnFilteredScanResults];
-[WFScanManager doUnFilteredScanning];
-[WFScanManager hotspotHelperForScanRecord:];
-[WFScanManager hotspotHelperScanning];
-[WFScanManager hotspotPluginNetworks];
-[WFScanManager initWithScanProxy:delegate:];
-[WFScanManager initWithScanProxy:delegate:useUIScanAPI:];
-[WFScanManager numberOfScansPerformed];
-[WFScanManager scanDispatchQueue];
-[WFScanManager scanProxy];
-[WFScanManager setConsecutiveZeroFilteredScanResults:];
-[WFScanManager setConsecutiveZeroUnFilteredScanResults:];
-[WFScanManager setDoUnFilteredScanning:];
-[WFScanManager setHotspotHelperScanning:];
-[WFScanManager setHotspotPluginNetworks:];
-[WFScanManager setNumberOfScansPerformed:];
-[WFScanManager setScanDispatchQueue:];
-[WFScanManager setScanProxy:];
-[WFScanManager setSingleScanBlock:];
-[WFScanManager setSupportsHotspotHelper:];
-[WFScanManager setSupportsUnfilteredScanning:];
-[WFScanManager setTwentyPercentSkew:];
-[WFScanManager setUseUIScanAPI:];
-[WFScanManager supportsHotspotHelper];
-[WFScanManager supportsUnfilteredScanning];
-[WFScanManager useUIScanAPI];
```
