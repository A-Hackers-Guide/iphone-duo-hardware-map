# `CUIVectorGlyphMutator`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 29 instance methods, 12 class methods

## Instance variables

```
@"CUIVectorGlyphPath" _originPath;
@"CUIVectorGlyphPath" _ultralightPath;
@"CUIVectorGlyphPath" _blackPath;
d _pointSize;
@"NSData" _originClipStrokeKeyframes;
@"NSData" _ultralightClipStrokeKeyframes;
@"NSData" _blackClipStrokeKeyframes;
{?="pointComponents"^d"numPoints"Q} _originPoints;
{?="deltaComponents"^d"numDeltas"Q} _ultralightDeltas;
{?="deltaComponents"^d"numDeltas"Q} _blackDeltas;
```

## Properties

```
@property (T@"CUIVectorGlyphPath",&,N,V_originPath) originPath;
@property (T@"CUIVectorGlyphPath",&,N,V_ultralightPath) ultralightPath;
@property (T@"CUIVectorGlyphPath",&,N,V_blackPath) blackPath;
@property (Td,N,V_pointSize) pointSize;
@property (T{?=^dQ},N,V_originPoints) originPoints;
@property (T{?=^dQ},N,V_ultralightDeltas) ultralightDeltas;
@property (T{?=^dQ},N,V_blackDeltas) blackDeltas;
@property (T@"NSData",&,N,V_originClipStrokeKeyframes) originClipStrokeKeyframes;
@property (T@"NSData",&,N,V_ultralightClipStrokeKeyframes) ultralightClipStrokeKeyframes;
@property (T@"NSData",&,N,V_blackClipStrokeKeyframes) blackClipStrokeKeyframes;
```

## Class methods

```
+[CUIVectorGlyphMutator _scalarsForGlyphContinuousWeight:inDictionary:shouldClamp:];
+[CUIVectorGlyphMutator createFloatDeltasFrom:to:];
+[CUIVectorGlyphMutator transformForGlyphSize:];
+[CUIVectorGlyphMutator createInterpolatedFloatsFromFloats:ultralightDeltas:blackDeltas:withScalars:];
+[CUIVectorGlyphMutator scalarsForGlyphWeight:glyphSize:];
+[CUIVectorGlyphMutator realloc_cgfloat_array:withNewCount:];
+[CUIVectorGlyphMutator transformForGlyphContinuousSize:];
+[CUIVectorGlyphMutator deltaArrayFrom:to:];
+[CUIVectorGlyphMutator _interpolationData];
+[CUIVectorGlyphMutator pointArrayFromPath:];
+[CUIVectorGlyphMutator scalarsForGlyphContinuousWeight:glyphContinuousSize:];
+[CUIVectorGlyphMutator createInterpolatedPointsFromPoints:ultralightDeltas:blackDeltas:withScalars:];
```

## Instance methods

```
-[CUIVectorGlyphMutator originPoints];
-[CUIVectorGlyphMutator pathForScalars:andTransform:];
-[CUIVectorGlyphMutator pathForScalars:];
-[CUIVectorGlyphMutator setBlackPath:];
-[CUIVectorGlyphMutator setPointSize:];
-[CUIVectorGlyphMutator convertDistance0:distance1:elementIndex0Out:distance0Out:elementIndex1Out:distance1Out:subpath0:subpath1:data:];
-[CUIVectorGlyphMutator setBlackClipStrokeKeyframes:];
-[CUIVectorGlyphMutator dealloc];
-[CUIVectorGlyphMutator setOriginPath:];
-[CUIVectorGlyphMutator ultralightPath];
-[CUIVectorGlyphMutator originClipStrokeKeyframes];
-[CUIVectorGlyphMutator setUltralightPath:];
-[CUIVectorGlyphMutator blackPath];
-[CUIVectorGlyphMutator setUltralightClipStrokeKeyframes:];
-[CUIVectorGlyphMutator cgPathFrom:];
-[CUIVectorGlyphMutator setOriginPoints:];
-[CUIVectorGlyphMutator pointSize];
-[CUIVectorGlyphMutator applyDeltasWithScalars:andTransform:];
-[CUIVectorGlyphMutator applyDeltasWithScalars:];
-[CUIVectorGlyphMutator ultralightDeltas];
-[CUIVectorGlyphMutator blackClipStrokeKeyframes];
-[CUIVectorGlyphMutator clipStrokeKeyframesForPath:scalars:];
-[CUIVectorGlyphMutator setUltralightDeltas:];
-[CUIVectorGlyphMutator blackDeltas];
-[CUIVectorGlyphMutator setOriginClipStrokeKeyframes:];
-[CUIVectorGlyphMutator initWithPointSize:regular:ultralight:black:];
-[CUIVectorGlyphMutator originPath];
-[CUIVectorGlyphMutator setBlackDeltas:];
-[CUIVectorGlyphMutator ultralightClipStrokeKeyframes];
```
