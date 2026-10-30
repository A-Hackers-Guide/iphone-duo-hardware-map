# `CAFASCTree`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 26 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _accessories;
@"NSString" _routeSharingUserVisibleReason;
@"NSString" _routeSharingUserVisibleBrand;
@"NSDictionary" _nightModeByDisplayID;
@"NSMutableSet" _missingRegistrations;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V_missingRegistrations) missingRegistrations;
@property (T@"NSDictionary",R,N,V_accessories) accessories;
@property (T@"NSString",R,N,V_routeSharingUserVisibleReason) routeSharingUserVisibleReason;
@property (T@"NSString",R,N,V_routeSharingUserVisibleBrand) routeSharingUserVisibleBrand;
@property (T@"NSDictionary",R,N,V_nightModeByDisplayID) nightModeByDisplayID;
```

## Class methods

```
+[CAFASCTree supportsSecureCoding];
+[CAFASCTree _nodesOfType:fromDict:];
```

## Instance methods

```
-[CAFASCTree initEmpty];
-[CAFASCTree initWithDictionary:];
-[CAFASCTree initWithContentsOfFile:];
-[CAFASCTree accessories];
-[CAFASCTree encodeWithCoder:];
-[CAFASCTree initWithCoder:];
-[CAFASCTree hasAccessoryWithClass:serviceWithClass:characteristicWithClass:];
-[CAFASCTree validateRegisteredForAccessory:];
-[CAFASCTree _hasAccessory:service:characteristicOrControl:];
-[CAFASCTree hasAccessory:];
-[CAFASCTree hasAccessory:service:];
-[CAFASCTree hasAccessory:service:characteristic:];
-[CAFASCTree hasAccessory:service:control:];
-[CAFASCTree hasAccessoryWithClass:];
-[CAFASCTree hasAccessoryWithClass:serviceWithClass:];
-[CAFASCTree initWithCarSessionConfiguration:];
-[CAFASCTree logErrorIfNeededForMissingRegistration:];
-[CAFASCTree missingRegistrations];
-[CAFASCTree nightModeByDisplayID];
-[CAFASCTree nodeForAccessory:serviceType:];
-[CAFASCTree routeSharingUserVisibleBrand];
-[CAFASCTree routeSharingUserVisibleReason];
-[CAFASCTree treeLogLines];
-[CAFASCTree validateRegisteredForAccessory:service:];
-[CAFASCTree validateRegisteredForAccessory:service:characteristic:];
-[CAFASCTree validateRegisteredForAccessory:service:control:];
```
