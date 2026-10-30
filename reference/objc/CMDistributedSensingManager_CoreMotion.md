# `CMDistributedSensingManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"CMDistributedSensingManagerInternal" _internal;
@"<CMDistributedSensingDelegate>" _delegate;
```

## Properties

```
@property (T@"CMDistributedSensingManagerInternal",R,N,V_internal) _internal;
@property (T@"<CMDistributedSensingDelegate>",N,V_delegate) delegate;
```

## Class methods

```
+[CMDistributedSensingManager isVehicleStateUpdatesAvailable];
```

## Instance methods

```
-[CMDistributedSensingManager _internal];
-[CMDistributedSensingManager init];
-[CMDistributedSensingManager dealloc];
-[CMDistributedSensingManager setDelegate:];
-[CMDistributedSensingManager delegate];
-[CMDistributedSensingManager subscribeToVehicleState];
-[CMDistributedSensingManager unsubscribeToVehicleState];
```
