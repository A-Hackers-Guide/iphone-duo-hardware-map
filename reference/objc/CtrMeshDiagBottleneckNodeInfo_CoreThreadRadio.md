# `CtrMeshDiagBottleneckNodeInfo`

- Image: [`/System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio`](../userland/System__Library__PrivateFrameworks__CoreThreadRadio.framework__CoreThreadRadio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 12 properties, 15 instance methods, 1 class methods

## Instance variables

```
C _routerId;
B _isThisDevice;
B _isThisDeviceParent;
B _isLeader;
B _isBorderRouter;
S _rloc16;
S _version;
I _trafficThroughput;
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
@property (TB,R,V_isThisDevice) isThisDevice;
@property (TB,R,V_isThisDeviceParent) isThisDeviceParent;
@property (TB,R,V_isLeader) isLeader;
@property (TB,R,V_isBorderRouter) isBorderRouter;
@property (TI,R,V_trafficThroughput) trafficThroughput;
@property (T@"NSString",R,V_vendorName) vendorName;
@property (T@"NSString",R,V_vendorModel) vendorModel;
@property (T@"NSArray",R,V_ipv6Addresses) ipv6Addresses;
```

## Class methods

```
+[CtrMeshDiagBottleneckNodeInfo supportsSecureCoding];
```

## Instance methods

```
-[CtrMeshDiagBottleneckNodeInfo vendorName];
-[CtrMeshDiagBottleneckNodeInfo version];
-[CtrMeshDiagBottleneckNodeInfo ipv6Addresses];
-[CtrMeshDiagBottleneckNodeInfo encodeWithCoder:];
-[CtrMeshDiagBottleneckNodeInfo initWithCoder:];
-[CtrMeshDiagBottleneckNodeInfo isThisDevice];
-[CtrMeshDiagBottleneckNodeInfo isLeader];
-[CtrMeshDiagBottleneckNodeInfo extAddress];
-[CtrMeshDiagBottleneckNodeInfo rloc16];
-[CtrMeshDiagBottleneckNodeInfo routerId];
-[CtrMeshDiagBottleneckNodeInfo initWithExtAddress:rloc16:routerId:version:isThisDevice:isThisDeviceParent:isLeader:isBorderRouter:trafficThroughput:vendorName:vendorModel:ipv6Addresses:];
-[CtrMeshDiagBottleneckNodeInfo isBorderRouter];
-[CtrMeshDiagBottleneckNodeInfo isThisDeviceParent];
-[CtrMeshDiagBottleneckNodeInfo trafficThroughput];
-[CtrMeshDiagBottleneckNodeInfo vendorModel];
```
