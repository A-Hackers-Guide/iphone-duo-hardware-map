# `CtrMeshDiagCriticalNodeInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 15 properties, 18 instance methods, 1 class methods

## Instance variables

```
C _routerId;
B _isThisDevice;
B _isThisDeviceParent;
B _isLeader;
B _isBorderRouter;
B _hasEnhancedRoute;
B _hasVendorRoute;
B _hasOffgridRoute;
S _rloc16;
S _version;
@"NSData" _extAddress;
@"NSString" _vendorName;
@"NSString" _vendorModel;
@"NSData" _linkQualities;
@"NSArray" _ipv6Addresses;
```

## Properties

```
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (TB,R,V_hasEnhancedRoute) hasEnhancedRoute;
@property (TB,R,V_hasVendorRoute) hasVendorRoute;
@property (TB,R,V_hasOffgridRoute) hasOffgridRoute;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSData",R,V_linkQualities) linkQualities;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
```

## Class methods

```
+[CtrMeshDiagCriticalNodeInfo supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagCriticalNodeInfo vendorName];
-[CtrMeshDiagCriticalNodeInfo version];
-[CtrMeshDiagCriticalNodeInfo ipv6Addresses];
-[CtrMeshDiagCriticalNodeInfo encodeWithCoder:];
-[CtrMeshDiagCriticalNodeInfo initWithCoder:];
-[CtrMeshDiagCriticalNodeInfo isThisDevice];
-[CtrMeshDiagCriticalNodeInfo isLeader];
-[CtrMeshDiagCriticalNodeInfo extAddress];
-[CtrMeshDiagCriticalNodeInfo rloc16];
-[CtrMeshDiagCriticalNodeInfo routerId];
-[CtrMeshDiagCriticalNodeInfo hasOffgridRoute];
-[CtrMeshDiagCriticalNodeInfo hasEnhancedRoute];
-[CtrMeshDiagCriticalNodeInfo hasVendorRoute];
-[CtrMeshDiagCriticalNodeInfo initWithExtAddress:rloc16:routerId:version:isThisDevice:isThisDeviceParent:isLeader:isBorderRouter:hasEnhancedRoute:hasVendorRoute:hasOffgridRoute:vendorName:vendorModel:linkQualities:ipv6Addresses:];
-[CtrMeshDiagCriticalNodeInfo isBorderRouter];
-[CtrMeshDiagCriticalNodeInfo isThisDeviceParent];
-[CtrMeshDiagCriticalNodeInfo linkQualities];
-[CtrMeshDiagCriticalNodeInfo vendorModel];
```
