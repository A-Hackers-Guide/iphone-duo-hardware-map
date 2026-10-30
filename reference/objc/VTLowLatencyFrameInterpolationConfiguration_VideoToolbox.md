# `VTLowLatencyFrameInterpolationConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 8 instance variables, 13 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"VCPVideoInterpolationConfiguration" vcpConfiguration;
q _frameWidth;
q _frameHeight;
q _spatialScaleFactor;
q _numberOfInterpolatedFrames;
@"NSArray" _frameSupportedPixelFormats;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (Tq,R,N,V_spatialScaleFactor) spatialScaleFactor;
@property (Tq,R,N,V_numberOfInterpolatedFrames) numberOfInterpolatedFrames;
@property (T@"NSArray",R,N,V_frameSupportedPixelFormats) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N,V_destinationPixelBufferAttributes) destinationPixelBufferAttributes;
@property (Tq,?,R,N) nextFrameCount;
@property (Tq,?,R,N) previousFrameCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTLowLatencyFrameInterpolationConfiguration isSupported];
+[VTLowLatencyFrameInterpolationConfiguration maximumDimensionForSpatialScaleFactor:];
+[VTLowLatencyFrameInterpolationConfiguration maximumPixelCountForSpatialScaleFactor:];
```

## Instance methods

```
-[VTLowLatencyFrameInterpolationConfiguration dealloc];
-[VTLowLatencyFrameInterpolationConfiguration destinationPixelBufferAttributes];
-[VTLowLatencyFrameInterpolationConfiguration frameHeight];
-[VTLowLatencyFrameInterpolationConfiguration frameSupportedPixelFormats];
-[VTLowLatencyFrameInterpolationConfiguration frameWidth];
-[VTLowLatencyFrameInterpolationConfiguration initWithFrameWidth:frameHeight:numberOfInterpolatedFrames:];
-[VTLowLatencyFrameInterpolationConfiguration initWithFrameWidth:frameHeight:spatialScaleFactor:];
-[VTLowLatencyFrameInterpolationConfiguration numberOfInterpolatedFrames];
-[VTLowLatencyFrameInterpolationConfiguration sourcePixelBufferAttributes];
-[VTLowLatencyFrameInterpolationConfiguration spatialScaleFactor];
-[VTLowLatencyFrameInterpolationConfiguration vcpConfiguration];
```
