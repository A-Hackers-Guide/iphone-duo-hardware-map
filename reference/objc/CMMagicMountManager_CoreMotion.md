# `CMMagicMountManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 17 instance methods, 1 class methods

## Instance variables

```
@ _internal;
C _propertyC;
q _lastSentMountStatusToClient;
q _magicMountConfiguration;
```

## Properties

```
@property (T{CMMagicMountStateStruct=dqC},R,N) currentMagicMountState;
@property (Tq,N,V_magicMountConfiguration) magicMountConfiguration;
```

## Class methods

```
+[CMMagicMountManager isAvailable];
```

## Instance methods

```
-[CMMagicMountManager init];
-[CMMagicMountManager initPrivate];
-[CMMagicMountManager dealloc];
-[CMMagicMountManager deallocPrivate];
-[CMMagicMountManager currentMagicMountState];
-[CMMagicMountManager feedMountStatus:apAwake:simulated:timestamp:];
-[CMMagicMountManager magicMountConfiguration];
-[CMMagicMountManager onMagicMountData:];
-[CMMagicMountManager sendMagicMountStateToClientPrivate];
-[CMMagicMountManager setAPWakesAllowed:];
-[CMMagicMountManager setAPWakesAllowedPrivate:];
-[CMMagicMountManager setMagicMountConfiguration:];
-[CMMagicMountManager simulateMagicMountEvent:delay:];
-[CMMagicMountManager startMagicMountUpdatesPrivateToQueue:withHandler:];
-[CMMagicMountManager startMagicMountUpdatesToQueue:withHandler:];
-[CMMagicMountManager stopMagicMountUpdates];
-[CMMagicMountManager stopMagicMountUpdatesPrivate];
```
