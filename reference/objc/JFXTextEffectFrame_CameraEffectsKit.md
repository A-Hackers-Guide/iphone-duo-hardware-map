# `JFXTextEffectFrame`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 18 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _forcePosterFrame;
i _effectOrigin;
i _origin;
@"NSArray" _hitAreaPoints;
^{CGPath=} _hitAreaPath;
^{CGPath=} _expandedHitAreaPath;
@"JFXTextEffectTransforms" _transforms;
@"NSArray" _textFrames;
{CGSize="width"d"height"d} _effectSize;
{CGSize="width"d"height"d} _relativeToSize;
{?="value"q"timescale"i"flags"I"epoch"q} _time;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _outputROI;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _objectBounds;
{PVCGPointQuad="a"{CGPoint="x"d"y"d}"b"{CGPoint="x"d"y"d}"c"{CGPoint="x"d"y"d}"d"{CGPoint="x"d"y"d}} _cornerPoints;
{?="columns"[4]} _transform;
{PVTransformInfo="translation""rotation"{?="vector"}"scale""shear"} _transformInfo;
```

## Properties

```
@property (T{?=qiIq},N,V_time) time;
@property (TB,N,V_forcePosterFrame) forcePosterFrame;
@property (Ti,N,V_effectOrigin) effectOrigin;
@property (T{CGSize=dd},N,V_effectSize) effectSize;
@property (Ti,N,V_origin) origin;
@property (T{CGSize=dd},N,V_relativeToSize) relativeToSize;
@property (T{PVCGPointQuad={CGPoint=dd}{CGPoint=dd}{CGPoint=dd}{CGPoint=dd}},N,V_cornerPoints) cornerPoints;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_outputROI) outputROI;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_objectBounds) objectBounds;
@property (T@"NSArray",&,N,V_hitAreaPoints) hitAreaPoints;
@property (T^{CGPath=},N,V_hitAreaPath) hitAreaPath;
@property (T^{CGPath=},N,V_expandedHitAreaPath) expandedHitAreaPath;
@property (T{?=[4]},N,V_transform) transform;
@property (T{PVTransformInfo={?=}},N,V_transformInfo) transformInfo;
@property (T@"JFXTextEffectTransforms",&,N,V_transforms) transforms;
@property (T@"NSArray",&,N,V_textFrames) textFrames;
@property (T{CGPoint=dd},R,N) center;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) viewSpaceObjectBounds;
```

## Class methods

```
+[JFXTextEffectFrame frameWithEffect:relativeToSize:origin:time:forcePosterFrame:includeDropShadow:includeTextFrames:];
```

## Instance methods

```
-[JFXTextEffectFrame origin];
-[JFXTextEffectFrame dealloc];
-[JFXTextEffectFrame setTransform:];
-[JFXTextEffectFrame transform];
-[JFXTextEffectFrame setOrigin:];
-[JFXTextEffectFrame center];
-[JFXTextEffectFrame description];
-[JFXTextEffectFrame setTime:];
-[JFXTextEffectFrame time];
-[JFXTextEffectFrame transforms];
-[JFXTextEffectFrame outputROI];
-[JFXTextEffectFrame setOutputROI:];
-[JFXTextEffectFrame objectBounds];
-[JFXTextEffectFrame setObjectBounds:];
-[JFXTextEffectFrame setTransforms:];
-[JFXTextEffectFrame setHitAreaPath:];
-[JFXTextEffectFrame cornerPoints];
-[JFXTextEffectFrame effectOrigin];
-[JFXTextEffectFrame effectSize];
-[JFXTextEffectFrame expandedHitAreaPath];
-[JFXTextEffectFrame forcePosterFrame];
-[JFXTextEffectFrame hitAreaPath];
-[JFXTextEffectFrame hitAreaPoints];
-[JFXTextEffectFrame initWithEffect:relativeToSize:origin:time:forcePosterFrame:includeDropShadow:includeTextFrames:];
-[JFXTextEffectFrame relativeToSize];
-[JFXTextEffectFrame setCornerPoints:];
-[JFXTextEffectFrame setEffectOrigin:];
-[JFXTextEffectFrame setEffectSize:];
-[JFXTextEffectFrame setExpandedHitAreaPath:];
-[JFXTextEffectFrame setForcePosterFrame:];
-[JFXTextEffectFrame setHitAreaPoints:];
-[JFXTextEffectFrame setRelativeToSize:];
-[JFXTextEffectFrame setTextFrames:];
-[JFXTextEffectFrame setTransformInfo:];
-[JFXTextEffectFrame textFrames];
-[JFXTextEffectFrame transformInfo];
-[JFXTextEffectFrame viewSpaceObjectBounds];
```
