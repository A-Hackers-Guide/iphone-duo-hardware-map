# `UISegmentedControlTVGlassStyleProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISegmentedControlTVStyleProvider`
- Protocols: `UISegmentedControlGlassStyleProvider`
- 1 instance variables, 40 properties, 23 instance methods, 7 class methods

## Instance variables

```
@"UIView" _backdropView;
```

## Properties

```
@property (T@"UIView",&,N,V_backdropView) backdropView;
@property (TB,R,N) alwaysUseConcentricCornerRadius;
@property (T@"<_UIViewMaterial>",R,N) backgroundMaterial;
@property (Td,R,N) defaultHeightWithBackgroundMaterial;
@property (T@"UIFont",R,N) fontWithBackgroundMaterial;
@property (TB,R,N) useLensView;
@property (TB,R,N) useC2Animation;
@property (TB,R,N) allowFreeSelectionSliding;
@property (TB,R,N) useGeneratedImages;
@property (TB,R,N) useSelectionIndicatorStyling;
@property (TB,R,N) animateSlidingSelectionByDefault;
@property (TB,R,N) useTVStyleFocusSelection;
@property (Td,R,N) defaultContentPaddingWidth;
@property (Td,R,N) defaultTextContentPaddingWidth;
@property (Td,R,N) segmentSelectionScaleFactor;
@property (Td,R,N) segmentHidingFinalScaleFactor;
@property (TB,R,N) limitInternalLayoutAndInteractionToDefaultHeight;
@property (TB,R,N) hasTransparentBackgroundByDefault;
@property (T@"UIColor",R,N) defaultBackgroundTintColor;
@property (TB,R,N) supportsDynamicTypeByDefault;
@property (TB,R,N) supportsAXPopover;
@property (Td,R,N) defaultInterSegmentSpacing;
@property (T@"UIVibrancyEffect",R,N) selectedSegmentDefaultVibrancyEffect;
@property (T@"UIBlurEffect",R,N) selectedSegmentDefaultBlurEffect;
@property (T@"UIVibrancyEffect",R,N) selectedSegmentContentDefaultVibrancyEffect;
@property (T@"UIVibrancyEffect",R,N) unselectedSegmentContentDefaultVibrancyEffect;
@property (TB,R,N) hasShadowWithSelectedSegmentEffect;
@property (Td,R,N) mostlyInsideMargin;
@property (TB,R,N) usesContinuousCurveCorners;
@property (TB,?,R,N) wantsFocusWithoutSelection;
@property (TB,?,R,N) shouldHideSelectionOnFocusUpdate;
@property (TB,?,R,N) animateHighlightingSelectionByDefault;
@property (T@"UIVibrancyEffect",?,R,N) highlightedSegmentDefaultVibrancyEffect;
@property (TB,?,R,N) apportionsSegmentWidthsByContentByDefault;
@property (T@"UIBlurEffect",?,R,N) backgroundBlurEffect;
@property (TB,?,R,N) disablePointerEffects;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorDisabledSelected];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorDisabledUserInterfaceStyleDark];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorDisabledUserInterfaceStyleLight];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorFocused];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorNormalUserInterfaceStyleDark];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorNormalUserInterfaceStyleLight];
+[UISegmentedControlTVGlassStyleProvider _tvDefaultTextColorSelected];
```

## Instance methods

```
-[UISegmentedControlTVGlassStyleProvider setBackdropView:];
-[UISegmentedControlTVGlassStyleProvider backdropView];
-[UISegmentedControlTVGlassStyleProvider backgroundMaterial];
-[UISegmentedControlTVGlassStyleProvider segmentSelectionScaleFactor];
-[UISegmentedControlTVGlassStyleProvider highlightColorForSegmentSelected:highlighted:traitCollection:tintColor:];
-[UISegmentedControlTVGlassStyleProvider selectionIndicatorInsetWithMaterialForControlSize:];
-[UISegmentedControlTVGlassStyleProvider fontColorForSegment:enabled:selected:state:];
-[UISegmentedControlTVGlassStyleProvider usesContinuousCurveCorners];
-[UISegmentedControlTVGlassStyleProvider alwaysUseConcentricCornerRadius];
-[UISegmentedControlTVGlassStyleProvider fontWithBackgroundMaterial];
-[UISegmentedControlTVGlassStyleProvider useC2Animation];
-[UISegmentedControlTVGlassStyleProvider useLensView];
-[UISegmentedControlTVGlassStyleProvider selectionIndicatorInsetForControlSize:];
-[UISegmentedControlTVGlassStyleProvider defaultHeightForControlSize:traitCollection:];
-[UISegmentedControlTVGlassStyleProvider allowFreeSelectionSliding];
-[UISegmentedControlTVGlassStyleProvider defaultHeightWithBackgroundMaterial];
-[UISegmentedControlTVGlassStyleProvider createBackdropView];
-[UISegmentedControlTVGlassStyleProvider animateSlidingSelectionByDefault];
-[UISegmentedControlTVGlassStyleProvider segmentHidingFinalScaleFactor];
-[UISegmentedControlTVGlassStyleProvider selectedSegmentCompositingModeForTraitCollection:];
-[UISegmentedControlTVGlassStyleProvider shouldHideSelectionOnFocusUpdate];
-[UISegmentedControlTVGlassStyleProvider useGeneratedImages];
-[UISegmentedControlTVGlassStyleProvider useSelectionIndicatorStyling];
```
