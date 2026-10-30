# `WFOtherNetworkProviderContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFCredentialsProviderContext`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) WAPIEnabled;
@property (T@"NSArray",R,N) WAPIRootCertificates;
@property (T@"NSArray",R,N) WAPIIdentities;
@property (TB,R,N) supportsRandomMACAddress;
@property (TB,R,N) isUsingRandomMACAddress;
@property (T@"NSString",R,C,N) randomMACAddress;
@property (T@"NSString",R,C,N) hardwareMACAddress;
```

## Instance methods

```
-[WFOtherNetworkProviderContext hardwareMACAddress];
-[WFOtherNetworkProviderContext WAPIEnabled];
-[WFOtherNetworkProviderContext WAPIIdentities];
-[WFOtherNetworkProviderContext WAPIRootCertificates];
-[WFOtherNetworkProviderContext isUsingRandomMACAddress];
-[WFOtherNetworkProviderContext randomMACAddress];
-[WFOtherNetworkProviderContext supportsRandomMACAddress];
-[WFOtherNetworkProviderContext savePrivateAddressMode:];
```
