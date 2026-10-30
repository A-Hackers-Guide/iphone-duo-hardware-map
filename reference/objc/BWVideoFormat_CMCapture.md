# `BWVideoFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFormat`
- 13 instance variables, 14 properties, 33 instance methods, 11 class methods

## Instance variables

```
Q _width;
Q _height;
Q _sliceCount;
I _pixelFormat;
Q _bytesPerRowAlignment;
Q _planeAlignment;
Q _extendedWidth;
Q _extendedHeight;
I _cacheMode;
B _prewireBuffers;
B _memoryPoolUseAllowed;
@"NSDictionary" _pixelBufferAttributes;
i _colorSpaceProperties;
```

## Properties

```
@property (TQ,N,V_width) width;
@property (TQ,N,V_height) height;
@property (T{?=ii},R,N) dimensions;
@property (TQ,N,V_sliceCount) sliceCount;
@property (TI,N,V_pixelFormat) pixelFormat;
@property (TQ,N,V_bytesPerRowAlignment) bytesPerRowAlignment;
@property (TQ,N,V_planeAlignment) planeAlignment;
@property (TQ,N,V_extendedWidth) extendedWidth;
@property (TQ,N,V_extendedHeight) extendedHeight;
@property (TI,N,V_cacheMode) cacheMode;
@property (TB,N,V_prewireBuffers) prewireBuffers;
@property (TB,N,V_memoryPoolUseAllowed) memoryPoolUseAllowed;
@property (T@"NSDictionary",R,N,V_pixelBufferAttributes) pixelBufferAttributes;
@property (Ti,R,N,V_colorSpaceProperties) colorSpaceProperties;
```

## Class methods

```
+[BWVideoFormat initialize];
+[BWVideoFormat colorInfoWithSourceColorSpace:sourcePixelFormat:sourceDimensions:requestedPixelFormat:];
+[BWVideoFormat colorSpacePropertiesForPixelBufferAttachments:];
+[BWVideoFormat colorSpacePropertiesForSourceThatSupportsWideColor:sourceColorSpace:sourcePixelFormat:sourceDimensions:requestedPixelFormat:];
+[BWVideoFormat colorSpacePropertiesForSourceThatSupportsWideColor:sourceColorSpace:sourcePixelFormat:sourceDimensions:requestedPixelFormat:supportedColorSpaces:];
+[BWVideoFormat colorSpacePropertiesWithSourceColorSpace:sourcePixelFormat:sourceDimensions:requestedPixelFormat:];
+[BWVideoFormat colorSpacePropertiesWithSourceColorSpace:sourcePixelFormat:sourceDimensions:requestedPixelFormat:supportedColorSpaces:];
+[BWVideoFormat compressionPropertiesForColorSpaceProperties:];
+[BWVideoFormat formatByResolvingRequirements:];
+[BWVideoFormat formatByResolvingRequirements:printErrors:];
+[BWVideoFormat pixelBufferAttachmentsForColorSpaceProperties:];
```

## Instance methods

```
-[BWVideoFormat formatDescription];
-[BWVideoFormat extendedWidth];
-[BWVideoFormat extendedHeight];
-[BWVideoFormat dimensions];
-[BWVideoFormat pixelBufferAttributes];
-[BWVideoFormat prewireBuffers];
-[BWVideoFormat setExtendedWidth:];
-[BWVideoFormat debugDescription];
-[BWVideoFormat sliceCount];
-[BWVideoFormat dealloc];
-[BWVideoFormat isHLGColorSpace];
-[BWVideoFormat memoryPoolUseAllowed];
-[BWVideoFormat formatWithUpdatedDimensions:dimensionAlignment:memoryPoolUseAllowed:];
-[BWVideoFormat setHeight:];
-[BWVideoFormat setPlaneAlignment:];
-[BWVideoFormat setPrewireBuffers:];
-[BWVideoFormat cacheMode];
-[BWVideoFormat setSliceCount:];
-[BWVideoFormat planeAlignment];
-[BWVideoFormat description];
-[BWVideoFormat pixelFormat];
-[BWVideoFormat setWidth:];
-[BWVideoFormat width];
-[BWVideoFormat colorSpaceProperties];
-[BWVideoFormat setPixelFormat:];
-[BWVideoFormat mediaType];
-[BWVideoFormat setCacheMode:];
-[BWVideoFormat setBytesPerRowAlignment:];
-[BWVideoFormat isEqual:];
-[BWVideoFormat height];
-[BWVideoFormat setExtendedHeight:];
-[BWVideoFormat bytesPerRowAlignment];
-[BWVideoFormat setMemoryPoolUseAllowed:];
```
