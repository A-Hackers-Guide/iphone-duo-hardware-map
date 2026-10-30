# `BLSHPreventBacklightIdleAttributeHandler`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHLocalCountingAssertionAttributeHandler`
- 3 instance variables, 1 properties, 8 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
[3B] _active;
@"BLSHBacklightIdleProvider" _provider;
```

## Properties

```
@property (T@"BLSHBacklightIdleProvider",R,W,N,V_provider) provider;
```

## Class methods

```
+[BLSHPreventBacklightIdleAttributeHandler attributeBaseClass];
+[BLSHPreventBacklightIdleAttributeHandler attributeClasses];
+[BLSHPreventBacklightIdleAttributeHandler registerHandlerForService:provider:];
```

## Instance methods

```
-[BLSHPreventBacklightIdleAttributeHandler display];
-[BLSHPreventBacklightIdleAttributeHandler provider];
-[BLSHPreventBacklightIdleAttributeHandler activateWithFirstEntry:];
-[BLSHPreventBacklightIdleAttributeHandler countingTargetForEntry:];
-[BLSHPreventBacklightIdleAttributeHandler deactivateWithFinalEntry:];
-[BLSHPreventBacklightIdleAttributeHandler activate:withEntry:];
-[BLSHPreventBacklightIdleAttributeHandler initForService:provider:];
-[BLSHPreventBacklightIdleAttributeHandler typeForEntry:];
```
