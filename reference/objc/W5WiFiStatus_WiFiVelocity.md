# `W5WiFiStatus`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 48 instance variables, 48 properties, 105 instance methods, 1 class methods

## Instance variables

```
B _powerOn;
B _smartCCADesenseSupported;
B _smartCCADesenseUSBPresence;
B _isSnifferSupported;
i _opMode;
I _eapolControlMode;
I _eapolSupplicantState;
i _phyMode;
i _btcMode;
@"NSString" _macAddress;
@"NSString" _hardwareMACAddress;
@"NSString" _interfaceName;
@"NSArray" _capabilities;
@"NSData" _power;
@"NSString" _ssidString;
@"NSData" _ssid;
@"NSString" _bssid;
q _rssi;
Q _cca;
q _noise;
Q _txPacketErrorRate;
d _txRate;
q _security;
Q _mcsIndex;
Q _guardInterval;
Q _numberOfSpacialStreams;
@"W5WiFiChannel" _channel;
@"NSArray" _linkQualityUpdates;
@"NSArray" _supportedChannels;
@"NSString" _countryCode;
@"NSString" _networkServiceID;
q _ipv4ConfigMethod;
q _ipv6ConfigMethod;
@"NSArray" _ipv4Addresses;
@"NSArray" _ipv6Addresses;
@"NSString" _ipv4RouterAddress;
@"NSString" _ipv6RouterAddress;
@"NSArray" _dnsAddresses;
@"NSData" _chainAck;
@"NSData" _txChainPower;
@"NSData" _desense;
@"NSData" _desenseLevel;
@"NSData" _btcConfig;
@"NSData" _btcProfiles2GHz;
@"NSData" _btcProfiles5GHz;
@"W5WiFiScanResult" _lastJoinedScanResult;
@"W5WiFiPreferredNetwork" _lastJoinedPreferredNetwork;
@"NSArray" _cachedScanResults;
```

## Properties

```
@property (T@"NSString",C,N,V_macAddress) macAddress;
@property (T@"NSString",C,N,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (T@"NSArray",C,N,V_capabilities) capabilities;
@property (TB,N,V_powerOn) powerOn;
@property (T@"NSData",C,N,V_power) power;
@property (Ti,N,V_opMode) opMode;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (Tq,N,V_rssi) rssi;
@property (TQ,N,V_cca) cca;
@property (Tq,N,V_noise) noise;
@property (TQ,N,V_txPacketErrorRate) txPacketErrorRate;
@property (Td,N,V_txRate) txRate;
@property (Tq,N,V_security) security;
@property (TI,N,V_eapolControlMode) eapolControlMode;
@property (TI,N,V_eapolSupplicantState) eapolSupplicantState;
@property (Ti,N,V_phyMode) phyMode;
@property (TQ,N,V_mcsIndex) mcsIndex;
@property (TQ,N,V_guardInterval) guardInterval;
@property (TQ,N,V_numberOfSpacialStreams) numberOfSpacialStreams;
@property (T@"W5WiFiChannel",C,N,V_channel) channel;
@property (T@"NSArray",C,N,V_linkQualityUpdates) linkQualityUpdates;
@property (T@"NSArray",C,N,V_supportedChannels) supportedChannels;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (T@"NSString",C,N,V_networkServiceID) networkServiceID;
@property (Tq,N,V_ipv4ConfigMethod) ipv4ConfigMethod;
@property (Tq,N,V_ipv6ConfigMethod) ipv6ConfigMethod;
@property (T@"NSArray",C,N,V_ipv4Addresses) ipv4Addresses;
@property (T@"NSArray",C,N,V_ipv6Addresses) ipv6Addresses;
@property (T@"NSString",C,N,V_ipv4RouterAddress) ipv4RouterAddress;
@property (T@"NSString",C,N,V_ipv6RouterAddress) ipv6RouterAddress;
@property (T@"NSArray",C,N,V_dnsAddresses) dnsAddresses;
@property (Ti,N,V_btcMode) btcMode;
@property (T@"NSData",C,N,V_chainAck) chainAck;
@property (T@"NSData",C,N,V_txChainPower) txChainPower;
@property (T@"NSData",C,N,V_desense) desense;
@property (T@"NSData",C,N,V_desenseLevel) desenseLevel;
@property (T@"NSData",C,N,V_btcConfig) btcConfig;
@property (T@"NSData",C,N,V_btcProfiles2GHz) btcProfiles2GHz;
@property (T@"NSData",C,N,V_btcProfiles5GHz) btcProfiles5GHz;
@property (T@"W5WiFiScanResult",C,N,V_lastJoinedScanResult) lastJoinedScanResult;
@property (T@"W5WiFiPreferredNetwork",C,N,V_lastJoinedPreferredNetwork) lastJoinedPreferredNetwork;
@property (T@"NSArray",C,N,V_cachedScanResults) cachedScanResults;
@property (TB,N,V_smartCCADesenseSupported) smartCCADesenseSupported;
@property (TB,N,V_smartCCADesenseUSBPresence) smartCCADesenseUSBPresence;
@property (TB,N,V_isSnifferSupported) isSnifferSupported;
```

## Class methods

```
+[W5WiFiStatus supportsSecureCoding];
```

## Instance methods

