# `LTMGeometryDataV2`

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LTMGeometryDataBase`
- 13 instance variables, 15 properties, 22 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputTextureRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _minimumRect;
B _isPortraitOrientated;
f _inputTextureDownsampleRatio;
f _LTMProcessotInputTexToLTMInTexScale;
f _deepZoomRatio;
i _rawSensorWidth;
i _rawSensorHeight;
{CGPoint="x"d"y"d} _deepZoomOrigin;
{CGSize="width"d"height"d} _inputTextureSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _sourceRect;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _sensorSpaceToValidBufferSpaceTransform;
```

## Properties

```
@property (T{CGAffineTransform=dddddd},N,V_sensorSpaceToValidBufferSpaceTransform) sensorSpaceToValidBufferSpaceTransform;
@property (Tf,N,V_deepZoomRatio) deepZoomRatio;
@property (Ti,N,V_rawSensorWidth) rawSensorWidth;
@property (Ti,N,V_rawSensorHeight) rawSensorHeight;
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
-[LTMGeometryDataV2 sourceRect];
-[LTMGeometryDataV2 inputTextureDownsampleRatio];
-[LTMGeometryDataV2 rawSensorWidth];
-[LTMGeometryDataV2 setDeepZoomRatio:];
-[LTMGeometryDataV2 deepZoomRatio];
-[LTMGeometryDataV2 LTMProcessotInputTexToLTMInTexScale];
-[LTMGeometryDataV2 initWithInputTextureWidth:height:];
-[LTMGeometryDataV2 cropRect];
-[LTMGeometryDataV2 setSensorSpaceToValidBufferSpaceTransform:];
-[LTMGeometryDataV2 setRawSensorWidth:];
-[LTMGeometryDataV2 inputTextureSize];
-[LTMGeometryDataV2 setInputTextureDownsampleRatio:];
-[LTMGeometryDataV2 setIsPortraitOrientated:];
-[LTMGeometryDataV2 setDeepZoomOrigin:];
-[LTMGeometryDataV2 isPortraitOrientated];
-[LTMGeometryDataV2 setLTMProcessotInputTexToLTMInTexScale:];
-[LTMGeometryDataV2 setRawSensorHeight:];
-[LTMGeometryDataV2 deepZoomOrigin];
-[LTMGeometryDataV2 copyWithZone:];
-[LTMGeometryDataV2 rawSensorHeight];
-[LTMGeometryDataV2 setCropRect:sourceRect:];
-[LTMGeometryDataV2 sensorSpaceToValidBufferSpaceTransform];
```
