# `AVMetadataTextRegionObject`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVMetadataObject`
- 4 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
q _regionID;
f _confidence;
f _angularOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _angularOffsetBounds;
```

## Properties

```
@property (Tq,R,V_regionID) regionID;
@property (Tf,R,V_confidence) confidence;
@property (Tf,R,V_angularOffset) angularOffset;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,V_angularOffsetBounds) angularOffsetBounds;
```

## Class methods

```
+[AVMetadataTextRegionObject textRegionObjectWithDictionary:input:];
```

## Instance methods

```
-[AVMetadataTextRegionObject dealloc];
-[AVMetadataTextRegionObject regionID];
-[AVMetadataTextRegionObject copyWithZone:];
-[AVMetadataTextRegionObject confidence];
-[AVMetadataTextRegionObject angularOffset];
-[AVMetadataTextRegionObject angularOffsetBounds];
-[AVMetadataTextRegionObject initDerivedMetadataObjectFromMetadataObject:withTransform:isVideoMirrored:rollAdjustment:];
-[AVMetadataTextRegionObject initTextRegionObjectWithDictionary:input:];
```
