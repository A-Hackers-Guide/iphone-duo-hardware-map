# `_ANEMutableWeightsMapping`

- Image: [`/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`](../userland/System__Library__PrivateFrameworks__ParavirtualizedANE.framework__ParavirtualizedANE.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"_ANEIOSurfaceObject" _guestIOSurface;
^v _hwBuffer;
Q _hwSize;
```

## Properties

```
@property (T@"_ANEIOSurfaceObject",&,N,V_guestIOSurface) guestIOSurface;
@property (T^v,N,V_hwBuffer) hwBuffer;
@property (TQ,N,V_hwSize) hwSize;
```

## Class methods

```
+[_ANEMutableWeightsMapping mappingWithGuestIOSurface:hwBuffer:hwSize:];
```

## Instance methods

```
-[_ANEMutableWeightsMapping hwSize];
-[_ANEMutableWeightsMapping setHwSize:];
-[_ANEMutableWeightsMapping guestIOSurface];
-[_ANEMutableWeightsMapping hwBuffer];
-[_ANEMutableWeightsMapping setGuestIOSurface:];
-[_ANEMutableWeightsMapping setHwBuffer:];
```
