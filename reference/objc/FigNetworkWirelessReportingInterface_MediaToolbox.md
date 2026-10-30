# `FigNetworkWirelessReportingInterface`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"FigCoreWiFi" _wifiManager;
@"FigCoreTelephony" _cellManager;
@"FigWTEPredictionProvider" _wtePredictionProvider;
```

## Properties

```
@property (T@"FigCoreWiFi",R,N,V_wifiManager) wifiManager;
@property (T@"FigCoreTelephony",R,N,V_cellManager) cellManager;
@property (T@"FigWTEPredictionProvider",R,N,V_wtePredictionProvider) wtePredictionProvider;
```

## Class methods

```
+[FigNetworkWirelessReportingInterface globalInterface];
```

## Instance methods

```
-[FigNetworkWirelessReportingInterface wifiManager];
-[FigNetworkWirelessReportingInterface init];
-[FigNetworkWirelessReportingInterface cellManager];
-[FigNetworkWirelessReportingInterface wtePredictionProvider];
```
