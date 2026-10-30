# `VTTestProcessorConfiguration`

- Image: [`/System/Library/Frameworks/VideoToolbox.framework/VideoToolbox`](../userland/System__Library__Frameworks__VideoToolbox.framework__VideoToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VTFrameProcessorConfiguration`
- 6 instance variables, 12 properties, 8 instance methods, 4 class methods

## Instance variables

```
q _frameWidth;
q _frameHeight;
q _flags;
@"NSArray" _frameSupportedPixelFormats;
@"NSDictionary" _sourcePixelBufferAttributes;
@"NSDictionary" _destinationPixelBufferAttributes;
```

## Properties

```
@property (Tq,R,N,V_frameWidth) frameWidth;
@property (Tq,R,N,V_frameHeight) frameHeight;
@property (Tq,R,N,V_flags) flags;
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
+[VTTestProcessorConfiguration isSupported];
+[VTTestProcessorConfiguration maximumDimensions];
+[VTTestProcessorConfiguration minimumDimensions];
+[VTTestProcessorConfiguration processorSupported];
```

## Instance methods

```
-[VTTestProcessorConfiguration flags];
-[VTTestProcessorConfiguration dealloc];
-[VTTestProcessorConfiguration destinationPixelBufferAttributes];
-[VTTestProcessorConfiguration frameHeight];
-[VTTestProcessorConfiguration frameSupportedPixelFormats];
-[VTTestProcessorConfiguration frameWidth];
-[VTTestProcessorConfiguration initWithFrameWidth:frameHeight:flags:];
-[VTTestProcessorConfiguration sourcePixelBufferAttributes];
```
