# `LTMGeometryDataBase` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`](../userland/System__Library__PrivateFrameworks__CameraColorProcessing.framework__CameraColorProcessing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},N) deepZoomOrigin;
@property (Tf,N) inputTextureDownsampleRatio;
@property (Tf,N) LTMProcessotInputTexToLTMInTexScale;
@property (T{CGSize=dd},R,N) inputTextureSize;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) cropRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) sourceRect;
@property (TB,N) isPortraitOrientated;
```

## Instance methods

```
-[LTMGeometryDataBase sourceRect];
-[LTMGeometryDataBase inputTextureDownsampleRatio];
-[LTMGeometryDataBase init];
-[LTMGeometryDataBase LTMProcessotInputTexToLTMInTexScale];
-[LTMGeometryDataBase initWithInputTextureWidth:height:];
-[LTMGeometryDataBase cropRect];
-[LTMGeometryDataBase inputTextureSize];
-[LTMGeometryDataBase setInputTextureDownsampleRatio:];
-[LTMGeometryDataBase setIsPortraitOrientated:];
-[LTMGeometryDataBase setDeepZoomOrigin:];
-[LTMGeometryDataBase isPortraitOrientated];
-[LTMGeometryDataBase setLTMProcessotInputTexToLTMInTexScale:];
-[LTMGeometryDataBase deepZoomOrigin];
-[LTMGeometryDataBase setCropRect:sourceRect:];
```
