# `SBAsymmetricalCornerRadiusWrapperView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHitTestExtendedView`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSCornerRadiusConfiguration" _cornerRadiusConfiguration;
Q _maskedCorners;
@"SBHitTestExtendedView" _trailingCornersMaskingView;
```

## Properties

```
@property (T@"BSCornerRadiusConfiguration",&,N,V_cornerRadiusConfiguration) cornerRadiusConfiguration;
@property (TQ,N,V_maskedCorners) maskedCorners;
@property (T@"NSArray",R,C,N) contentViews;
```

## Instance methods

```
-[SBAsymmetricalCornerRadiusWrapperView setClipsToBounds:];
-[SBAsymmetricalCornerRadiusWrapperView _updateCornerRadius];
-[SBAsymmetricalCornerRadiusWrapperView cornerRadiusConfiguration];
-[SBAsymmetricalCornerRadiusWrapperView contentViews];
-[SBAsymmetricalCornerRadiusWrapperView bringContentViewToFront:];
-[SBAsymmetricalCornerRadiusWrapperView setCornerRadiusConfiguration:];
-[SBAsymmetricalCornerRadiusWrapperView maskedCorners];
-[SBAsymmetricalCornerRadiusWrapperView addContentView:];
-[SBAsymmetricalCornerRadiusWrapperView sendContentViewToBack:];
-[SBAsymmetricalCornerRadiusWrapperView setMaskedCorners:];
-[SBAsymmetricalCornerRadiusWrapperView initWithFrame:];
-[SBAsymmetricalCornerRadiusWrapperView _updateMaskedCorners];
```
