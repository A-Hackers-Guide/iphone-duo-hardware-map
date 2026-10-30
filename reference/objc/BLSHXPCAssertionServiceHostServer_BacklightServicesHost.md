# `BLSHXPCAssertionServiceHostServer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 2 instance methods, 2 class methods

## Instance variables

```
@"<BLSAssertionService>" _localAssertionService;
@"<BLSHBacklightOSInterfaceProviding>" _osInterfaceProvider;
@"BSServiceConnectionListener" _serviceListener;
@"BSServiceDispatchQueue" _callbackQueue;
```

## Class methods

```
+[BLSHXPCAssertionServiceHostServer domainSpecification];
+[BLSHXPCAssertionServiceHostServer serverWithLocalAssertionService:osInterfaceProvider:];
```

## Instance methods

```
-[BLSHXPCAssertionServiceHostServer _handleIncomingConnection:];
-[BLSHXPCAssertionServiceHostServer initWithLocalAssertionService:osInterfaceProvider:];
```
