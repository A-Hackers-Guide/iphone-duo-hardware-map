# `CtrMeshDiagUnreliableNodeInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 13 properties, 16 instance methods, 1 class methods

## Instance variables

```
C _routerId;
B _isThisDevice;
B _isThisDeviceParent;
B _isLeader;
B _isBorderRouter;
S _rloc16;
S _version;
S _reasonFlags;
S _userActionFlags;
@"NSData" _extAddress;
@"NSString" _vendorName;
@"NSString" _vendorModel;
@"NSArray" _ipv6Addresses;
```

## Properties

```
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TS,R,V_version) version;
@property (TS,R,V_reasonFlags) reasonFlags;
@property (TS,R,V_userActionFlags) userActionFlags;
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
```

## Class methods

```
+[CtrMeshDiagUnreliableNodeInfo supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagUnreliableNodeInfo vendorName];
-[CtrMeshDiagUnreliableNodeInfo reasonFlags];
-[CtrMeshDiagUnreliableNodeInfo version];
-[CtrMeshDiagUnreliableNodeInfo ipv6Addresses];
-[CtrMeshDiagUnreliableNodeInfo encodeWithCoder:];
-[CtrMeshDiagUnreliableNodeInfo initWithCoder:];
-[CtrMeshDiagUnreliableNodeInfo isThisDevice];
-[CtrMeshDiagUnreliableNodeInfo isLeader];
-[CtrMeshDiagUnreliableNodeInfo extAddress];
-[CtrMeshDiagUnreliableNodeInfo rloc16];
-[CtrMeshDiagUnreliableNodeInfo routerId];
-[CtrMeshDiagUnreliableNodeInfo userActionFlags];
-[CtrMeshDiagUnreliableNodeInfo initWithExtAddress:rloc16:routerId:version:reasonFlags:userActionFlags:isThisDevice:isThisDeviceParent:isLeader:isBorderRouter:vendorName:vendorModel:ipv6Addresses:];
-[CtrMeshDiagUnreliableNodeInfo isBorderRouter];
-[CtrMeshDiagUnreliableNodeInfo isThisDeviceParent];
-[CtrMeshDiagUnreliableNodeInfo vendorModel];
```
