# `BWAmbientLightSensor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _hidSystemClient;
@"NSObject<OS_dispatch_queue>" _alsQueue;
i _luxLevel;
f _rearLuxLevel;
@"BrightnessSystemClient" _brightnessSystemClient;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _numberOfAmbientLightUpdates;
```

## Properties

```
@property (Ti,R,N) luxLevel;
@property (Tf,R,N) rearLuxLevel;
```

## Class methods

```
+[BWAmbientLightSensor initialize];
```

## Instance methods

```
-[BWAmbientLightSensor init];
-[BWAmbientLightSensor dealloc];
-[BWAmbientLightSensor luxLevel];
-[BWAmbientLightSensor forceUpdateRearLuxLevel];
-[BWAmbientLightSensor rearLuxLevel];
```
