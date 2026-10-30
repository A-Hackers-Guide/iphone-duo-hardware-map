# `FigCoreWiFi`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigReentrantMutex=} _wifiStatsLock;
@"CWFInterface" cwfInterface;
@"NSDictionary" wifiStats;
@"NSString" ssid;
```

## Instance methods

```
-[FigCoreWiFi dealloc];
-[FigCoreWiFi initWithError:];
-[FigCoreWiFi getLatestWiFiStats];
-[FigCoreWiFi initializeWifiStatsFromCachedData];
-[FigCoreWiFi refreshSSIDFromCoreWifiInterface];
-[FigCoreWiFi updateWifiStatsWithLinkQualityData:];
-[FigCoreWiFi withWifiStatsLock:];
```
