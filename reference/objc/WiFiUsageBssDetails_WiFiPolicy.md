# `WiFiUsageBssDetails`

- Image: [`/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`](../userland/System__Library__PrivateFrameworks__WiFiPolicy.framework__WiFiPolicy.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 35 instance variables, 35 properties, 79 instance methods, 2 class methods

## Instance variables

```
B _mrsnoConnection;
B _isEdgeBss;
B _hasAppleIE;
B _hasInterworkingIE;
B _hasWpsIE;
B _hasDomainName;
B _hasNaiRealms;
B _hasRoamingOis;
B _hasColocatedMLOs;
i _phyMode;
i _band;
I _supportedAKMBitmask;
i _currentMloPreferredBand;
@"NSString" _bssid;
@"NSString" _apProfile;
@"NSError" _apProfileError;
d _locationLatitude;
d _locationLongitude;
q _nSS;
q _apMode;
q _channel;
q _channelWidth;
Q _channelFlags;
q _rssi;
q _rsnPriority;
Q _networkAccessCode;
Q _venueGroup;
Q _venueCode;
@"NSString" _manufacturerName;
@"NSString" _modelName;
@"NSString" _modelNumber;
@"NSString" _deviceVersion;
Q _currentMloLinksCount;
@"NSArray" _currentMloLinks;
@"NSNumber" _mloTrafficSwitchEnabled;
```

## Properties

```
@property (T@"NSString",C,N,V_bssid) bssid;
@property (Td,N,V_locationLatitude) locationLatitude;
@property (Td,N,V_locationLongitude) locationLongitude;
@property (Ti,N,V_phyMode) phyMode;
@property (Tq,N,V_apMode) apMode;
@property (Ti,N,V_band) band;
@property (Tq,N,V_channel) channel;
@property (Tq,N,V_channelWidth) channelWidth;
@property (TQ,N,V_channelFlags) channelFlags;
@property (Tq,N,V_rssi) rssi;
@property (TB,N,V_isEdgeBss) isEdgeBss;
@property (TQ,N,V_currentMloLinksCount) currentMloLinksCount;
@property (Ti,N,V_currentMloPreferredBand) currentMloPreferredBand;
@property (T@"NSArray",&,N,V_currentMloLinks) currentMloLinks;
@property (T@"NSNumber",&,N,V_mloTrafficSwitchEnabled) mloTrafficSwitchEnabled;
@property (T@"NSString",C,N,V_apProfile) apProfile;
@property (T@"NSError",C,N,V_apProfileError) apProfileError;
@property (Tq,N,V_nSS) nSS;
@property (Tq,N,V_rsnPriority) rsnPriority;
@property (TB,N,V_mrsnoConnection) mrsnoConnection;
@property (TI,N,V_supportedAKMBitmask) supportedAKMBitmask;
@property (TB,N,V_hasAppleIE) hasAppleIE;
@property (TB,N,V_hasInterworkingIE) hasInterworkingIE;
@property (TB,N,V_hasWpsIE) hasWpsIE;
@property (TB,N,V_hasDomainName) hasDomainName;
@property (TB,N,V_hasNaiRealms) hasNaiRealms;
@property (TB,N,V_hasRoamingOis) hasRoamingOis;
@property (TQ,N,V_networkAccessCode) networkAccessCode;
@property (TQ,N,V_venueGroup) venueGroup;
@property (TQ,N,V_venueCode) venueCode;
@property (T@"NSString",C,N,V_manufacturerName) manufacturerName;
@property (T@"NSString",C,N,V_modelName) modelName;
@property (T@"NSString",C,N,V_modelNumber) modelNumber;
@property (T@"NSString",C,N,V_deviceVersion) deviceVersion;
@property (TB,N,V_hasColocatedMLOs) hasColocatedMLOs;
```

## Class methods

```
+[WiFiUsageBssDetails bssWithIdentifier:apProfile:apMode:phyMode:channel:channelFlags:channelWidth:rssi:latitude:longitude:isEdgeBss:];
+[WiFiUsageBssDetails bssWithIdentifier:channel:channelFlags:rssi:];
```

## Instance methods

```
-[WiFiUsageBssDetails rssi];
-[WiFiUsageBssDetails modelNumber];
-[WiFiUsageBssDetails setChannel:];
-[WiFiUsageBssDetails channel];
-[WiFiUsageBssDetails currentMloPreferredBand];
-[WiFiUsageBssDetails venueGroup];
-[WiFiUsageBssDetails networkAccessCode];
-[WiFiUsageBssDetails setCurrentMloLinksCount:];
-[WiFiUsageBssDetails setSupportedAKMBitmask:];
-[WiFiUsageBssDetails mrsnoConnection];
-[WiFiUsageBssDetails setApProfile:];
-[WiFiUsageBssDetails currentMloLinks];
-[WiFiUsageBssDetails isEdgeBss];
-[WiFiUsageBssDetails setDeviceVersion:];
-[WiFiUsageBssDetails updateMLORuntimeConfig:];
-[WiFiUsageBssDetails phyMode];
-[WiFiUsageBssDetails hasDomainName];
-[WiFiUsageBssDetails setApMode:];
-[WiFiUsageBssDetails setModelNumber:];
-[WiFiUsageBssDetails locationLatitude];
-[WiFiUsageBssDetails apProfile];
-[WiFiUsageBssDetails setRssi:];
-[WiFiUsageBssDetails setHasRoamingOis:];
-[WiFiUsageBssDetails band];
-[WiFiUsageBssDetails setBssid:];
-[WiFiUsageBssDetails setHasDomainName:];
-[WiFiUsageBssDetails setHasWpsIE:];
-[WiFiUsageBssDetails setApProfileError:];
-[WiFiUsageBssDetails nSS];
-[WiFiUsageBssDetails currentMloLinksCount];
-[WiFiUsageBssDetails eventDictionary:];
-[WiFiUsageBssDetails setHasAppleIE:];
-[WiFiUsageBssDetails setIsEdgeBss:];
-[WiFiUsageBssDetails redactedDescription];
-[WiFiUsageBssDetails setHasInterworkingIE:];
-[WiFiUsageBssDetails channelFlags];
-[WiFiUsageBssDetails isOnChannel:];
-[WiFiUsageBssDetails setNetworkAccessCode:];
-[WiFiUsageBssDetails setMloTrafficSwitchEnabled:];
-[WiFiUsageBssDetails hasRoamingOis];
-[WiFiUsageBssDetails channelWidth];
-[WiFiUsageBssDetails supportedAKMBitmask];
-[WiFiUsageBssDetails hasWpsIE];
-[WiFiUsageBssDetails setModelName:];
-[WiFiUsageBssDetails deviceVersion];
-[WiFiUsageBssDetails setBand:];
-[WiFiUsageBssDetails manufacturerName];
-[WiFiUsageBssDetails setManufacturerName:];
-[WiFiUsageBssDetails hasColocatedMLOs];
-[WiFiUsageBssDetails setLocationLongitude:];
-[WiFiUsageBssDetails hasNaiRealms];
-[WiFiUsageBssDetails hash];
-[WiFiUsageBssDetails rsnPriority];
-[WiFiUsageBssDetails hasAppleIE];
-[WiFiUsageBssDetails setRsnPriority:];
-[WiFiUsageBssDetails description];
-[WiFiUsageBssDetails bssid];
-[WiFiUsageBssDetails setHasColocatedMLOs:];
-[WiFiUsageBssDetails venueCode];
-[WiFiUsageBssDetails apProfileError];
-[WiFiUsageBssDetails setVenueGroup:];
-[WiFiUsageBssDetails apMode];
-[WiFiUsageBssDetails hasInterworkingIE];
-[WiFiUsageBssDetails setNSS:];
-[WiFiUsageBssDetails copyWithZone:];
-[WiFiUsageBssDetails setChannelWidth:];
-[WiFiUsageBssDetails setCurrentMloPreferredBand:];
-[WiFiUsageBssDetails setChannelFlags:];
-[WiFiUsageBssDetails mloTrafficSwitchEnabled];
-[WiFiUsageBssDetails setVenueCode:];
-[WiFiUsageBssDetails isEqual:];
-[WiFiUsageBssDetails locationLongitude];
-[WiFiUsageBssDetails setHasNaiRealms:];
-[WiFiUsageBssDetails setMrsnoConnection:];
-[WiFiUsageBssDetails supportedAKMsAsDictionary:];
-[WiFiUsageBssDetails setPhyMode:];
-[WiFiUsageBssDetails modelName];
-[WiFiUsageBssDetails setLocationLatitude:];
-[WiFiUsageBssDetails setCurrentMloLinks:];
```
