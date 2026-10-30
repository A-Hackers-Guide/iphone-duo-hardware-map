# `RAWGainMap`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 11 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"CIImage" inputImage;
@"NSData" inputGainMapData;
@"CIVector" inputGainMapApplyRegion;
@"CIVector" inputGainMapRegion;
@"CIVector" inputGainMapSize;
@"NSNumber" inputGainMapRowPitch;
@"NSNumber" inputGainMapColPitch;
@"NSNumber" inputGainMapNumPlanes;
@"NSNumber" inputGainMapExecute;
@ inputColorSpace;
@"CIImage" _gainMapImg;
```

## Instance methods

```
-[RAWGainMap outputImage];
-[RAWGainMap setDefaults];
-[RAWGainMap setValue:forKey:];
-[RAWGainMap makeMapSampler];
```
