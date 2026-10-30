# `CUIVectorGlyphPath`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 10 instance methods, 11 class methods

## Instance variables

```
{CUIVectorGlyphPathLengthData="totalLength"f"subpathLengths"^f"elementLengths"^{CUIVectorGlyphPathElementLength}"elementToSubpath"^Q"numSubpaths"Q"numElements"Q} _lengthData;
@ _path;
@"NSData" _clipStrokeKeyframes;
```

## Properties

```
@property (T@,R,&,N,V_path) path;
@property (T@"NSData",R,&,N,V_clipStrokeKeyframes) clipStrokeKeyframes;
@property (T@"NSData",R,&,N) encodedClipStrokeKeyframes;
@property (Tq,R,N) subpathCount;
```

## Class methods

```
+[CUIVectorGlyphPath _createConcatenatingPaths:indices:];
+[CUIVectorGlyphPath createFromSubpaths:indices:clipStrokeIndices:];
+[CUIVectorGlyphPath realloc_float_array:withNewCount:];
+[CUIVectorGlyphPath _createAdoptingPath:clipStrokeKeyframes:];
+[CUIVectorGlyphPath createConcatenatingPaths:];
+[CUIVectorGlyphPath realloc_length_array:withNewCount:];
+[CUIVectorGlyphPath createWithPath:clipStrokeKeyframeProvider:];
+[CUIVectorGlyphPath createWithPath:clipStrokeKeyframes:];
+[CUIVectorGlyphPath createFromSubpaths:indices:];
+[CUIVectorGlyphPath realloc_long_array:withNewCount:];
+[CUIVectorGlyphPath emptyData];
```

## Instance methods

```
-[CUIVectorGlyphPath dealloc];
-[CUIVectorGlyphPath createSubpaths];
-[CUIVectorGlyphPath createCopyApplyingTransform:];
-[CUIVectorGlyphPath clipStrokeKeyframes];
-[CUIVectorGlyphPath computeLengthData];
-[CUIVectorGlyphPath encodedClipStrokeKeyframes];
-[CUIVectorGlyphPath copyWithZone:];
-[CUIVectorGlyphPath subpathCount];
-[CUIVectorGlyphPath lengthData];
-[CUIVectorGlyphPath path];
```
