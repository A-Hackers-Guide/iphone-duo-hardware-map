# `BLSHLocalOnlyServiceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 2 class methods

## Instance variables

```
f _dimmedFactor;
d _fadeInDuration;
d _fadeOutDuration;
d _dimmingDuration;
```

## Properties

```
@property (Td,R,N,V_fadeInDuration) fadeInDuration;
@property (Td,R,N,V_fadeOutDuration) fadeOutDuration;
@property (Td,R,N,V_dimmingDuration) dimmingDuration;
@property (Tf,R,N,V_dimmedFactor) dimmedFactor;
```

## Class methods

```
+[BLSHLocalOnlyServiceConfiguration configurationWithFadeInDuration:fadeOutDuration:];
+[BLSHLocalOnlyServiceConfiguration configurationWithFadeInDuration:fadeOutDuration:dimmingDuration:dimmedFactor:];
```

## Instance methods

```
-[BLSHLocalOnlyServiceConfiguration init];
-[BLSHLocalOnlyServiceConfiguration fadeOutDuration];
-[BLSHLocalOnlyServiceConfiguration fadeInDuration];
-[BLSHLocalOnlyServiceConfiguration dimmingDuration];
-[BLSHLocalOnlyServiceConfiguration dimmedFactor];
-[BLSHLocalOnlyServiceConfiguration initWithFadeInDuration:fadeOutDuration:dimmingDuration:dimmedFactor:];
```
