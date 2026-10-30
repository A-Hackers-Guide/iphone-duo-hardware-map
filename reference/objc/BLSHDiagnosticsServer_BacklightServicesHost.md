# `BLSHDiagnosticsServer`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 2 instance methods, 2 class methods

## Instance variables

```
@"<BLSFlipbookDiagnosticsProviding>" _flipbookDiagnosticsProvider;
@"BSServiceConnectionListener" _serviceListener;
@"BSServiceDispatchQueue" _callbackQueue;
```

## Class methods

```
+[BLSHDiagnosticsServer domainSpecification];
+[BLSHDiagnosticsServer serverWithFlipbookDiagnosticsProvider:];
```

## Instance methods

```
-[BLSHDiagnosticsServer _handleIncomingConnection:];
-[BLSHDiagnosticsServer initWithFlipbookDiagnosticsProvider:];
```
