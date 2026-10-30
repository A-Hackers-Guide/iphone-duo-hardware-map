# `CTMobileEquipmentInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 19 instance variables, 19 properties, 43 instance methods, 1 class methods

## Instance variables

```
q _slotId;
@"NSString" _currentMobileId;
@"NSString" _currentSubscriberId;
@"NSString" _IMEI;
@"NSString" _ICCID;
@"NSString" _IMSI;
@"NSString" _cdmaIMSI;
@"NSString" _MEID;
@"NSString" _EUIMID;
@"NSNumber" _PRLVersion;
@"NSNumber" _ERIVersion;
@"NSString" _MIN;
@"NSString" _NAI;
@"NSString" _baseVersion;
@"NSString" _baseId;
@"NSString" _baseProfile;
@"NSString" _effectiveICCID;
@"NSString" _CSN;
@"NSString" _displayCSN;
```

## Properties

```
@property (Tq,N,V_slotId) slotId;
@property (T@"NSString",&,N,V_currentMobileId) currentMobileId;
@property (T@"NSString",&,N,V_currentSubscriberId) currentSubscriberId;
@property (T@"NSString",&,N,V_IMEI) IMEI;
@property (T@"NSString",&,N,V_ICCID) ICCID;
@property (T@"NSString",&,N,V_IMSI) IMSI;
@property (T@"NSString",&,N,V_cdmaIMSI) cdmaIMSI;
@property (T@"NSString",&,N,V_MEID) MEID;
@property (T@"NSString",&,N,V_EUIMID) EUIMID;
@property (T@"NSNumber",&,N,V_PRLVersion) PRLVersion;
@property (T@"NSNumber",&,N,V_ERIVersion) ERIVersion;
@property (T@"NSString",&,N,V_MIN) MIN;
@property (T@"NSString",&,N,V_NAI) NAI;
@property (T@"NSString",&,N,V_baseVersion) baseVersion;
@property (T@"NSString",&,N,V_baseId) baseId;
@property (T@"NSString",&,N,V_baseProfile) baseProfile;
@property (T@"NSString",&,N,V_effectiveICCID) effectiveICCID;
@property (T@"NSString",&,N,V_CSN) CSN;
@property (T@"NSString",&,N,V_displayCSN) displayCSN;
```

## Class methods

```
+[CTMobileEquipmentInfo supportsSecureCoding];
```

## Instance methods

```
-[CTMobileEquipmentInfo NAI];
-[CTMobileEquipmentInfo IMEI];
-[CTMobileEquipmentInfo setCSN:];
-[CTMobileEquipmentInfo setIMEI:];
-[CTMobileEquipmentInfo setEffectiveICCID:];
-[CTMobileEquipmentInfo CSN];
-[CTMobileEquipmentInfo baseProfile];
-[CTMobileEquipmentInfo setEUIMID:];
-[CTMobileEquipmentInfo MEID];
-[CTMobileEquipmentInfo setBaseVersion:];
-[CTMobileEquipmentInfo setDisplayCSN:];
-[CTMobileEquipmentInfo setCdmaIMSI:];
-[CTMobileEquipmentInfo MIN];
-[CTMobileEquipmentInfo setCurrentSubscriberId:];
-[CTMobileEquipmentInfo setIMSI:];
-[CTMobileEquipmentInfo baseVersion];
-[CTMobileEquipmentInfo setBaseId:];
-[CTMobileEquipmentInfo PRLVersion];
-[CTMobileEquipmentInfo IMSI];
-[CTMobileEquipmentInfo setICCID:];
-[CTMobileEquipmentInfo setERIVersion:];
-[CTMobileEquipmentInfo setMIN:];
-[CTMobileEquipmentInfo encodeWithCoder:];
-[CTMobileEquipmentInfo setMEID:];
-[CTMobileEquipmentInfo setCurrentMobileId:];
-[CTMobileEquipmentInfo baseId];
-[CTMobileEquipmentInfo cdmaIMSI];
-[CTMobileEquipmentInfo effectiveICCID];
-[CTMobileEquipmentInfo description];
-[CTMobileEquipmentInfo currentSubscriberId];
-[CTMobileEquipmentInfo initWithCoder:];
-[CTMobileEquipmentInfo ICCID];
-[CTMobileEquipmentInfo setNAI:];
-[CTMobileEquipmentInfo setBaseProfile:];
-[CTMobileEquipmentInfo ERIVersion];
-[CTMobileEquipmentInfo setSlotId:];
-[CTMobileEquipmentInfo slotId];
-[CTMobileEquipmentInfo copyWithZone:];
-[CTMobileEquipmentInfo isEqual:];
-[CTMobileEquipmentInfo EUIMID];
-[CTMobileEquipmentInfo setPRLVersion:];
-[CTMobileEquipmentInfo displayCSN];
-[CTMobileEquipmentInfo currentMobileId];
```
