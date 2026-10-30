# `BWMultiFilterThumbnailNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
{CGSize="width"d"height"d} _thumbnailSize;
@"NSArray" _filters;
i _maxLossyCompressionLevel;
@"BWColorLookupCache" _colorLookupCache;
@"FigColorCubeMetalFilter" _filter;
^{opaqueCMFormatDescription=} _mostRecentFormatDescription;
```

## Class methods

```
+[BWMultiFilterThumbnailNode initialize];
```

## Instance methods

```
-[BWMultiFilterThumbnailNode prepareForCurrentConfigurationToBecomeLive];
-[BWMultiFilterThumbnailNode renderSampleBuffer:forInput:];
-[BWMultiFilterThumbnailNode dealloc];
-[BWMultiFilterThumbnailNode didReachEndOfDataForConfigurationID:input:];
-[BWMultiFilterThumbnailNode nodeSubType];
-[BWMultiFilterThumbnailNode didSelectFormat:forInput:];
-[BWMultiFilterThumbnailNode nodeType];
-[BWMultiFilterThumbnailNode initWithFilters:thumbnailSize:maxLossyCompressionLevel:];
```
