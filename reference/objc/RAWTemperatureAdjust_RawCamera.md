# `RAWTemperatureAdjust`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 5 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"CIImage" inputImage;
@"CIVector" inputWhitePoint;
@"NSNumber" inputExposure;
@"NSNumber" inputVersion;
@"CIVector" defaultWhitePoint;
```

## Class methods

```
+[RAWTemperatureAdjust customAttributes];
+[RAWTemperatureAdjust automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[RAWTemperatureAdjust customAttributes];
-[RAWTemperatureAdjust outputImage];
-[RAWTemperatureAdjust setInputExposure:];
-[RAWTemperatureAdjust outputMatrix];
-[RAWTemperatureAdjust setInputWhitePoint:];
```
