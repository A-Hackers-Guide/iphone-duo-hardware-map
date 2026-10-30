# `VTTemporalNoiseFilterConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 10 instance variables, 11 properties, 15 instance methods, 5 class methods

## Instance variables

```
I _sourcePixelFormat;
q _filterStrengthMode;
q _latencyMode;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
@"NSArray" _frameSupportedPixelFormats;
q _nextFrameCount;
q _previousFrameCount;
q _frameWidth;
q _frameHeight;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (T@"NSArray",R,N,V_frameSupportedPixelFormats) frameSupportedPixelFormats;
@property (T@"NSDictionary",R,N,V_sourcePixelBufferAttributes) sourcePixelBufferAttributes;
@property (T@"NSDictionary",R,N,V_destinationPixelBufferAttributes) destinationPixelBufferAttributes;
@property (Tq,R,N,V_nextFrameCount) nextFrameCount;
@property (Tq,R,N,V_previousFrameCount) previousFrameCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[VTTemporalNoiseFilterConfiguration isSupported];
+[VTTemporalNoiseFilterConfiguration _loadCapabilities];
+[VTTemporalNoiseFilterConfiguration maximumDimensions];
+[VTTemporalNoiseFilterConfiguration minimumDimensions];
+[VTTemporalNoiseFilterConfiguration supportedSourcePixelFormats];
```

## Instance methods

```
-[VTTemporalNoiseFilterConfiguration dealloc];
-[VTTemporalNoiseFilterConfiguration initWithFrameWidth:frameHeight:];
-[VTTemporalNoiseFilterConfiguration destinationPixelBufferAttributes];
-[VTTemporalNoiseFilterConfiguration filterStrengthMode];
-[VTTemporalNoiseFilterConfiguration frameHeight];
-[VTTemporalNoiseFilterConfiguration frameSupportedPixelFormats];
-[VTTemporalNoiseFilterConfiguration frameWidth];
-[VTTemporalNoiseFilterConfiguration initWithFrameWidth:frameHeight:filterStrengthMode:latencyMode:sourcePixelFormat:];
-[VTTemporalNoiseFilterConfiguration initWithFrameWidth:frameHeight:sourcePixelFormat:];
-[VTTemporalNoiseFilterConfiguration latencyMode];
-[VTTemporalNoiseFilterConfiguration loadProperties];
-[VTTemporalNoiseFilterConfiguration nextFrameCount];
-[VTTemporalNoiseFilterConfiguration previousFrameCount];
-[VTTemporalNoiseFilterConfiguration sourcePixelBufferAttributes];
-[VTTemporalNoiseFilterConfiguration sourcePixelFormat];
```
