# `CEKSliderTickMarksView`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_TtP13CameraEditKit19TickMarksDataSource_`, `_TtP13CameraEditKit17TickMarksDelegate_`, `CEKTickMarksContainer`
- 3 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<CEKSliderTickMarksDelegate>" _delegate;
@"_TtC13CameraEditKit14TickMarksModel" _tickMarksModel;
@"NSArray" _tickColorGradient;
```

## Properties

```
@property (T@"NSArray",C,N,V_tickColorGradient) tickColorGradient;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (T{UIEdgeInsets=dddd},R,N) alignmentRectInsets;
@property (T@"<CEKSliderTickMarksDelegate>",W,N,V_delegate) delegate;
@property (T@"_TtC13CameraEditKit14TickMarksModel",R,N,V_tickMarksModel) tickMarksModel;
```

## Instance methods

```
-[CEKSliderTickMarksView tickMarksModelDidChangeAppearanceWithModel:];
-[CEKSliderTickMarksView alignmentRectInsets];
-[CEKSliderTickMarksView drawRect:];
-[CEKSliderTickMarksView tickMarksModelDidChangeWidthForTickMarkCountWithModel:];
-[CEKSliderTickMarksView setDelegate:];
-[CEKSliderTickMarksView setTickColorGradient:];
-[CEKSliderTickMarksView delegate];
-[CEKSliderTickMarksView tickColorGradient];
-[CEKSliderTickMarksView frameForTickMarkAtIndex:];
-[CEKSliderTickMarksView initWithFrame:];
-[CEKSliderTickMarksView tickMarksModel];
-[CEKSliderTickMarksView _shadowWidth];
-[CEKSliderTickMarksView _shadowFrameForTickMarkRect:];
```
