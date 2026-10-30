# `CWFPrivateMACManager`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 20 instance variables, 14 properties, 41 instance methods, 0 class methods

## Instance variables

```
Q _rotationInterval;
@"NSData" _deviceKey;
@"NSData" _rotationKey;
@"NSDate" _rotationKeyUpdatedAt;
@"NSMutableDictionary" _privateMACAddressCache;
@"NSMutableArray" _privateMACAddressCacheIDList;
@"NSMutableDictionary" _userJoinFailureTimestampMap;
@"NSMutableDictionary" _userJoinFailureCountMap;
@"NSMutableDictionary" _tempUserSettingMap;
q _systemSetting;
@"NSString" _interfaceName;
@"NSString" _hardwareMACAddress;
@? _updatedSystemSettingHandler;
@? _updatedDeviceKeyHandler;
@? _updatedNetworkIDHandler;
@? _updatedRotationKeyHandler;
@? _effectiveHardwareMACAddress;
@? _allowRotationHandler;
@? _isNetworkManagedByMDMHandler;
@"NSObject<OS_dispatch_queue>" _targetQueue;
```

## Properties

```
@property (T@"NSString",R,V_interfaceName) interfaceName;
@property (T@"NSString",R,V_hardwareMACAddress) hardwareMACAddress;
@property (T@"NSData",C,D) deviceKey;
@property (Tq,D) systemSetting;
@property (T@?,C,V_updatedSystemSettingHandler) updatedSystemSettingHandler;
@property (T@?,C,V_updatedDeviceKeyHandler) updatedDeviceKeyHandler;
@property (T@"NSData",C,D) rotationKey;
@property (T@"NSDate",C,D) rotationKeyUpdatedAt;
@property (T@?,C,V_updatedNetworkIDHandler) updatedNetworkIDHandler;
@property (T@?,C,V_updatedRotationKeyHandler) updatedRotationKeyHandler;
@property (T@?,C,V_effectiveHardwareMACAddress) effectiveHardwareMACAddress;
@property (T@?,C,V_allowRotationHandler) allowRotationHandler;
@property (T@?,C,V_isNetworkManagedByMDMHandler) isNetworkManagedByMDMHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,V_targetQueue) targetQueue;
```

## Instance methods

```
-[CWFPrivateMACManager hardwareMACAddress];
-[CWFPrivateMACManager privateMACAddressModeForNetworkProfile:];
-[CWFPrivateMACManager setTargetQueue:];
-[CWFPrivateMACManager privateMACAddressForNetworkProfile:];
-[CWFPrivateMACManager targetQueue];
-[CWFPrivateMACManager init];
-[CWFPrivateMACManager interfaceName];
-[CWFPrivateMACManager invalidate];
-[CWFPrivateMACManager deviceKey];
-[CWFPrivateMACManager setRotationKey:];
-[CWFPrivateMACManager setEffectiveHardwareMACAddress:];
-[CWFPrivateMACManager setUpdatedSystemSettingHandler:];
-[CWFPrivateMACManager __calloutToAllowRotation];
-[CWFPrivateMACManager __calloutToCheckIfNetworkIsMDMManaged:];
-[CWFPrivateMACManager __calloutToGetEffectiveHardwareMACAddress];
-[CWFPrivateMACManager allowRotationHandler];
-[CWFPrivateMACManager allowUserJoinFailureUIForNetworkProfile:];
-[CWFPrivateMACManager clearTemporaryUserSettings];
-[CWFPrivateMACManager effectiveHardwareMACAddress];
-[CWFPrivateMACManager initWithInterfaceName:hardwareMACAddress:];
-[CWFPrivateMACManager isNetworkManagedByMDMHandler];
-[CWFPrivateMACManager rotationKey];
-[CWFPrivateMACManager rotationKeyUpdatedAt];
-[CWFPrivateMACManager setAllowRotationHandler:];
-[CWFPrivateMACManager setDeviceKey:];
-[CWFPrivateMACManager setIsNetworkManagedByMDMHandler:];
-[CWFPrivateMACManager setNetworkIDForAssociationWithMACAddress:networkProfile:];
-[CWFPrivateMACManager setRotationKeyUpdatedAt:];
-[CWFPrivateMACManager setSystemSetting:];
-[CWFPrivateMACManager setTemporaryUserSetting:networkProfile:];
-[CWFPrivateMACManager setUpdatedDeviceKeyHandler:];
-[CWFPrivateMACManager setUpdatedNetworkIDHandler:];
-[CWFPrivateMACManager setUpdatedRotationKeyHandler:];
-[CWFPrivateMACManager setUserJoinFailureUIState:networkProfile:];
-[CWFPrivateMACManager submitPrivateMACStatsMetricWithEventType:networkProfile:];
-[CWFPrivateMACManager systemSetting];
-[CWFPrivateMACManager temporaryUserSettingForNetworkProfile:];
-[CWFPrivateMACManager updatedDeviceKeyHandler];
-[CWFPrivateMACManager updatedNetworkIDHandler];
-[CWFPrivateMACManager updatedRotationKeyHandler];
-[CWFPrivateMACManager updatedSystemSettingHandler];
```
