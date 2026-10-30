# `CWFRNRBSS`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CWFJSONEncodable`, `NSCopying`, `NSSecureCoding`
- 11 instance variables, 15 properties, 30 instance methods, 1 class methods

## Instance variables

```
B _UPRActive;
B _sameSSID;
B _multipleBSSID;
B _transmittedBSSID;
B _multiband6GHz;
B _colocatedAP;
Q _shortSSID;
@"NSString" _BSSID;
@"CWFChannel" _channel;
Q _TBTTOffset;
Q _primary20MHzPSD;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,N,V_shortSSID) shortSSID;
@property (T@"NSString",C,N,V_BSSID) BSSID;
@property (T@"CWFChannel",C,N,V_channel) channel;
@property (TB,N,GisUPRActive,V_UPRActive) UPRActive;
@property (TB,N,GisSameSSID,V_sameSSID) sameSSID;
@property (TB,N,GisMultipleBSSID,V_multipleBSSID) multipleBSSID;
@property (TB,N,GisTransmittedBSSID,V_transmittedBSSID) transmittedBSSID;
@property (TB,N,GisMultiband6GHz,V_multiband6GHz) multiband6GHz;
@property (TB,N,GisColocatedAP,V_colocatedAP) colocatedAP;
@property (TQ,N,V_TBTTOffset) TBTTOffset;
@property (TQ,N,V_primary20MHzPSD) primary20MHzPSD;
```

## Class methods

```
+[CWFRNRBSS supportsSecureCoding];
```

## Instance methods

```
-[CWFRNRBSS setChannel:];
-[CWFRNRBSS channel];
-[CWFRNRBSS BSSID];
-[CWFRNRBSS JSONCompatibleKeyValueMap];
-[CWFRNRBSS setShortSSID:];
-[CWFRNRBSS setBSSID:];
-[CWFRNRBSS shortSSID];
-[CWFRNRBSS encodeWithCoder:];
-[CWFRNRBSS hash];
-[CWFRNRBSS description];
-[CWFRNRBSS initWithCoder:];
-[CWFRNRBSS copyWithZone:];
-[CWFRNRBSS isEqual:];
-[CWFRNRBSS isMultiband6GHz];
-[CWFRNRBSS setColocatedAP:];
-[CWFRNRBSS isMultipleBSSID];
-[CWFRNRBSS primary20MHzPSD];
-[CWFRNRBSS TBTTOffset];
-[CWFRNRBSS isColocatedAP];
-[CWFRNRBSS isEqualToRNRBSS:];
-[CWFRNRBSS isSameSSID];
-[CWFRNRBSS isTransmittedBSSID];
-[CWFRNRBSS isUPRActive];
-[CWFRNRBSS setMultiband6GHz:];
-[CWFRNRBSS setMultipleBSSID:];
-[CWFRNRBSS setPrimary20MHzPSD:];
-[CWFRNRBSS setSameSSID:];
-[CWFRNRBSS setTBTTOffset:];
-[CWFRNRBSS setTransmittedBSSID:];
-[CWFRNRBSS setUPRActive:];
```
