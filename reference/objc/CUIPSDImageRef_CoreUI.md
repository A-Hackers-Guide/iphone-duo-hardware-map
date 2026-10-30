# `CUIPSDImageRef`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 77 instance methods, 4 class methods

## Instance variables

```
^v _psd;
@"NSString" _path;
i _file;
B _parsedForLayers;
@"_CUIPSDSublayerInfo" _rootLayers;
```

## Properties

```
@property (Ti,N,V_file) file;
@property (T@"NSString",C,N,V_path) path;
@property (T^v,N,V_psd) psd;
```

## Class methods

```
+[CUIPSDImageRef isValidPSDResourceAtPath:];
+[CUIPSDImageRef isValidPSDResourceAtPath:withImageInfo:];
+[CUIPSDImageRef isValidPSDResourceAtPath:withLayerCount:];
+[CUIPSDImageRef isValidPSDResourceAtPath:withLayerCount:validateLayers:];
```

## Instance methods

```
-[CUIPSDImageRef file];
-[CUIPSDImageRef initWithPath:];
-[CUIPSDImageRef dealloc];
-[CUIPSDImageRef size];
-[CUIPSDImageRef setPath:];
-[CUIPSDImageRef path];
-[CUIPSDImageRef numberOfChannels];
-[CUIPSDImageRef setFile:];
-[CUIPSDImageRef layerNames];
-[CUIPSDImageRef imageInfo];
-[CUIPSDImageRef numberOfLayers];
-[CUIPSDImageRef metadataString];
-[CUIPSDImageRef _psdLayerRecordAtAbsoluteIndex:];
-[CUIPSDImageRef imageFromSlice:atAbsoluteLayer:];
-[CUIPSDImageRef layerEnumerator];
-[CUIPSDImageRef psdFile];
-[CUIPSDImageRef setPsd:];
-[CUIPSDImageRef _innerGlowFromLayerEffectsInfo:];
-[CUIPSDImageRef _outerGlowFromLayerEffectsInfo:];
-[CUIPSDImageRef boundsForSlice:];
-[CUIPSDImageRef psd];
-[CUIPSDImageRef _absoluteIndexOfRootLayer:];
-[CUIPSDImageRef _bevelEmbossFromLayerEffectsInfo:];
-[CUIPSDImageRef _blendModeAtAbsluteIndex:];
-[CUIPSDImageRef _boundsAtAbsoluteIndex:];
-[CUIPSDImageRef _colorOverlayFromLayerEffectsInfo:];
-[CUIPSDImageRef _copyCGImageAtAbsoluteIndex:];
-[CUIPSDImageRef _copySublayerInfoAtAbsoluteIndex:atRoot:];
-[CUIPSDImageRef _createMaskFromSlice:atAbsoluteIndex:];
-[CUIPSDImageRef _dropShadowFromLayerEffectsInfo:];
-[CUIPSDImageRef _fillOpacityAtAbsoluteIndex:];
-[CUIPSDImageRef _fillSampleAtAbsoluteIndex:];
-[CUIPSDImageRef _gradientAtAbsoluteIndex:];
-[CUIPSDImageRef _gradientOverlayFromLayerEffectsAtAbsoluteIndex:];
-[CUIPSDImageRef _imageAtAbsoluteIndex:isZeroSizeImage:];
-[CUIPSDImageRef _imageFromSlice:atAbsoluteIndex:isEmptyImage:];
-[CUIPSDImageRef _innerShadowFromLayerEffectsInfo:];
-[CUIPSDImageRef _layerEffectsAtAbsoluteIndex:];
-[CUIPSDImageRef _layerIndexFromLayerNames:indexRangeBegin:indexRangeEnd:isTopLevel:];
-[CUIPSDImageRef _layerInfo];
-[CUIPSDImageRef _layerRefAtAbsoluteIndex:];
-[CUIPSDImageRef _logInvalidAbsoluteIndex:psd:];
-[CUIPSDImageRef _nameAtAbsoluteIndex:];
-[CUIPSDImageRef _namesOfSublayers:];
-[CUIPSDImageRef _opacityAtAbsoluteIndex:];
-[CUIPSDImageRef _patternFromSlice:atAbsoluteIndex:isZeroSizeImage:];
-[CUIPSDImageRef _psdFileWithLayers:];
-[CUIPSDImageRef _treatDividerAsLayer];
-[CUIPSDImageRef _visibilityAtAbsoluteIndex:];
-[CUIPSDImageRef absoluteLayerIndexFromLayerNames:];
-[CUIPSDImageRef boundsAtLayer:];
-[CUIPSDImageRef cgBlendModeForPSDLayerOrLayerEffectBlendMode:];
-[CUIPSDImageRef colorFromDocumentColor:];
-[CUIPSDImageRef compositeImage];
-[CUIPSDImageRef copyColorSpace];
-[CUIPSDImageRef createCGImageAtLayer:];
-[CUIPSDImageRef createCompositeCGImage];
-[CUIPSDImageRef enumerateLayersUsingBlock:];
-[CUIPSDImageRef fillSampleAtLayer:];
-[CUIPSDImageRef gradientAtLayer:];
-[CUIPSDImageRef imageAtLayer:];
-[CUIPSDImageRef imageAtLayer:isZeroSizeImage:];
-[CUIPSDImageRef imageFromRef:];
-[CUIPSDImageRef imageFromSlice:atLayer:];
-[CUIPSDImageRef imageFromSlice:atLayer:isEmptyImage:];
-[CUIPSDImageRef layerRefAtIndex:];
-[CUIPSDImageRef loadPSDFileWithLayers:];
-[CUIPSDImageRef maskFromCompositeAlphaChannel:];
-[CUIPSDImageRef maskFromSlice:atLayer:];
-[CUIPSDImageRef metricsInAlphaChannel:forRect:];
-[CUIPSDImageRef metricsInMask:forRect:];
-[CUIPSDImageRef numberOfSlices];
-[CUIPSDImageRef openImageFile];
-[CUIPSDImageRef patternFromSlice:atLayer:];
-[CUIPSDImageRef patternFromSlice:atLayer:isZeroSizeImage:];
-[CUIPSDImageRef psdFileForComposite];
-[CUIPSDImageRef visibilityAtLayer:];
```
