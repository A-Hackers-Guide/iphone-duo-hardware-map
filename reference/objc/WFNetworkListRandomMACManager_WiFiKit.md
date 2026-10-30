# `WFNetworkListRandomMACManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _shouldResetCache;
@"NSMutableDictionary" _cache;
@"WFClient" _client;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_cache) cache;
@property (T@"WFClient",&,N,V_client) client;
@property (TB,N,V_shouldResetCache) shouldResetCache;
```

## Instance methods

```
-[WFNetworkListRandomMACManager cache];
-[WFNetworkListRandomMACManager initWithClient:];
-[WFNetworkListRandomMACManager setClient:];
-[WFNetworkListRandomMACManager setCache:];
-[WFNetworkListRandomMACManager client];
-[WFNetworkListRandomMACManager cachedRandomMACForSSID:];
-[WFNetworkListRandomMACManager isSSIDinCache:];
-[WFNetworkListRandomMACManager newScanRecordWithRandomMACFromScanRecord:];
-[WFNetworkListRandomMACManager resetCacheWithCurrentNetworkName:];
-[WFNetworkListRandomMACManager setRandomMAC:forNetwork:mode:];
-[WFNetworkListRandomMACManager setShouldResetCache:];
-[WFNetworkListRandomMACManager shouldEnableRandomMACForSSID:];
-[WFNetworkListRandomMACManager shouldResetCache];
```
