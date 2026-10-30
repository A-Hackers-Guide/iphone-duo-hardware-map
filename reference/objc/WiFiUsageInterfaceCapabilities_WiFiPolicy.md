# `WiFiUsageInterfaceCapabilities`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
i _supportedPhyModes;
@"NSString" _interfaceName;
^{_Apple80211=} _a11Ref;
Q _maxPHYRate;
@"NSSet" _deviceCapabilities;
```

## Properties

```
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T^{_Apple80211=},N,V_a11Ref) a11Ref;
@property (TQ,N,V_maxPHYRate) maxPHYRate;
@property (Ti,N,V_supportedPhyModes) supportedPhyModes;
@property (T@"NSSet",&,N,V_deviceCapabilities) deviceCapabilities;
```

## Instance methods

```
-[WiFiUsageInterfaceCapabilities deviceCapabilities];
-[WiFiUsageInterfaceCapabilities setInterfaceName:];
-[WiFiUsageInterfaceCapabilities dealloc];
-[WiFiUsageInterfaceCapabilities interfaceName];
-[WiFiUsageInterfaceCapabilities setDeviceCapabilities:];
-[WiFiUsageInterfaceCapabilities initWithInterfaceName:];
-[WiFiUsageInterfaceCapabilities description];
-[WiFiUsageInterfaceCapabilities deviceSupports:];
-[WiFiUsageInterfaceCapabilities a11Ref];
-[WiFiUsageInterfaceCapabilities currentNumberOfSpatialStreams];
-[WiFiUsageInterfaceCapabilities maxInterfacePHYRate];
-[WiFiUsageInterfaceCapabilities maxPHYRate];
-[WiFiUsageInterfaceCapabilities setA11Ref:];
-[WiFiUsageInterfaceCapabilities setMaxPHYRate:];
-[WiFiUsageInterfaceCapabilities setSupportedPhyModes:];
-[WiFiUsageInterfaceCapabilities supportedPhyModes];
```
