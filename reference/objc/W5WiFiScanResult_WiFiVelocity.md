# `W5WiFiScanResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 18 instance variables, 18 properties, 50 instance methods, 1 class methods

## Instance variables

```
B _isIBSS;
B _isPasspoint;
B _isPersonalHotspot;
B _isAppleSWAP;
B _supportsWEPCipher;
B _supportsTKIPCipher;
i _supportedPHYModes;
@"NSDictionary" _scanRecord;
@"NSData" _ssid;
@"NSString" _ssidString;
@"NSString" _bssid;
@"NSArray" _supportedSecurityTypes;
q _rssi;
q _noise;
@"NSString" _countryCode;
q _beaconInterval;
@"NSString" _airPortBaseStationModelName;
@"W5WiFiChannel" _channel;
```

## Properties

```
@property (T@"NSDictionary",C,N,V_scanRecord) scanRecord;
@property (T@"NSData",C,N,V_ssid) ssid;
@property (T@"NSString",C,N,V_ssidString) ssidString;
@property (T@"NSString",C,N,V_bssid) bssid;
@property (T@"NSArray",C,N,V_supportedSecurityTypes) supportedSecurityTypes;
@property (Ti,N,V_supportedPHYModes) supportedPHYModes;
@property (Tq,N,V_rssi) rssi;
@property (Tq,N,V_noise) noise;
@property (TB,N,V_isIBSS) isIBSS;
@property (T@"NSString",C,N,V_countryCode) countryCode;
@property (Tq,N,V_beaconInterval) beaconInterval;
@property (TB,N,V_isPasspoint) isPasspoint;
@property (TB,N,V_isPersonalHotspot) isPersonalHotspot;
@property (TB,N,V_isAppleSWAP) isAppleSWAP;
@property (T@"NSString",C,N,V_airPortBaseStationModelName) airPortBaseStationModelName;
@property (T@"W5WiFiChannel",C,N,V_channel) channel;
@property (TB,N,V_supportsWEPCipher) supportsWEPCipher;
@property (TB,N,V_supportsTKIPCipher) supportsTKIPCipher;
```

## Class methods

```
+[W5WiFiScanResult supportsSecureCoding];
```

## Instance methods

```
-[W5WiFiScanResult rssi];
-[W5WiFiScanResult setChannel:];
-[W5WiFiScanResult setNoise:];
-[W5WiFiScanResult ssid];
-[W5WiFiScanResult setSsid:];
-[W5WiFiScanResult channel];
-[W5WiFiScanResult supportedPHYModes];
-[W5WiFiScanResult isPersonalHotspot];
-[W5WiFiScanResult noise];
-[W5WiFiScanResult setIsPersonalHotspot:];
-[W5WiFiScanResult dealloc];
-[W5WiFiScanResult setRssi:];
-[W5WiFiScanResult setIsPasspoint:];
-[W5WiFiScanResult setBssid:];
-[W5WiFiScanResult countryCode];
-[W5WiFiScanResult isPasspoint];
-[W5WiFiScanResult encodeWithCoder:];
-[W5WiFiScanResult conformsToProtocol:];
-[W5WiFiScanResult hash];
-[W5WiFiScanResult description];
-[W5WiFiScanResult bssid];
-[W5WiFiScanResult initWithCoder:];
-[W5WiFiScanResult copyWithZone:];
-[W5WiFiScanResult isEqual:];
-[W5WiFiScanResult setCountryCode:];
-[W5WiFiScanResult beaconInterval];
-[W5WiFiScanResult scanRecord];
-[W5WiFiScanResult setBeaconInterval:];
-[W5WiFiScanResult fastestSupportedPHYMode];
-[W5WiFiScanResult isAppleSWAP];
-[W5WiFiScanResult isEqualToScanResult:];
-[W5WiFiScanResult isIBSS];
-[W5WiFiScanResult setSupportedSecurityTypes:];
-[W5WiFiScanResult supportedSecurityTypes];
-[W5WiFiScanResult ssidString];
-[W5WiFiScanResult setAirPortBaseStationModelName:];
-[W5WiFiScanResult setIsAppleSWAP:];
-[W5WiFiScanResult airPortBaseStationModelName];
-[W5WiFiScanResult isAirPortBaseStation:modelID:];
-[W5WiFiScanResult setIsIBSS:];
-[W5WiFiScanResult setScanRecord:];
-[W5WiFiScanResult setSsidString:];
-[W5WiFiScanResult setSupportedPHYModes:];
-[W5WiFiScanResult setSupportsTKIPCipher:];
-[W5WiFiScanResult setSupportsWEPCipher:];
-[W5WiFiScanResult strongestSupportedSecurity];
-[W5WiFiScanResult supportsPHYMode:];
-[W5WiFiScanResult supportsSecurity:];
-[W5WiFiScanResult supportsTKIPCipher];
-[W5WiFiScanResult supportsWEPCipher];
```
