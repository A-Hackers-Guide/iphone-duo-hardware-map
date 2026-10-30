# `CAMMultiCamPIPMetrics`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 9 instance methods, 0 class methods

## Instance variables

```
d _cornerRadius;
d _borderWidth;
^{CGColor=} _borderColor;
q _videoResolution;
{?="value"q"timescale"i"flags"I"epoch"q} _timestamp;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T{?=qiIq},R,N,V_timestamp) timestamp;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_frame) frame;
@property (Td,R,N,V_cornerRadius) cornerRadius;
@property (Td,R,N,V_borderWidth) borderWidth;
@property (T^{CGColor=},R,N,V_borderColor) borderColor;
@property (Tq,R,N,V_videoResolution) videoResolution;
```

## Instance methods

```
-[CAMMultiCamPIPMetrics videoResolution];
-[CAMMultiCamPIPMetrics timestamp];
-[CAMMultiCamPIPMetrics borderWidth];
-[CAMMultiCamPIPMetrics cornerRadius];
-[CAMMultiCamPIPMetrics borderColor];
-[CAMMultiCamPIPMetrics frame];
-[CAMMultiCamPIPMetrics frameInCoreImageLandscapeCoordinateSpace];
-[CAMMultiCamPIPMetrics initWithTimestamp:frame:cornerRadius:borderWidth:borderColor:videoResolution:];
-[CAMMultiCamPIPMetrics timeStampInSeconds];
```
