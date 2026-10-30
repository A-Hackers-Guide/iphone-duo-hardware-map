# `BLSHPendingBacklightRamp`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@? _lock_backlightRampBlock;
```

## Properties

```
@property (TB,R,N) hasPendingRamp;
```

## Instance methods

```
-[BLSHPendingBacklightRamp description];
-[BLSHPendingBacklightRamp hasPendingRamp];
-[BLSHPendingBacklightRamp initWithBacklightRampBlock:];
-[BLSHPendingBacklightRamp performBacklightRampIfNeededWithDuration:];
```
