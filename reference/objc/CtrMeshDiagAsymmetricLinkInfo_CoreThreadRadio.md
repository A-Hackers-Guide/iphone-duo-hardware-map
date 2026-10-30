# `CtrMeshDiagAsymmetricLinkInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 15 instance variables, 15 properties, 19 instance methods, 1 class methods

## Instance variables

```
C _nodeARouterId;
C _nodeBRouterId;
C _forwardLinkCost;
C _reverseLinkCost;
C _costDifference;
S _nodeARloc16;
S _nodeBRloc16;
@"NSData" _nodeAExtAddress;
@"NSString" _nodeAVendorName;
@"NSString" _nodeAVendorModel;
@"NSData" _nodeBExtAddress;
@"NSString" _nodeBVendorName;
@"NSString" _nodeBVendorModel;
@"NSArray" _nodeAIpv6Addresses;
@"NSArray" _nodeBIpv6Addresses;
```

## Properties

```
@property (T@"NSData",R,V_nodeAExtAddress) nodeAExtAddress;
@property (TS,R,V_nodeARloc16) nodeARloc16;
@property (TC,R,V_nodeARouterId) nodeARouterId;
@property (T@"NSString",R,V_nodeAVendorName) nodeAVendorName;
@property (T@"NSString",R,V_nodeAVendorModel) nodeAVendorModel;
@property (T@"NSData",R,V_nodeBExtAddress) nodeBExtAddress;
@property (TS,R,V_nodeBRloc16) nodeBRloc16;
@property (TC,R,V_nodeBRouterId) nodeBRouterId;
@property (T@"NSString",R,V_nodeBVendorName) nodeBVendorName;
@property (T@"NSString",R,V_nodeBVendorModel) nodeBVendorModel;
@property (TC,R,V_forwardLinkCost) forwardLinkCost;
@property (TC,R,V_reverseLinkCost) reverseLinkCost;
@property (TC,R,V_costDifference) costDifference;
@property (T@"NSArray",R,V_nodeAIpv6Addresses) nodeAIpv6Addresses;
@property (T@"NSArray",R,V_nodeBIpv6Addresses) nodeBIpv6Addresses;
```

## Class methods

```
+[CtrMeshDiagAsymmetricLinkInfo supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagAsymmetricLinkInfo encodeWithCoder:];
-[CtrMeshDiagAsymmetricLinkInfo initWithCoder:];
-[CtrMeshDiagAsymmetricLinkInfo forwardLinkCost];
-[CtrMeshDiagAsymmetricLinkInfo nodeAExtAddress];
-[CtrMeshDiagAsymmetricLinkInfo nodeBExtAddress];
-[CtrMeshDiagAsymmetricLinkInfo reverseLinkCost];
-[CtrMeshDiagAsymmetricLinkInfo nodeAVendorName];
-[CtrMeshDiagAsymmetricLinkInfo nodeBVendorName];
-[CtrMeshDiagAsymmetricLinkInfo costDifference];
-[CtrMeshDiagAsymmetricLinkInfo initWithNodeAExtAddress:nodeARloc16:nodeARouterId:nodeAVendorName:nodeAVendorModel:nodeBExtAddress:nodeBRloc16:nodeBRouterId:nodeBVendorName:nodeBVendorModel:forwardLinkCost:reverseLinkCost:costDifference:nodeAIpv6Addresses:nodeBIpv6Addresses:];
-[CtrMeshDiagAsymmetricLinkInfo initWithNodeAExtAddress:peerExtAddress:localRloc16:peerRloc16:localRouterId:peerRouterId:localLinkQuality:peerLinkQuality:localRssi:peerRssi:];
-[CtrMeshDiagAsymmetricLinkInfo nodeAIpv6Addresses];
-[CtrMeshDiagAsymmetricLinkInfo nodeARloc16];
-[CtrMeshDiagAsymmetricLinkInfo nodeARouterId];
-[CtrMeshDiagAsymmetricLinkInfo nodeAVendorModel];
-[CtrMeshDiagAsymmetricLinkInfo nodeBIpv6Addresses];
-[CtrMeshDiagAsymmetricLinkInfo nodeBRloc16];
-[CtrMeshDiagAsymmetricLinkInfo nodeBRouterId];
-[CtrMeshDiagAsymmetricLinkInfo nodeBVendorModel];
```
