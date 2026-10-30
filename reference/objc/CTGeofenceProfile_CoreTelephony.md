# `CTGeofenceProfile`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _cellularDataPreferred;
B _enableNRStandalone;
@"NSString" _dataSetName;
@"NSString" _versionNumber;
@"NSString" _csgNetworkIdentifier;
@"NSString" _networkIdentifier;
@"NSArray" _geofenceList;
q _NRStandaloneMode;
```

## Properties

```
@property (T@"NSString",&,N,V_dataSetName) dataSetName;
@property (T@"NSString",&,N,V_versionNumber) versionNumber;
@property (T@"NSString",&,N,V_csgNetworkIdentifier) csgNetworkIdentifier;
@property (T@"NSString",&,N,V_networkIdentifier) networkIdentifier;
@property (T@"NSArray",&,N,V_geofenceList) geofenceList;
@property (TB,N,V_cellularDataPreferred) cellularDataPreferred;
@property (TB,N,V_enableNRStandalone) enableNRStandalone;
@property (Tq,N,V_NRStandaloneMode) NRStandaloneMode;
```

## Class methods

```
+[CTGeofenceProfile supportsSecureCoding];
```

## Instance methods

```
-[CTGeofenceProfile versionNumber];
-[CTGeofenceProfile encodeWithCoder:];
-[CTGeofenceProfile description];
-[CTGeofenceProfile initWithCoder:];
-[CTGeofenceProfile setVersionNumber:];
-[CTGeofenceProfile setDataSetName:];
-[CTGeofenceProfile cellularDataPreferred];
-[CTGeofenceProfile csgNetworkIdentifier];
-[CTGeofenceProfile dataSetName];
-[CTGeofenceProfile enableNRStandalone];
-[CTGeofenceProfile geofenceList];
-[CTGeofenceProfile networkIdentifier];
-[CTGeofenceProfile setCellularDataPreferred:];
-[CTGeofenceProfile setCsgNetworkIdentifier:];
-[CTGeofenceProfile setEnableNRStandalone:];
-[CTGeofenceProfile setGeofenceList:];
-[CTGeofenceProfile setNetworkIdentifier:];
-[CTGeofenceProfile NRStandaloneMode];
-[CTGeofenceProfile setNRStandaloneMode:];
```
