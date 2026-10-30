# `WFDetailContextPrivateAddressConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _connectedWithHardwareAddress;
B _alwaysDisplayRandomAddress;
B _privateAddressSupported;
Q _privateAddressMode;
@"NSString" _randomMACAddress;
@"NSString" _hardwareMACAddress;
```

## Properties

```
@property (TQ,N,V_privateAddressMode) privateAddressMode;
@property (T@"NSString",C,N,V_randomMACAddress) randomMACAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (TB,N,GisConnectedWithHardwareAddress,V_connectedWithHardwareAddress) connectedWithHardwareAddress;
@property (TB,N,GisPrivateAddressSupported,V_privateAddressSupported) privateAddressSupported;
@property (TB,R,N,GisAlwaysDisplayRandomAddress,V_alwaysDisplayRandomAddress) alwaysDisplayRandomAddress;
```

## Instance methods

```
-[WFDetailContextPrivateAddressConfig hardwareMACAddress];
-[WFDetailContextPrivateAddressConfig initWithRandomMACAddress:hardwareMACAddress:privateAddressMode:connectedWithHardwareAddress:privateAddressSupported:];
-[WFDetailContextPrivateAddressConfig isAlwaysDisplayRandomAddress];
-[WFDetailContextPrivateAddressConfig isConnectedWithHardwareAddress];
-[WFDetailContextPrivateAddressConfig isPrivateAddressSupported];
-[WFDetailContextPrivateAddressConfig privateAddressMode];
-[WFDetailContextPrivateAddressConfig randomMACAddress];
-[WFDetailContextPrivateAddressConfig setConnectedWithHardwareAddress:];
-[WFDetailContextPrivateAddressConfig setHardwareMACAddress:];
-[WFDetailContextPrivateAddressConfig setPrivateAddressMode:];
-[WFDetailContextPrivateAddressConfig setPrivateAddressSupported:];
-[WFDetailContextPrivateAddressConfig setRandomMACAddress:];
```
