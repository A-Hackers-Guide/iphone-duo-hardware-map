# `AVSemanticSegmentationMatte`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 15 instance methods, 4 class methods

## Instance variables

```
@"NSString" _matteType;
^{__CVBuffer=} _pixelBuffer;
i _version;
```

## Properties

```
@property (T@"NSString",R) matteType;
@property (TI,R) pixelFormatType;
@property (T^{__CVBuffer=},R) mattingImage;
```

## Class methods

```
+[AVSemanticSegmentationMatte initialize];
+[AVSemanticSegmentationMatte semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:];
+[AVSemanticSegmentationMatte _allSupportedSemanticSegmentationMattePixelFormatTypes];
+[AVSemanticSegmentationMatte _allSupportedSemanticSegmentationMatteTypes];
```

## Instance methods

```
-[AVSemanticSegmentationMatte auxiliaryImageType];
-[AVSemanticSegmentationMatte debugDescription];
-[AVSemanticSegmentationMatte dealloc];
-[AVSemanticSegmentationMatte description];
-[AVSemanticSegmentationMatte pixelFormatType];
-[AVSemanticSegmentationMatte dictionaryRepresentationForAuxiliaryDataType:];
-[AVSemanticSegmentationMatte mattingImage];
-[AVSemanticSegmentationMatte copyAuxiliaryMetadata];
-[AVSemanticSegmentationMatte initWithType:pixelBuffer:auxiliaryMetadata:];
-[AVSemanticSegmentationMatte initWithType:pixelBuffer:semanticSegmentationMatteMetadataDictionary:];
-[AVSemanticSegmentationMatte matteType];
-[AVSemanticSegmentationMatte semanticSegmentationMatteByApplyingExifOrientation:];
-[AVSemanticSegmentationMatte semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:];
-[AVSemanticSegmentationMatte versionMajor];
-[AVSemanticSegmentationMatte versionMinor];
```
