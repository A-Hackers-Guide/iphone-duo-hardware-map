# `CtrMeshDiagUnreachableNodeInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 10 instance methods, 1 class methods

## Instance variables

```
C _routerId;
B _extAddressKnown;
S _rloc16;
@"NSData" _extAddress;
@"NSString" _vendorName;
@"NSString" _vendorModel;
```

## Properties

```
@property (T@"NSData",R,V_extAddress) extAddress;
@property (TS,R,V_rloc16) rloc16;
@property (TC,R,V_routerId) routerId;
@property (TB,R,V_extAddressKnown) extAddressKnown;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
```

## Class methods

```
+[CtrMeshDiagUnreachableNodeInfo supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagUnreachableNodeInfo vendorName];
-[CtrMeshDiagUnreachableNodeInfo encodeWithCoder:];
-[CtrMeshDiagUnreachableNodeInfo initWithCoder:];
-[CtrMeshDiagUnreachableNodeInfo extAddress];
-[CtrMeshDiagUnreachableNodeInfo rloc16];
-[CtrMeshDiagUnreachableNodeInfo routerId];
-[CtrMeshDiagUnreachableNodeInfo extAddressKnown];
-[CtrMeshDiagUnreachableNodeInfo initWithExtAddress:rloc16:routerId:extAddressKnown:vendorName:vendorModel:];
-[CtrMeshDiagUnreachableNodeInfo initWithExtAddress:rloc16:routerId:version:isThisDevice:isThisDeviceParent:isLeader:isBorderRouter:vendorName:vendorModel:];
-[CtrMeshDiagUnreachableNodeInfo vendorModel];
```
