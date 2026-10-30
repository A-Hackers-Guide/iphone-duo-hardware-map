# `CWFWiFiNetworkSharingAskToShareScanResult`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _isConnected;
B _wasFoundOnAccessory;
B _isConnectedOnAccessory;
@"NSData" _SSID;
d _signalStrength;
d _signalStrengthOnAccessory;
```

## Properties

```
@property (T@"NSString",R) networkName;
@property (T@"NSData",C,V_SSID) SSID;
@property (Td,V_signalStrength) signalStrength;
@property (TB,V_isConnected) isConnected;
@property (TB,V_wasFoundOnAccessory) wasFoundOnAccessory;
@property (Td,V_signalStrengthOnAccessory) signalStrengthOnAccessory;
@property (TB,V_isConnectedOnAccessory) isConnectedOnAccessory;
```

## Class methods

```
+[CWFWiFiNetworkSharingAskToShareScanResult supportsSecureCoding];
```

## Instance methods

```
-[CWFWiFiNetworkSharingAskToShareScanResult signalStrength];
-[CWFWiFiNetworkSharingAskToShareScanResult isConnected];
-[CWFWiFiNetworkSharingAskToShareScanResult networkName];
-[CWFWiFiNetworkSharingAskToShareScanResult setSSID:];
-[CWFWiFiNetworkSharingAskToShareScanResult SSID];
-[CWFWiFiNetworkSharingAskToShareScanResult encodeWithCoder:];
-[CWFWiFiNetworkSharingAskToShareScanResult hash];
-[CWFWiFiNetworkSharingAskToShareScanResult description];
-[CWFWiFiNetworkSharingAskToShareScanResult initWithCoder:];
-[CWFWiFiNetworkSharingAskToShareScanResult copyWithZone:];
-[CWFWiFiNetworkSharingAskToShareScanResult setIsConnected:];
-[CWFWiFiNetworkSharingAskToShareScanResult isEqual:];
-[CWFWiFiNetworkSharingAskToShareScanResult setSignalStrength:];
-[CWFWiFiNetworkSharingAskToShareScanResult isConnectedOnAccessory];
-[CWFWiFiNetworkSharingAskToShareScanResult isEqualToWiFiNetworkSharingAskToShareScanResult:];
-[CWFWiFiNetworkSharingAskToShareScanResult setIsConnectedOnAccessory:];
-[CWFWiFiNetworkSharingAskToShareScanResult setSignalStrengthOnAccessory:];
-[CWFWiFiNetworkSharingAskToShareScanResult setWasFoundOnAccessory:];
-[CWFWiFiNetworkSharingAskToShareScanResult signalStrengthOnAccessory];
-[CWFWiFiNetworkSharingAskToShareScanResult wasFoundOnAccessory];
```
