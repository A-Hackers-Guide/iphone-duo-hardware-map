# `CUIRenditionSliceInformation`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
q _renditionType;
[4d] _boundaries;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _destinationRect;
{?="top"d"left"d"bottom"d"right"d} _edgeInsets;
```

## Properties

```
@property (Tq,R,N,V_renditionType) renditionType;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_destinationRect) destinationRect;
@property (T{?=dddd},R,N,V_edgeInsets) edgeInsets;
```

## Instance methods

```
-[CUIRenditionSliceInformation _bottomRightCapSize];
-[CUIRenditionSliceInformation _topLeftCapSize];
-[CUIRenditionSliceInformation renditionType];
-[CUIRenditionSliceInformation initWithSliceInformation:destinationRect:];
-[CUIRenditionSliceInformation description];
-[CUIRenditionSliceInformation initWithRenditionType:destinationRect:topLeftInset:bottomRightInset:];
-[CUIRenditionSliceInformation edgeInsets];
-[CUIRenditionSliceInformation positionOfSliceBoundary:];
-[CUIRenditionSliceInformation copyWithZone:];
-[CUIRenditionSliceInformation destinationRect];
```
