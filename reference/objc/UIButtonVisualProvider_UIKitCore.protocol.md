# `UIButtonVisualProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 73 instance methods, 3 class methods

## Properties

```
@property (Td,N) focusSizeIncrease;
@property (T@"UIButton",?,N) button;
@property (TB,?,N) avoidDefaultTitleAndImageLayout;
```

## Class methods

```
+[UIButtonVisualProvider requiresNewVisualProviderForChanges];
+[UIButtonVisualProvider visualProviderForButton:];
+[UIButtonVisualProvider shouldUpdateContextMenuEnabledOnMenuChanges];
```

## Instance methods

```
-[UIButtonVisualProvider useTitleForSelectedIndicatorBounds];
-[UIButtonVisualProvider setContentVerticalAlignment:];
-[UIButtonVisualProvider focusSizeIncrease];
-[UIButtonVisualProvider setFocusSizeIncrease:];
-[UIButtonVisualProvider setSelected:];
-[UIButtonVisualProvider adjustsFontForContentSizeCategory];
-[UIButtonVisualProvider contentBackdropView];
-[UIButtonVisualProvider contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[UIButtonVisualProvider selectionIndicatorView];
-[UIButtonVisualProvider pointerEffectPreviewParameters];
-[UIButtonVisualProvider pointerWillExit:];
-[UIButtonVisualProvider cleanupForVisualProvider:];
-[UIButtonVisualProvider contextMenuInteraction:configurationForMenuAtLocation:];
-[UIButtonVisualProvider defaultFocusEffect];
-[UIButtonVisualProvider effectiveContentView];
-[UIButtonVisualProvider didUpdateFocusInContext:withAnimationCoordinator:];
-[UIButtonVisualProvider alignmentRectInsets];
-[UIButtonVisualProvider setShowsTouchWhenHighlighted:];
-[UIButtonVisualProvider setContextMenuIsPrimary:];
-[UIButtonVisualProvider setHighlighted:animated:];
-[UIButtonVisualProvider contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[UIButtonVisualProvider imageRectForContentRect:];
-[UIButtonVisualProvider menuAttachmentPointForConfiguration:];
-[UIButtonVisualProvider viewForLastBaselineLayout];
-[UIButtonVisualProvider layoutSubviews];
-[UIButtonVisualProvider imageViewCreateIfNeeded:];
-[UIButtonVisualProvider setPreferredSymbolConfiguration:forImageInState:];
-[UIButtonVisualProvider baselineOffsetsAtSize:];
-[UIButtonVisualProvider updateProperties];
-[UIButtonVisualProvider canBecomeFocused];
-[UIButtonVisualProvider visualBoundsWithCornerRadius:];
-[UIButtonVisualProvider intrinsicContentSizeInvalidatedForChildView:];
-[UIButtonVisualProvider setSemanticContentAttribute:];
-[UIButtonVisualProvider pointerWillEnter:];
-[UIButtonVisualProvider pointerEffectWithPreview:];
-[UIButtonVisualProvider setMenuProvider:];
-[UIButtonVisualProvider tintColorDidChange];
-[UIButtonVisualProvider willMoveToWindow:];
-[UIButtonVisualProvider preferredConfigurationForFocusAnimation:inContext:];
-[UIButtonVisualProvider imageEffectContainerView];
-[UIButtonVisualProvider setEnabled:];
-[UIButtonVisualProvider viewForFirstBaselineLayout];
-[UIButtonVisualProvider setAttributedTitle:forState:];
-[UIButtonVisualProvider updatedAppliedCornerRadius:];
-[UIButtonVisualProvider titleViewCreateIfNeeded:];
-[UIButtonVisualProvider updatedAppliedCornersAreContinuous:];
-[UIButtonVisualProvider setTitle:forState:];
-[UIButtonVisualProvider setImage:forState:];
-[UIButtonVisualProvider setOn:];
-[UIButtonVisualProvider setRole:];
-[UIButtonVisualProvider backgroundViewCreateIfNeeded:];
-[UIButtonVisualProvider preferredHoverEffect];
-[UIButtonVisualProvider updateConstraints];
-[UIButtonVisualProvider traitCollectionDidChange:];
-[UIButtonVisualProvider isOn];
-[UIButtonVisualProvider intrinsicSizeWithinSize:];
-[UIButtonVisualProvider pointerShapeInContainer:proposal:];
-[UIButtonVisualProvider touchesBegan];
-[UIButtonVisualProvider setReversesTitleShadowWhenHighlighted:];
-[UIButtonVisualProvider preferredHoverShape];
-[UIButtonVisualProvider touchesEnded];
-[UIButtonVisualProvider didChangeFromIdiom:onScreen:traverseHierarchy:];
-[UIButtonVisualProvider titleRectForContentRect:];
-[UIButtonVisualProvider setControlEvent:];
-[UIButtonVisualProvider setContentHorizontalAlignment:];
-[UIButtonVisualProvider contentRectForBounds:];
-[UIButtonVisualProvider setContentHuggingPriorities:];
-[UIButtonVisualProvider contextMenuInteraction:updateStyleForMenuWithConfiguration:style:];
-[UIButtonVisualProvider setMenu:];
-[UIButtonVisualProvider avoidDefaultTitleAndImageLayout];
-[UIButtonVisualProvider setButton:];
-[UIButtonVisualProvider button];
-[UIButtonVisualProvider setAvoidDefaultTitleAndImageLayout:];
```