```
-[W5WiFiStatus power];
-[W5WiFiStatus rssi];
-[W5WiFiStatus cca];
-[W5WiFiStatus hardwareMACAddress];
-[W5WiFiStatus setChannel:];
-[W5WiFiStatus setNoise:];
-[W5WiFiStatus opMode];
-[W5WiFiStatus ssid];
-[W5WiFiStatus setSsid:];
-[W5WiFiStatus powerOn];
-[W5WiFiStatus channel];
-[W5WiFiStatus networkServiceID];
-[W5WiFiStatus txChainPower];
-[W5WiFiStatus txRate];
-[W5WiFiStatus guardInterval];
-[W5WiFiStatus desenseLevel];
-[W5WiFiStatus chainAck];
-[W5WiFiStatus ipv4Addresses];
-[W5WiFiStatus desense];
-[W5WiFiStatus macAddress];
-[W5WiFiStatus setTxRate:];
-[W5WiFiStatus noise];
-[W5WiFiStatus phyMode];
-[W5WiFiStatus ipv4RouterAddress];
-[W5WiFiStatus setInterfaceName:];
-[W5WiFiStatus setCca:];
-[W5WiFiStatus dealloc];
-[W5WiFiStatus setRssi:];
-[W5WiFiStatus setSupportedChannels:];
-[W5WiFiStatus setBssid:];
-[W5WiFiStatus interfaceName];
-[W5WiFiStatus setMacAddress:];
-[W5WiFiStatus ipv6Addresses];
-[W5WiFiStatus countryCode];
-[W5WiFiStatus supportedChannels];
-[W5WiFiStatus encodeWithCoder:];
-[W5WiFiStatus capabilities];
-[W5WiFiStatus conformsToProtocol:];
-[W5WiFiStatus hash];
-[W5WiFiStatus security];
-[W5WiFiStatus description];
-[W5WiFiStatus bssid];
-[W5WiFiStatus initWithCoder:];
-[W5WiFiStatus copyWithZone:];
-[W5WiFiStatus setCapabilities:];
-[W5WiFiStatus isEqual:];
-[W5WiFiStatus setPhyMode:];
-[W5WiFiStatus setCountryCode:];
-[W5WiFiStatus setSecurity:];
-[W5WiFiStatus setIpv4RouterAddress:];
-[W5WiFiStatus setPower:];
-[W5WiFiStatus setIpv4Addresses:];
-[W5WiFiStatus setIpv6Addresses:];
-[W5WiFiStatus txPacketErrorRate];
-[W5WiFiStatus setPowerOn:];
-[W5WiFiStatus btcMode];
-[W5WiFiStatus eapolControlMode];
-[W5WiFiStatus eapolSupplicantState];
-[W5WiFiStatus mcsIndex];
-[W5WiFiStatus numberOfSpacialStreams];
-[W5WiFiStatus ssidString];
-[W5WiFiStatus cachedScanResults];
-[W5WiFiStatus setSmartCCADesenseSupported:];
-[W5WiFiStatus smartCCADesenseSupported];
-[W5WiFiStatus ipv4ConfigMethod];
-[W5WiFiStatus ipv6ConfigMethod];
-[W5WiFiStatus ipv6RouterAddress];
-[W5WiFiStatus setHardwareMACAddress:];
-[W5WiFiStatus setIpv6RouterAddress:];
-[W5WiFiStatus btcProfiles2GHz];
-[W5WiFiStatus btcProfiles5GHz];
-[W5WiFiStatus btcConfig];
-[W5WiFiStatus dnsAddresses];
-[W5WiFiStatus isEqualToWiFiStatus:];
-[W5WiFiStatus isSnifferSupported];
-[W5WiFiStatus lastJoinedPreferredNetwork];
-[W5WiFiStatus lastJoinedScanResult];
-[W5WiFiStatus linkQualityUpdates];
-[W5WiFiStatus setBtcConfig:];
-[W5WiFiStatus setBtcMode:];
-[W5WiFiStatus setBtcProfiles2GHz:];
-[W5WiFiStatus setBtcProfiles5GHz:];
-[W5WiFiStatus setCachedScanResults:];
-[W5WiFiStatus setChainAck:];
-[W5WiFiStatus setDesense:];
-[W5WiFiStatus setDesenseLevel:];
-[W5WiFiStatus setDnsAddresses:];
-[W5WiFiStatus setEapolControlMode:];
-[W5WiFiStatus setEapolSupplicantState:];
-[W5WiFiStatus setGuardInterval:];
-[W5WiFiStatus setIpv4ConfigMethod:];
-[W5WiFiStatus setIpv6ConfigMethod:];
-[W5WiFiStatus setIsSnifferSupported:];
-[W5WiFiStatus setLastJoinedPreferredNetwork:];
-[W5WiFiStatus setLastJoinedScanResult:];
-[W5WiFiStatus setLinkQualityUpdates:];
-[W5WiFiStatus setMcsIndex:];
-[W5WiFiStatus setNetworkServiceID:];
-[W5WiFiStatus setNumberOfSpacialStreams:];
-[W5WiFiStatus setOpMode:];
-[W5WiFiStatus setSmartCCADesenseUSBPresence:];
-[W5WiFiStatus setSsidString:];
-[W5WiFiStatus setTxChainPower:];
-[W5WiFiStatus setTxPacketErrorRate:];
-[W5WiFiStatus smartCCADesenseUSBPresence];
```
