# `ACCiAP2ShimServerUnregisteredClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`](../userland/System__Library__PrivateFrameworks__AccessoryiAP2Shim.framework__AccessoryiAP2Shim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
i _processId;
@"NSString" _bundleId;
^{SBSProcessAssertion=} _processAssertion;
q _processAssertionStartTime;
```

## Properties

```
@property (T^{SBSProcessAssertion=},R,N,V_processAssertion) processAssertion;
@property (Tq,R,N,V_processAssertionStartTime) processAssertionStartTime;
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (Ti,R,N,V_processId) processId;
```

## Instance methods

```
-[ACCiAP2ShimServerUnregisteredClient processId];
-[ACCiAP2ShimServerUnregisteredClient bundleId];
-[ACCiAP2ShimServerUnregisteredClient initWithBundleId:];
-[ACCiAP2ShimServerUnregisteredClient releaseProcessAssertion];
-[ACCiAP2ShimServerUnregisteredClient processAssertion];
-[ACCiAP2ShimServerUnregisteredClient _applicationInfoForBundleIDSync:];
-[ACCiAP2ShimServerUnregisteredClient _getProcessId];
-[ACCiAP2ShimServerUnregisteredClient processAssertionStartTime];
-[ACCiAP2ShimServerUnregisteredClient takeProcessAssertion:];
```
