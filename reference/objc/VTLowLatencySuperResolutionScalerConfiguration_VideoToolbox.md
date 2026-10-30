# `VTLowLatencySuperResolutionScalerConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 7 instance variables, 12 properties, 9 instance methods, 7 class methods

## Instance variables

```
@"VCPFrameSuperResolutionConfiguration" vcpConfiguration;
f _scaleFactor;
q _frameWidth;
q _frameHeight;
@"NSArray" _frameSupportedPixelFormats;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (T@"NSArray",R,N,V_frameSupportedPixelFormats) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N,V_destinationPixelBufferAttributes) destinationPixelBufferAttributes;
@property (Tf,R,N,V_scaleFactor) scaleFactor;
@property (Tq,?,R,N) nextFrameCount;
@property (Tq,?,R,N) previousFrameCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTLowLatencySuperResolutionScalerConfiguration isSupported];
+[VTLowLatencySuperResolutionScalerConfiguration maximumDimensionForSpatialScaleFactor:];
+[VTLowLatencySuperResolutionScalerConfiguration maximumDimensions];
+[VTLowLatencySuperResolutionScalerConfiguration maximumPixelCountForSpatialScaleFactor:];
+[VTLowLatencySuperResolutionScalerConfiguration minimumDimensions];
+[VTLowLatencySuperResolutionScalerConfiguration supportedScaleFactors];
+[VTLowLatencySuperResolutionScalerConfiguration supportedScaleFactorsForFrameWidth:frameHeight:];
```

## Instance methods

```
-[VTLowLatencySuperResolutionScalerConfiguration dealloc];
-[VTLowLatencySuperResolutionScalerConfiguration scaleFactor];
-[VTLowLatencySuperResolutionScalerConfiguration destinationPixelBufferAttributes];
-[VTLowLatencySuperResolutionScalerConfiguration frameHeight];
-[VTLowLatencySuperResolutionScalerConfiguration frameSupportedPixelFormats];
-[VTLowLatencySuperResolutionScalerConfiguration frameWidth];
-[VTLowLatencySuperResolutionScalerConfiguration initWithFrameWidth:frameHeight:scaleFactor:];
-[VTLowLatencySuperResolutionScalerConfiguration sourcePixelBufferAttributes];
-[VTLowLatencySuperResolutionScalerConfiguration vcpConfiguration];
```
