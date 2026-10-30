# `HIDRMUIUserAuthorizationRequest`

- Image: [`/System/Library/PrivateFrameworks/HIDRMUI.framework/HIDRMUI`](../userland/System__Library__PrivateFrameworks__HIDRMUI.framework__HIDRMUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 4 properties, 15 instance methods, 3 class methods

## Instance variables

```
B _requiresPairing;
B _requestedFromSettings;
@"NSString" _deviceName;
```

## Properties

```
@property (TB,N,V_requiresPairing) requiresPairing;
@property (TB,N,V_requestedFromSettings) requestedFromSettings;
@property (T@"NSObject<OS_os_log>",R,N) log;
@property (T@"NSString",C,N,V_deviceName) deviceName;
```

## Class methods

```
+[HIDRMUIUserAuthorizationRequest supportsSecureCoding];
+[HIDRMUIUserAuthorizationRequest requestWithDeviceName:requiresPairing:];
+[HIDRMUIUserAuthorizationRequest requestWithDeviceName:requiresPairing:requestedFromSettings:];
```

## Instance methods

```
-[HIDRMUIUserAuthorizationRequest setDeviceName:];
-[HIDRMUIUserAuthorizationRequest encodeWithCoder:];
-[HIDRMUIUserAuthorizationRequest hash];
-[HIDRMUIUserAuthorizationRequest description];
-[HIDRMUIUserAuthorizationRequest initWithCoder:];
-[HIDRMUIUserAuthorizationRequest log];
-[HIDRMUIUserAuthorizationRequest copyWithZone:];
-[HIDRMUIUserAuthorizationRequest isEqual:];
-[HIDRMUIUserAuthorizationRequest deviceName];
-[HIDRMUIUserAuthorizationRequest initWithDeviceName:requiresPairing:];
-[HIDRMUIUserAuthorizationRequest requiresPairing];
-[HIDRMUIUserAuthorizationRequest initWithDeviceName:requiresPairing:requestedFromSettings:];
-[HIDRMUIUserAuthorizationRequest requestedFromSettings];
-[HIDRMUIUserAuthorizationRequest setRequestedFromSettings:];
-[HIDRMUIUserAuthorizationRequest setRequiresPairing:];
```
