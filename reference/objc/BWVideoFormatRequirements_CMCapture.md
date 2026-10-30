# `BWVideoFormatRequirements`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFormatRequirements`
- Protocols: `NSSecureCoding`
- 13 instance variables, 15 properties, 39 instance methods, 7 class methods

## Instance variables

```
Q _width;
Q _height;
Q _sliceCount;
@"NSArray" _supportedPixelFormats;
@"NSArray" _preferredPixelFormats;
@"NSArray" _supportedColorSpaceProperties;
Q _bytesPerRowAlignment;
Q _planeAlignment;
Q _widthAlignment;
Q _heightAlignment;
@"NSArray" _supportedCacheModes;
B _prewireBuffers;
B _memoryPoolUseAllowed;
```

## Properties

```
@property (TQ,N,V_width) width;
@property (TQ,N,V_height) height;
@property (T{?=ii},N) dimensions;
@property (TQ,N,V_sliceCount) sliceCount;
@property (T@"NSArray",C,N,V_supportedPixelFormats) supportedPixelFormats;
@property (T@"NSArray",C,N,V_preferredPixelFormats) preferredPixelFormats;
@property (T@"NSArray",C,N,V_supportedColorSpaceProperties) supportedColorSpaceProperties;
@property (TQ,N,V_bytesPerRowAlignment) bytesPerRowAlignment;
@property (TQ,N,V_planeAlignment) planeAlignment;
@property (TQ,N,V_widthAlignment) widthAlignment;
@property (TQ,N,V_heightAlignment) heightAlignment;
@property (T@"NSArray",C,N,V_supportedCacheModes) supportedCacheModes;
@property (T@"NSDictionary",R,N) pixelBufferAttributes;
@property (TB,N,V_prewireBuffers) prewireBuffers;
@property (TB,N,V_memoryPoolUseAllowed) memoryPoolUseAllowed;
```

## Class methods

```
+[BWVideoFormatRequirements supportsSecureCoding];
+[BWVideoFormatRequirements formatRequirements];
+[BWVideoFormatRequirements initialize];
+[BWVideoFormatRequirements cacheModesForOptimizedCPUAccess];
+[BWVideoFormatRequirements cacheModesForCacheProfile:];
+[BWVideoFormatRequirements cacheModesForOptimizedDisplayAccess];
+[BWVideoFormatRequirements cacheModesForOptimizedHWAccess];
```

## Instance methods

```
-[BWVideoFormatRequirements setDimensions:];
-[BWVideoFormatRequirements dimensions];
-[BWVideoFormatRequirements pixelBufferAttributes];
-[BWVideoFormatRequirements setSupportedPixelFormats:];
-[BWVideoFormatRequirements prewireBuffers];
-[BWVideoFormatRequirements debugDescription];
-[BWVideoFormatRequirements sliceCount];
-[BWVideoFormatRequirements init];
-[BWVideoFormatRequirements dealloc];
-[BWVideoFormatRequirements supportedColorSpaceProperties];
-[BWVideoFormatRequirements setWidthAlignment:];
-[BWVideoFormatRequirements memoryPoolUseAllowed];
-[BWVideoFormatRequirements setSupportedColorSpaceProperties:];
-[BWVideoFormatRequirements setHeight:];
-[BWVideoFormatRequirements setHeightAlignment:];
-[BWVideoFormatRequirements setPlaneAlignment:];
-[BWVideoFormatRequirements setPrewireBuffers:];
-[BWVideoFormatRequirements encodeWithCoder:];
-[BWVideoFormatRequirements preferredPixelFormats];
-[BWVideoFormatRequirements setSliceCount:];
-[BWVideoFormatRequirements planeAlignment];
-[BWVideoFormatRequirements description];
-[BWVideoFormatRequirements initWithCoder:];
-[BWVideoFormatRequirements supportedPixelFormats];
-[BWVideoFormatRequirements setPreferredPixelFormats:];
-[BWVideoFormatRequirements setWidth:];
-[BWVideoFormatRequirements setSupportedCacheModes:];
-[BWVideoFormatRequirements width];
-[BWVideoFormatRequirements formatClass];
-[BWVideoFormatRequirements initWithPixelBufferAttributes:];
-[BWVideoFormatRequirements mediaType];
-[BWVideoFormatRequirements setBytesPerRowAlignment:];
-[BWVideoFormatRequirements isEqual:];
-[BWVideoFormatRequirements heightAlignment];
-[BWVideoFormatRequirements height];
-[BWVideoFormatRequirements widthAlignment];
-[BWVideoFormatRequirements supportedCacheModes];
-[BWVideoFormatRequirements bytesPerRowAlignment];
-[BWVideoFormatRequirements setMemoryPoolUseAllowed:];
```
