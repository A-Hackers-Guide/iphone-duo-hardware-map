# `_TtCO5UIKit14IntelligenceUI15PromptEntryView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_TtP5UIKit22UITextEffectViewSource_`, `UITextViewDelegate`
- 39 instance variables, 1 properties, 23 instance methods, 0 class methods

## Instance variables

```
_$sSSSg placeholder;
UIKit.IntelligenceUI.PromptEntryView.PlaceholderConfiguration placeholderConfiguration;
UIKit.IntelligenceUI.PromptEntryView.Delegate ? delegate;
_$sSo10UITextViewC textView;
_$sSo6UIViewCSg accessoryView;
UIKit.IntelligenceUI.PromptEntryView.ReturnKeyBehavior returnBehavior;
SX_px5BoundSXRts_XP _$sSiXjSg visibleLineLimit;
_$sSiSg characterLimit;
_$sSo8UIButtonC leadingButton;
Swift.Bool isLeadingButtonVisible;
_$sSo8UIButtonC trailingButton;
Swift.Bool isTrailingButtonVisible;
Swift.Bool trailingButtonHiddenWhenEmpty;
Swift.Bool trailingButtonShowsClearButtonWhenNotEmpty;
Swift.Bool isLeadingButtonConfiguredAsToggle;
Swift.Bool leadingButtonToggleState;
UIKit.UIPromptBackgroundView ? $__lazy_storage_$_backgroundView;
__C.UIEdgeInsets textViewPadding;
Swift.Bool isPonderingEffectEnabled;
Foundation.AttributeContainer styleAttributesForAmbiguity;
Foundation.AttributeContainer styleAttributesForResolvedAmbiguity;
UIKit.IntelligenceUI.PromptEntryView.PrivatePressGestureRecognizerDelegate _privatePressGestureRecognizerDelegate;
_$sSo7UILabelC placeholderLabel;
_$sSo6UIViewC accessorySeparatorView;
_$sSo12UIScrollViewC containerScrollView;
_$sSo23_UITouchPassthroughViewC buttonContainerView;
_$sSo18UIVisualEffectViewC placeholderEffectView;
UIKit.UITextEffectView ? $__lazy_storage_$_ponderingEffectView;
UIKit.UIPromptBackgroundView.Configuration ? nonPonderingBackgroundStyle;
UIKit.UITextEffectView.EffectID ? activePonderEffect;
_$sSo6UIViewCSg $__lazy_storage_$_accessoryContainerView;
_$sSo12_UIShapeViewCSg $__lazy_storage_$_accessoryContainerMaskView;
Swift.Bool _trailingButtonActivatesDictationWhenEmpty;
_$sSD -> UIKit.IntelligenceUI.PromptAmbiguityID UIKit.IntelligenceUI.PromptEntryView.AmbiguityData ambiguitiesByID;
_$sSD -> UIKit.IntelligenceUI.PromptAmbiguityID UIKit.IntelligenceUI.PromptEntryView.ImageAttributesState imageAttributeStates;
_$sSD -> UIKit.IntelligenceUI.PromptAmbiguityID UIKit.IntelligenceUI.PromptEntryView.AmbiguityAppearanceConfiguration customConfigurations;
Swift.Bool needsStyleUpdate;
_$sSo25_UIPressGestureRecognizerC modifierKeyRecognizer;
UIKit.UIPromptBackgroundView.CornerRadius backgroundCornerRadius;
```

## Properties

```
@property (T{CGSize=dd},N,R) intrinsicContentSize;
```

## Instance methods

```
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView canGenerateTargetedPreviewsWithCompletionHandler:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView systemLayoutSizeFittingSize:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView intrinsicContentSize];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView targetedPreviewFor:completionHandler:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView _textView:insertTextSuggestion:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView updateTextChunkVisibilityForAnimation:visible:completionHandler:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView buildMenuWithBuilder:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textViewDidChange:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView layoutSubviews];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView hitTest:withEvent:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textViewDidEndEditing:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView updatedTargetedPreviewGeometryFor:previous:completionHandler:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView sizeThatFits:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textView:menuConfigurationForTextItem:defaultMenu:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textViewDidBeginEditing:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView canGenerateTargetedPreviewForChunk:completionHandler:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView initWithCoder:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textView:shouldChangeTextInRange:replacementText:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView initWithFrame:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textViewDidChangeSelection:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView dictationAvailabilityDidChange];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView promptBackgroundViewDidUpdateConfiguration:];
-[_TtCO5UIKit14IntelligenceUI15PromptEntryView textViewShouldBeginEditing:];
```
