# `AVExposureBiasRange`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
f _minExposureBias;
f _maxExposureBias;
```

## Properties

```
@property (Tf,R,N,V_minExposureBias) minExposureBias;
@property (Tf,R,N,V_maxExposureBias) maxExposureBias;
```

## Class methods

```
+[AVExposureBiasRange exposureBiasRangeWithMinExposureBias:maxExposureBias:];
```

## Instance methods

```
-[AVExposureBiasRange description];
-[AVExposureBiasRange maxExposureBias];
-[AVExposureBiasRange minExposureBias];
-[AVExposureBiasRange containsExposureBias:];
-[AVExposureBiasRange initWithMinExposureBias:maxExposureBias:];
```
