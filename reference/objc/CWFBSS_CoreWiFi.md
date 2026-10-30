# `CWFBSS`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 1 instance variables, 18 properties, 58 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _internal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSMutableDictionary",&,N,V_internal) internal;
@property (T@"NSSet",R,C,D,N) properties;
@property (T@"NSString",C,D,N) BSSID;
@property (T@"CWFChannel",C,D,N) channel;
@property (T@"NSDate",C,D,N) lastAssociatedAt;
@property (T@"CLLocation",C,D,N) location;
@property (T@"NSDate",C,D,N) AWDLRealTimeModeTimestamp;
@property (T@"NSData",C,D,N) DHCPServerID;
@property (T@"NSData",C,D,N) DHCPv6ServerID;
@property (T@"NSString",C,D,N) IPv4NetworkSignature;
@property (T@"NSString",C,D,N) IPv6NetworkSignature;
@property (T@"CWFChannel",C,D,N) colocated2GHzRNRChannel;
@property (T@"CWFChannel",C,D,N) colocated5GHzRNRChannel;
@property (T@"NSDictionary",C,D,N) OSSpecificAttributes;
```

## Class methods

```
+[CWFBSS supportsSecureCoding];
+[CWFBSS supportedOSSpecificKeys];
```

## Instance methods

```
-[CWFBSS IPv4NetworkSignature];
-[CWFBSS setChannel:];
-[CWFBSS channel];
-[CWFBSS colocated5GHzRNRChannel];
-[CWFBSS IPv6NetworkSignature];
-[CWFBSS DHCPServerID];
-[CWFBSS properties];
-[CWFBSS DHCPv6ServerID];
-[CWFBSS BSSID];
-[CWFBSS JSONCompatibleKeyValueMap];
-[CWFBSS setBSSID:];
-[CWFBSS debugDescription];
-[CWFBSS __infoForLocation:];
-[CWFBSS colocated2GHzRNRChannel];
-[CWFBSS init];
-[CWFBSS location];
-[CWFBSS isEqualToBSS:];
-[CWFBSS coreWiFiSpecificAttributes];
-[CWFBSS __classDStorageProperties];
-[CWFBSS __defaultProperties];
-[CWFBSS externalForm];
-[CWFBSS __locationFromInfo:];
-[CWFBSS __filteredBSSWithProperties:OSSpecificKeys:];
-[CWFBSS wasJoinedRecentlyInProximityOf:];
-[CWFBSS setLastAssociatedAt:];
-[CWFBSS filteredBSSForClassDStorage];
-[CWFBSS setOSSpecificAttributes:];
-[CWFBSS OSSpecificValueForKey:];
-[CWFBSS setDHCPv6ServerID:];
-[CWFBSS setLocation:];
-[CWFBSS mergeWithBSS:];
-[CWFBSS setAWDLRealTimeModeTimestamp:];
-[CWFBSS filteredBSSWithProperties:OSSpecificKeys:];
-[CWFBSS setColocated5GHzRNRChannel:];
-[CWFBSS initWithExternalForm:];
-[CWFBSS encodeWithCoder:];
-[CWFBSS setCoreWiFiSpecificAttributes:];
-[CWFBSS setIPv4NetworkSignature:];
-[CWFBSS setOSSpecificValue:forKey:];
-[CWFBSS hash];
-[CWFBSS deepCopy];
-[CWFBSS AWDLRealTimeModeTimestamp];
-[CWFBSS description];
-[CWFBSS setInternal:];
-[CWFBSS lastAssociatedAt];
-[CWFBSS setIPv6NetworkSignature:];
-[CWFBSS initWithCoder:];
-[CWFBSS initWithInternal:];
-[CWFBSS __coreWiFiSpecificProperties];
-[CWFBSS OSSpecificAttributes];
-[CWFBSS __propertyForKey:];
-[CWFBSS internal];
-[CWFBSS copyWithZone:];
-[CWFBSS setDHCPServerID:];
-[CWFBSS __keyForProperty:];
-[CWFBSS filteredBSSWithProperties:];
-[CWFBSS isEqual:];
-[CWFBSS setColocated2GHzRNRChannel:];
```
