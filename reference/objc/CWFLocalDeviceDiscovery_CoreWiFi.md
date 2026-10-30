# `CWFLocalDeviceDiscovery`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
^{_LXLexicon=} _lexiconEnglish;
^{_LXLexicon=} _lexiconUserLocale;
@? _handler;
@"NSObject<OS_dispatch_queue>" _mrcQueue;
@"NSCharacterSet" _tokenizationCharacterSet;
@"NSDictionary" _filteredNames;
@"NSObject<OS_mrc_cached_local_records_inquiry>" _mrcInquiry;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_mrcQueue) mrcQueue;
@property (T@"NSCharacterSet",&,N,V_tokenizationCharacterSet) tokenizationCharacterSet;
@property (T@"NSDictionary",R,N,V_filteredNames) filteredNames;
@property (T@"NSObject<OS_mrc_cached_local_records_inquiry>",&,N,V_mrcInquiry) mrcInquiry;
@property (T@?,C,N,V_handler) handler;
```

## Instance methods

```
-[CWFLocalDeviceDiscovery init];
-[CWFLocalDeviceDiscovery dealloc];
-[CWFLocalDeviceDiscovery setHandler:];
-[CWFLocalDeviceDiscovery invalidate];
-[CWFLocalDeviceDiscovery handler];
-[CWFLocalDeviceDiscovery activate];
-[CWFLocalDeviceDiscovery _tokenizeStringForSpecialCharacters:];
-[CWFLocalDeviceDiscovery setTokenizationCharacterSet:];
-[CWFLocalDeviceDiscovery tokenizationCharacterSet];
-[CWFLocalDeviceDiscovery processRecords:];
-[CWFLocalDeviceDiscovery _callHandlerWithValidResults:filtered:];
-[CWFLocalDeviceDiscovery _combineDevicesWithDifferentSourceAddresses:];
-[CWFLocalDeviceDiscovery _filterName:forLexicon:];
-[CWFLocalDeviceDiscovery _processMRCRecord:];
-[CWFLocalDeviceDiscovery discover];
-[CWFLocalDeviceDiscovery filteredNames];
-[CWFLocalDeviceDiscovery mrcInquiry];
-[CWFLocalDeviceDiscovery mrcQueue];
-[CWFLocalDeviceDiscovery setMrcInquiry:];
-[CWFLocalDeviceDiscovery setMrcQueue:];
```
