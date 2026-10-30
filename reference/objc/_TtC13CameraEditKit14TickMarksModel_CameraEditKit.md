# `_TtC13CameraEditKit14TickMarksModel`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CEKTickMarksConfiguration`
- 12 instance variables, 13 properties, 31 instance methods, 0 class methods

## Instance variables

```
(objc_protocol 0x1c22b3918) ? dataSource;
(objc_protocol 0x1c22b3920) ? delegate;
_$sSu tickMarksCount;
CoreGraphics.CGFloat tickMarkSpacing;
CoreGraphics.CGFloat tickMarkWidth;
_$sSi mainTickMarkInterval;
_$sSi mainTickMarkOffset;
Swift.Bool logarithmic;
Swift.Bool endTickMarksProminent;
Swift.Bool useTickMarkLegibilityShadows;
_$sSo7UIColorCSg _primaryTickMarkColor;
_$sSo7UIColorCSg _secondaryTickMarkColor;
```

## Properties

```
@property (T@"<_TtP13CameraEditKit19TickMarksDataSource_>",N,W,VdataSource) dataSource;
@property (T@"<_TtP13CameraEditKit17TickMarksDelegate_>",N,W,Vdelegate) delegate;
@property (TQ,N,VtickMarksCount) tickMarksCount;
@property (Td,N,VtickMarkSpacing) tickMarkSpacing;
@property (Td,N,VtickMarkWidth) tickMarkWidth;
@property (Tq,N,VmainTickMarkInterval) mainTickMarkInterval;
@property (Tq,N,VmainTickMarkOffset) mainTickMarkOffset;
@property (TB,N,Vlogarithmic) logarithmic;
@property (TB,N,VendTickMarksProminent) endTickMarksProminent;
@property (TB,N,VuseTickMarkLegibilityShadows) useTickMarkLegibilityShadows;
@property (T@"UIColor",N,&) mainTickMarkColor;
@property (T@"UIColor",N,&) secondaryTickMarkColor;
@property (Td,N,R) requiredWidth;
```

## Instance methods

```
-[_TtC13CameraEditKit14TickMarksModel init];
-[_TtC13CameraEditKit14TickMarksModel setDataSource:];
-[_TtC13CameraEditKit14TickMarksModel setDelegate:];
-[_TtC13CameraEditKit14TickMarksModel dataSource];
-[_TtC13CameraEditKit14TickMarksModel delegate];
-[_TtC13CameraEditKit14TickMarksModel setMainTickMarkColor:];
-[_TtC13CameraEditKit14TickMarksModel setSecondaryTickMarkColor:];
-[_TtC13CameraEditKit14TickMarksModel setUseTickMarkLegibilityShadows:];
-[_TtC13CameraEditKit14TickMarksModel requiredWidth];
-[_TtC13CameraEditKit14TickMarksModel setMainTickMarkInterval:];
-[_TtC13CameraEditKit14TickMarksModel setTickMarkSpacing:];
-[_TtC13CameraEditKit14TickMarksModel setLogarithmic:];
-[_TtC13CameraEditKit14TickMarksModel tickMarkSpacing];
-[_TtC13CameraEditKit14TickMarksModel absoluteValueForNormalizedValue:inAbsoluteRangeSize:];
-[_TtC13CameraEditKit14TickMarksModel endTickMarksProminent];
-[_TtC13CameraEditKit14TickMarksModel floorTickMarkIndexForXOffset:];
-[_TtC13CameraEditKit14TickMarksModel isMainTickMarkAtIndex:];
-[_TtC13CameraEditKit14TickMarksModel logarithmic];
-[_TtC13CameraEditKit14TickMarksModel mainTickMarkColor];
-[_TtC13CameraEditKit14TickMarksModel mainTickMarkInterval];
-[_TtC13CameraEditKit14TickMarksModel mainTickMarkOffset];
-[_TtC13CameraEditKit14TickMarksModel secondaryTickMarkColor];
-[_TtC13CameraEditKit14TickMarksModel setEndTickMarksProminent:];
-[_TtC13CameraEditKit14TickMarksModel setMainTickMarkOffset:];
-[_TtC13CameraEditKit14TickMarksModel setTickMarkWidth:];
-[_TtC13CameraEditKit14TickMarksModel setTickMarksCount:];
-[_TtC13CameraEditKit14TickMarksModel tickMarkWidth];
-[_TtC13CameraEditKit14TickMarksModel tickMarksCount];
-[_TtC13CameraEditKit14TickMarksModel useTickMarkLegibilityShadows];
-[_TtC13CameraEditKit14TickMarksModel xOffsetForNormalizedValue:];
-[_TtC13CameraEditKit14TickMarksModel xOffsetForTickMarkIndex:];
```
