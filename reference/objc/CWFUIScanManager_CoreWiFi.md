# `CWFUIScanManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 5 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _scansInProgress;
@"NSMutableDictionary" _scanCache;
@"NSMutableDictionary" _scanCacheTimestamps;
@"NSMutableDictionary" _scanQueues;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSArray" _bandChannels;
@? _issueScanHandler;
@? _finishedScanHandler;
@? _hiddenNetworkNameHandler;
```

## Properties

```
@property (T@"NSArray",C,N,V_bandChannels) bandChannels;
@property (T@?,C,V_issueScanHandler) issueScanHandler;
@property (T@?,C,V_finishedScanHandler) finishedScanHandler;
@property (T@?,C,V_hiddenNetworkNameHandler) hiddenNetworkNameHandler;
@property (T@"NSArray",R,N) passpointANQPElementIDList;
```

## Instance methods

```
-[CWFUIScanManager resetCache];
-[CWFUIScanManager init];
-[CWFUIScanManager _performDirectedScanWithRetry:interfaceName:attempt:completion:];
-[CWFUIScanManager _accumulateScanResults:forInterface:];
-[CWFUIScanManager _channelBandForScanType:];
-[CWFUIScanManager _performDirectedScan:interfaceName:completion:];
-[CWFUIScanManager _performDirectedScanWithRetry:interfaceName:completion:];
-[CWFUIScanManager _performScan:interfaceName:completion:];
-[CWFUIScanManager _performScanWithRetry:interfaceName:attempt:completion:];
-[CWFUIScanManager _performScanWithRetry:interfaceName:completion:];
-[CWFUIScanManager _scanTypeNameForScanType:];
-[CWFUIScanManager addScanResults:forInterface:];
-[CWFUIScanManager bandChannels];
-[CWFUIScanManager cachedScanResultsForInterface:];
-[CWFUIScanManager cancelScansForInterfaceName:];
-[CWFUIScanManager didUpdateKnownNetwork:previousNetwork:eventType:];
-[CWFUIScanManager finishedScanHandler];
-[CWFUIScanManager getScanParamsForCacheFiltering];
-[CWFUIScanManager hiddenNetworkNameHandler];
-[CWFUIScanManager issueScanHandler];
-[CWFUIScanManager passpointANQPElementIDList];
-[CWFUIScanManager sanitizeCacheResult:];
-[CWFUIScanManager setBandChannels:];
-[CWFUIScanManager setFinishedScanHandler:];
-[CWFUIScanManager setHiddenNetworkNameHandler:];
-[CWFUIScanManager setIssueScanHandler:];
-[CWFUIScanManager startScansForInterfaceName:];
```
