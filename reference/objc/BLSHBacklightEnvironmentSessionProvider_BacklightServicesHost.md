# `BLSHBacklightEnvironmentSessionProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightEnvironmentSessionProviding`
- 3 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@? _perDisplayFactory;
@"NSDictionary" _lock_providersByDisplayId;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHBacklightEnvironmentSessionProvider providerWithProviderFactory:];
```

## Instance methods

```
-[BLSHBacklightEnvironmentSessionProvider init];
-[BLSHBacklightEnvironmentSessionProvider createInactiveEnvironmentSession];
-[BLSHBacklightEnvironmentSessionProvider createInactiveEnvironmentSessionForDisplay:];
-[BLSHBacklightEnvironmentSessionProvider initWithProviderFactory:];
-[BLSHBacklightEnvironmentSessionProvider providerForDisplay:];
-[BLSHBacklightEnvironmentSessionProvider providersByDisplayId];
```
