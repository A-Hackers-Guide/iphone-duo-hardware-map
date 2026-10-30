# `LTMGeometryDataV1`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMGeometryDataBase`
- 9 instance variables, 11 properties, 14 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputTextureRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minimumRect;
B _isPortraitOrientated;
f _inputTextureDownsampleRatio;
f _LTMProcessotInputTexToLTMInTexScale;
{CGPoint="x"d"y"d} _deepZoomOrigin;
{CGSize="width"d"height"d} _inputTextureSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
```

## Properties

```
@property (T{CGPoint=dd},N,V_deepZoomOrigin) deepZoomOrigin;
@property (Tf,N,V_inputTextureDownsampleRatio) inputTextureDownsampleRatio;
@property (Tf,N,V_LTMProcessotInputTexToLTMInTexScale) LTMProcessotInputTexToLTMInTexScale;
@property (T{CGSize=dd},R,N,V_inputTextureSize) inputTextureSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRect) cropRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_sourceRect) sourceRect;
@property (TB,N,V_isPortraitOrientated) isPortraitOrientated;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LTMGeometryDataV1 sourceRect];
-[LTMGeometryDataV1 inputTextureDownsampleRatio];
-[LTMGeometryDataV1 LTMProcessotInputTexToLTMInTexScale];
-[LTMGeometryDataV1 initWithInputTextureWidth:height:];
-[LTMGeometryDataV1 cropRect];
-[LTMGeometryDataV1 inputTextureSize];
-[LTMGeometryDataV1 setInputTextureDownsampleRatio:];
-[LTMGeometryDataV1 setIsPortraitOrientated:];
-[LTMGeometryDataV1 setDeepZoomOrigin:];
-[LTMGeometryDataV1 isPortraitOrientated];
-[LTMGeometryDataV1 setLTMProcessotInputTexToLTMInTexScale:];
-[LTMGeometryDataV1 deepZoomOrigin];
-[LTMGeometryDataV1 copyWithZone:];
-[LTMGeometryDataV1 setCropRect:sourceRect:];
```
