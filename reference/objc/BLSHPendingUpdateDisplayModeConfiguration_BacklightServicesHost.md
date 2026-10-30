# `BLSHPendingUpdateDisplayModeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _isAnimatedTransition;
B _isNullOperationAllowed;
@"BLSHPendingUpdateDisplayMode" _pendingOperation;
@"BLSHPendingUpdateDisplayMode" _abandonedInProgressOperation;
```

## Properties

```
@property (T@"BLSHPendingUpdateDisplayMode",&,V_pendingOperation) pendingOperation;
@property (T@"BLSHPendingUpdateDisplayMode",&,V_abandonedInProgressOperation) abandonedInProgressOperation;
@property (TB,V_isAnimatedTransition) isAnimatedTransition;
@property (TB,V_isNullOperationAllowed) isNullOperationAllowed;
```

## Instance methods

```
-[BLSHPendingUpdateDisplayModeConfiguration pendingOperation];
-[BLSHPendingUpdateDisplayModeConfiguration setPendingOperation:];
-[BLSHPendingUpdateDisplayModeConfiguration abandonedInProgressOperation];
-[BLSHPendingUpdateDisplayModeConfiguration isAnimatedTransition];
-[BLSHPendingUpdateDisplayModeConfiguration isNullOperationAllowed];
-[BLSHPendingUpdateDisplayModeConfiguration setAbandonedInProgressOperation:];
-[BLSHPendingUpdateDisplayModeConfiguration setIsAnimatedTransition:];
-[BLSHPendingUpdateDisplayModeConfiguration setIsNullOperationAllowed:];
```
