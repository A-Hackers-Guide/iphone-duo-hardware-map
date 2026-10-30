# `BLSHSceneRegistrationStore`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableDictionary" _lock_sceneLookup;
```

## Class methods

```
+[BLSHSceneRegistrationStore sharedInstance];
```

## Instance methods

```
-[BLSHSceneRegistrationStore init];
-[BLSHSceneRegistrationStore registerScene:];
-[BLSHSceneRegistrationStore unregisterScene:];
-[BLSHSceneRegistrationStore sceneForIdentityToken:];
```
