# `ACCiAP2ShimServerClient`

- Image: [`/System/Library/PrivateFrameworks/AccessoryiAP2Shim.framework/AccessoryiAP2Shim`](../userland/System__Library__PrivateFrameworks__AccessoryiAP2Shim.framework__AccessoryiAP2Shim.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _locationSupportedByClient;
B _cameraSupportedByClient;
B _supportsAccessibility;
B _clientRequiresAccReset;
B _interestedInBLENotifications;
B _entitlementForAllAccessories;
i _processId;
I _clientID;
I _capabilities;
i _iapSessionRefCount;
I _applicationState;
@"NSObject<OS_xpc_object>" _xpcConnection;
@"NSString" _bundleId;
@"NSArray" _clientEAProtocols;
@"NSObject<OS_dispatch_queue>" _processAssertionQ;
^{SBSProcessAssertion=} _processAssertion;
q _processAssertionStartTime;
@"NSObject<OS_dispatch_source>" _processAssertionTimer;
{?="val"[8I]} _auditToken;
```

## Properties

```
@property (TB,R,N,V_entitlementForAllAccessories) entitlementForAllAccessories;
@property (T@"NSArray",R,N,V_clientEAProtocols) clientEAProtocols;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_processAssertionQ) processAssertionQ;
@property (T^{SBSProcessAssertion=},R,N,V_processAssertion) processAssertion;
@property (Tq,R,N,V_processAssertionStartTime) processAssertionStartTime;
@property (T@"NSObject<OS_dispatch_source>",R,N,V_processAssertionTimer) processAssertionTimer;
@property (Ti,R,N,V_iapSessionRefCount) iapSessionRefCount;
@property (TI,N,V_applicationState) applicationState;
@property (TI,N,V_clientID) clientID;
@property (Ti,R,N,V_processId) processId;
@property (T@"NSObject<OS_xpc_object>",R,N,V_xpcConnection) xpcConnection;
@property (T@"NSString",R,N,V_bundleId) bundleId;
@property (T{?=[8I]},R,N,V_auditToken) auditToken;
@property (TI,R,N,V_capabilities) capabilities;
@property (TB,N,V_locationSupportedByClient) locationSupportedByClient;
@property (TB,N,V_cameraSupportedByClient) cameraSupportedByClient;
@property (TB,R,N,V_supportsAccessibility) supportsAccessibility;
@property (TB,N,V_clientRequiresAccReset) clientRequiresAccReset;
@property (TB,N,V_interestedInBLENotifications) interestedInBLENotifications;
```

## Instance methods

```
-[ACCiAP2ShimServerClient clientID];
-[ACCiAP2ShimServerClient setClientID:];
-[ACCiAP2ShimServerClient applicationState];
-[ACCiAP2ShimServerClient processId];
-[ACCiAP2ShimServerClient dealloc];
-[ACCiAP2ShimServerClient setApplicationState:];
-[ACCiAP2ShimServerClient xpcConnection];
-[ACCiAP2ShimServerClient bundleId];
-[ACCiAP2ShimServerClient releaseProcessAssertion];
-[ACCiAP2ShimServerClient capabilities];
-[ACCiAP2ShimServerClient description];
-[ACCiAP2ShimServerClient auditToken];
-[ACCiAP2ShimServerClient processAssertion];
-[ACCiAP2ShimServerClient supportsAccessibility];
-[ACCiAP2ShimServerClient processAssertionTimer];
-[ACCiAP2ShimServerClient hasEntitlementForAllAccessories];
-[ACCiAP2ShimServerClient _applicationInfoForBundleIDSync:];
-[ACCiAP2ShimServerClient cameraSupportedByClient];
-[ACCiAP2ShimServerClient canSendConnectionEventForAccessory:];
-[ACCiAP2ShimServerClient clientEAProtocols];
-[ACCiAP2ShimServerClient clientRequiresAccReset];
-[ACCiAP2ShimServerClient entitlementForAllAccessories];
-[ACCiAP2ShimServerClient iapSessionRefCount];
-[ACCiAP2ShimServerClient initWithCapabilities:auditToken:xpcConnection:eaProtocols:andBundleId:];
-[ACCiAP2ShimServerClient interestedInBLENotifications];
-[ACCiAP2ShimServerClient locationSupportedByClient];
-[ACCiAP2ShimServerClient processAssertionQ];
-[ACCiAP2ShimServerClient processAssertionStartTime];
-[ACCiAP2ShimServerClient setCameraSupportedByClient:];
-[ACCiAP2ShimServerClient setClientRequiresAccReset:];
-[ACCiAP2ShimServerClient setInterestedInBLENotifications:];
-[ACCiAP2ShimServerClient setLocationSupportedByClient:];
-[ACCiAP2ShimServerClient takeProcessAssertion:];
```
