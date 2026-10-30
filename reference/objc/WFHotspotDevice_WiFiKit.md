# `WFHotspotDevice`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFNetworkListRecord`
- 2 instance variables, 6 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"SFRemoteHotspotDevice" _hotspotDevice;
@"NSString" _ssid;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SFRemoteHotspotDevice",&,N,V_hotspotDevice) hotspotDevice;
@property (T@"NSString",C,N,V_ssid) ssid;
```

## Instance methods

```
-[WFHotspotDevice rssi];
-[WFHotspotDevice isKnown];
-[WFHotspotDevice signalBars];
-[WFHotspotDevice ssid];
-[WFHotspotDevice setSsid:];
-[WFHotspotDevice isSecure];
-[WFHotspotDevice isEnterprise];
-[WFHotspotDevice scaledRSSI];
-[WFHotspotDevice subtitle];
-[WFHotspotDevice init];
-[WFHotspotDevice uniqueIdentifier];
-[WFHotspotDevice isAdhoc];
-[WFHotspotDevice title];
-[WFHotspotDevice isInstantHotspot];
-[WFHotspotDevice hash];
-[WFHotspotDevice description];
-[WFHotspotDevice isEqual:];
-[WFHotspotDevice securityMode];
-[WFHotspotDevice cellularSlicingIsEnabled];
-[WFHotspotDevice prominentDisplay];
-[WFHotspotDevice _isEqualToHotspotDevice:];
-[WFHotspotDevice _isEqualToNetwork:];
-[WFHotspotDevice canBeDisplayedAsCurrent];
-[WFHotspotDevice hotspotBatteryLife];
-[WFHotspotDevice hotspotCellularProtocol];
-[WFHotspotDevice hotspotDevice];
-[WFHotspotDevice hotspotSignalStrength];
-[WFHotspotDevice iOSHotspot];
-[WFHotspotDevice initWithHotspotDevice:];
-[WFHotspotDevice isEquivalentRecord:];
-[WFHotspotDevice isHotspot20];
-[WFHotspotDevice isPopular];
-[WFHotspotDevice isUnconfiguredAccessory];
-[WFHotspotDevice lastJoinedDate];
-[WFHotspotDevice setHotspotDevice:];
-[WFHotspotDevice setScaledRSSI:];
-[WFHotspotDevice shouldShowInKnownNetworkList];
-[WFHotspotDevice shouldShowInMyNetworkList];
```
