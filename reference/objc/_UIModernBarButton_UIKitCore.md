# `_UIModernBarButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIButton`
- Protocols: `_UIButtonBarButtonAppearance`
- 6 instance variables, 6 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _guardAgainstDegenerateBaselineCalculation;
B _shouldUseButtonPlatters;
B _enableMonochromaticTreatmentOnImageAndTitle;
B _usesTintColorCapsuleForSelection;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} __additionalSelectionInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _selectionIndicatorViewFrame;
```

## Properties

```
@property (TB,N,S_setGuardAgainstDegenerateBaselineCalculation:) _guardAgainstDegenerateBaselineCalculation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_selectionIndicatorViewFrame) selectionIndicatorViewFrame;
@property (TB,N,V_usesTintColorCapsuleForSelection) usesTintColorCapsuleForSelection;
@property (TB,N,V_shouldUseButtonPlatters) shouldUseButtonPlatters;
@property (TB,N,V_enableMonochromaticTreatmentOnImageAndTitle) enableMonochromaticTreatmentOnImageAndTitle;
@property (T{UIEdgeInsets=dddd},N,S_setAdditionalSelectionInsets:,V__additionalSelectionInsets) _additionalSelectionInsets;
```

## Class methods

```
+[_UIModernBarButton _visualProviderClassForIdiom:];
```

## Instance methods

```
-[_UIModernBarButton _shouldAdjustToTraitCollection];
-[_UIModernBarButton didMoveToWindow];
-[_UIModernBarButton selectionIndicatorViewFrame];
-[_UIModernBarButton setShouldUseButtonPlatters:];
-[_UIModernBarButton _setAdditionalSelectionInsets:];
-[_UIModernBarButton _guardAgainstDegenerateBaselineCalculation];
-[_UIModernBarButton usesTintColorCapsuleForSelection];
-[_UIModernBarButton _roundSize:];
-[_UIModernBarButton _selectedIndicatorBounds];
-[_UIModernBarButton _setGuardAgainstDegenerateBaselineCalculation:];
-[_UIModernBarButton _registerForTraitChangeNotifications];
-[_UIModernBarButton _likelyToHaveTitle];
-[_UIModernBarButton setEnableMonochromaticTreatmentOnImageAndTitle:];
-[_UIModernBarButton _selectedIndicatorViewWithImage:];
-[_UIModernBarButton _updateMonochromaticTreatment];
-[_UIModernBarButton initWithCoder:];
-[_UIModernBarButton setUsesTintColorCapsuleForSelection:];
-[_UIModernBarButton _supportsMacIdiom];
-[_UIModernBarButton setSelectionIndicatorViewFrame:];
-[_UIModernBarButton _setupForUseAsImageButton];
-[_UIModernBarButton _additionalSelectionInsets];
-[_UIModernBarButton enableMonochromaticTreatmentOnImageAndTitle];
-[_UIModernBarButton initWithFrame:];
-[_UIModernBarButton contentRectForBounds:];
-[_UIModernBarButton shouldUseButtonPlatters];
```
