# `WiFiAwareDeviceCapabilities`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 11 properties, 16 instance methods, 8 class methods

## Instance variables

```
C _supportedBands;
B _supportsDataTransfer;
@"NSSet" _supportedFeatures;
@"NSNumber" _operatingChannel;
@"NSNumber" _operatingClass;
@"NSArray" _supportedCipherSuites;
@"NSString" _discoveryInterfaceName;
q _maxPeers;
q _maxPublishers;
q _maxSubscribers;
q _maxDatapaths;
```

## Properties

```
@property (T@"NSSet",R,N,V_supportedFeatures) supportedFeatures;
@property (T@"NSNumber",R,N,V_operatingChannel) operatingChannel;
@property (T@"NSNumber",R,N,V_operatingClass) operatingClass;
@property (T@"NSArray",R,N,V_supportedCipherSuites) supportedCipherSuites;
@property (TC,R,N,V_supportedBands) supportedBands;
@property (TB,R,N,V_supportsDataTransfer) supportsDataTransfer;
@property (T@"NSString",R,N,V_discoveryInterfaceName) discoveryInterfaceName;
@property (Tq,R,N,V_maxPeers) maxPeers;
@property (Tq,R,N,V_maxPublishers) maxPublishers;
@property (Tq,R,N,V_maxSubscribers) maxSubscribers;
@property (Tq,R,N,V_maxDatapaths) maxDatapaths;
```

## Class methods

```
+[WiFiAwareDeviceCapabilities supportsSecureCoding];
+[WiFiAwareDeviceCapabilities currentDeviceCapabilities];
+[WiFiAwareDeviceCapabilities rotateAutoPairingBootstrapBlobs];
+[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlob:];
+[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlob:uuid:];
+[WiFiAwareDeviceCapabilities addorUpdateAutoPairingBootstrapBlobForPeer:];
+[WiFiAwareDeviceCapabilities deleteAutoPairingBootstrapBlobForClientUUID:];
+[WiFiAwareDeviceCapabilities fetchAutoPairingBootstrapBlob:error:];
```

## Instance methods

```
-[WiFiAwareDeviceCapabilities supportedFeatures];
-[WiFiAwareDeviceCapabilities initWithSupportedFeatures:operatingChannel:operatingClass:supportedCipherSuites:supportsDataTransfer:supportedBands:discoveryInterfaceName:maxPeers:maxPublishers:maxSubscribers:maxDatapaths:];
-[WiFiAwareDeviceCapabilities maxSubscribers];
-[WiFiAwareDeviceCapabilities supportedCipherSuites];
-[WiFiAwareDeviceCapabilities supportedBands];
-[WiFiAwareDeviceCapabilities maxDatapaths];
-[WiFiAwareDeviceCapabilities operatingChannel];
-[WiFiAwareDeviceCapabilities operatingClass];
-[WiFiAwareDeviceCapabilities supportsDataTransfer];
-[WiFiAwareDeviceCapabilities encodeWithCoder:];
-[WiFiAwareDeviceCapabilities discoveryInterfaceName];
-[WiFiAwareDeviceCapabilities description];
-[WiFiAwareDeviceCapabilities initWithCoder:];
-[WiFiAwareDeviceCapabilities maxPeers];
-[WiFiAwareDeviceCapabilities isEqual:];
-[WiFiAwareDeviceCapabilities maxPublishers];
```
