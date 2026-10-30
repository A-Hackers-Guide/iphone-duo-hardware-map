# `VTOpticalFlowConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 9 instance variables, 13 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"VEOpticalFlowConfiguration" _veConfiguration;
I _flowPixelFormat;
q _frameWidth;
q _frameHeight;
q _qualityPrioritization;
q _revision;
@"NSArray" _frameSupportedPixelFormats;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (Tq,R,N,V_qualityPrioritization) qualityPrioritization;
@property (Tq,R,N,V_revision) revision;
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
+[VTOpticalFlowConfiguration isSupported];
+[VTOpticalFlowConfiguration defaultRevision];
+[VTOpticalFlowConfiguration processorSupported];
+[VTOpticalFlowConfiguration supportedRevisions];
```

## Instance methods

```
-[VTOpticalFlowConfiguration revision];
-[VTOpticalFlowConfiguration dealloc];
-[VTOpticalFlowConfiguration qualityPrioritization];
-[VTOpticalFlowConfiguration veConfiguration];
-[VTOpticalFlowConfiguration destinationPixelBufferAttributes];
-[VTOpticalFlowConfiguration frameHeight];
-[VTOpticalFlowConfiguration frameSupportedPixelFormats];
-[VTOpticalFlowConfiguration frameWidth];
-[VTOpticalFlowConfiguration initWithFrameWidth:frameHeight:qualityPrioritization:revision:];
-[VTOpticalFlowConfiguration sourcePixelBufferAttributes];
```
