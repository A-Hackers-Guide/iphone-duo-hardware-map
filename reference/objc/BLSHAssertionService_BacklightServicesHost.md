# `BLSHAssertionService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 2 instance methods, 1 class methods

## Instance variables

```
@"BLSHXPCAssertionServiceHostServer" _server;
@"BLSHLocalAssertionService" _localAssertionService;
```

## Properties

```
@property (T@"BLSHLocalAssertionService",R,N,V_localAssertionService) localAssertionService;
```

## Class methods

```
+[BLSHAssertionService serviceWithOSInterfaceProvider:localOnly:];
```

## Instance methods

```
-[BLSHAssertionService localAssertionService];
-[BLSHAssertionService initWithOSInterfaceProvider:localOnly:];
```
