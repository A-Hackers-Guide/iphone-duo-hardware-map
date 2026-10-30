# `MPSGraphCropResizeOpDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- Protocols: `NSCopying`
- 7 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _normalizeCoordinates;
f _spatialScale;
Q _resizeWidth;
Q _resizeHeight;
Q _resizeMode;
Q _samplingMode;
Q _coordinateMode;
```

## Properties

```
@property (TQ,N,V_resizeWidth) resizeWidth;
@property (TQ,N,V_resizeHeight) resizeHeight;
@property (TB,N,V_normalizeCoordinates) normalizeCoordinates;
@property (Tf,N,V_spatialScale) spatialScale;
@property (TQ,N,V_resizeMode) resizeMode;
@property (TQ,N,V_samplingMode) samplingMode;
@property (TQ,N,V_coordinateMode) coordinateMode;
```

## Class methods

```
+[MPSGraphCropResizeOpDescriptor descriptorWithResizeWidth:resizeHeight:];
+[MPSGraphCropResizeOpDescriptor descriptorWithResizeWidth:resizeHeight:normalizeCoordinates:spatialScale:resizeMode:samplingMode:coordinateMode:];
```

## Instance methods

```
-[MPSGraphCropResizeOpDescriptor resizeMode];
-[MPSGraphCropResizeOpDescriptor setResizeMode:];
-[MPSGraphCropResizeOpDescriptor copyWithZone:];
-[MPSGraphCropResizeOpDescriptor setResizeWidth:];
-[MPSGraphCropResizeOpDescriptor coordinateMode];
-[MPSGraphCropResizeOpDescriptor normalizeCoordinates];
-[MPSGraphCropResizeOpDescriptor resizeHeight];
-[MPSGraphCropResizeOpDescriptor resizeWidth];
-[MPSGraphCropResizeOpDescriptor samplingMode];
-[MPSGraphCropResizeOpDescriptor setCoordinateMode:];
-[MPSGraphCropResizeOpDescriptor setNormalizeCoordinates:];
-[MPSGraphCropResizeOpDescriptor setResizeHeight:];
-[MPSGraphCropResizeOpDescriptor setSamplingMode:];
-[MPSGraphCropResizeOpDescriptor setSpatialScale:];
-[MPSGraphCropResizeOpDescriptor spatialScale];
```
