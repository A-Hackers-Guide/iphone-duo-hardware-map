# `BWIOSurfaceCompressionHistogramAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 7 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSString" _portType;
I _bufferHeight;
i _nodeType;
B _pixelFormatIsTenBit;
I _numberOfSamples;
[16Q] _lumaCompressionHistogram;
[16Q] _chromaCompressionHistogram;
```

## Properties

```
@property (T@"NSString",&,N,V_portType) portType;
@property (TI,N,V_bufferHeight) bufferHeight;
@property (Ti,N,V_nodeType) nodeType;
@property (TB,N,V_pixelFormatIsTenBit) pixelFormatIsTenBit;
@property (TI,N,V_numberOfSamples) numberOfSamples;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWIOSurfaceCompressionHistogramAnalyticsPayload portType];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload eventDictionary];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload dealloc];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload reset];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload numberOfSamples];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setPixelFormatIsTenBit:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setPortType:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload eventName];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload pixelFormatIsTenBit];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload nodeType];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setNodeType:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload bufferHeight];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setBufferHeight:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setChromaCompressionHistogram:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setLumaCompressionHistogram:];
-[BWIOSurfaceCompressionHistogramAnalyticsPayload setNumberOfSamples:];
```
