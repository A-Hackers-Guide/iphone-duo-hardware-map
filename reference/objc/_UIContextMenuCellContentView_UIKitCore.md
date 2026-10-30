# `_UIContextMenuCellContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 27 instance variables, 34 properties, 110 instance methods, 0 class methods

## Instance variables

```
B _needsHoverStyleUpdate;
B _needsConstraintRebuild;
B _isEmphasized;
B _hasAttributedTitle;
@"UIImageView" _iconImageView;
@"UIButton" _accessoryButton;
Q _options;
q _selectedIconBehavior;
Q _numberOfTitleLines;
@"UIImageView" _selectionIndicatorImageView;
@"UIImageView" _childIndicatorImageView;
@"_UIKeyboardShortcutView" _keyShortcutInputView;
@"UILabel" _emphasizedTitleLabel;
@"UIImageView" _emphasizedIconImageView;
@"NSLayoutConstraint" _nonSymbolImageWidth;
@"NSLayoutConstraint" _nonSymbolImageHeight;
@"_UITextStyleDescriptor" _titleStyleDescriptor;
Q _controlState;
@"_UISlotView" _securePasteButtonSlotView;
q _overrideNumberOfTitleLines;
q _overrideNumberOfSubtitleLines;
@"<_UIContextMenuCellLayout>" _layout;
@"UIStackView" _labelStackView;
@"UILabel" _titleLabel;
@"UILabel" _subtitleLabel;
@"UISPasteVariant" _pasteVariant;
q _typeSelectState;
```

## Properties

```
@property (T@"UIImageView",&,N,V_selectionIndicatorImageView) selectionIndicatorImageView;
@property (T@"UIImageView",&,N,V_childIndicatorImageView) childIndicatorImageView;
@property (T@"_UIKeyboardShortcutView",&,N,V_keyShortcutInputView) keyShortcutInputView;
@property (T@"UILabel",&,N,V_emphasizedTitleLabel) emphasizedTitleLabel;
@property (T@"UIImageView",&,N,V_emphasizedIconImageView) emphasizedIconImageView;
@property (T@"NSLayoutConstraint",&,N,V_nonSymbolImageWidth) nonSymbolImageWidth;
@property (T@"NSLayoutConstraint",&,N,V_nonSymbolImageHeight) nonSymbolImageHeight;
@property (TB,N,V_needsHoverStyleUpdate) needsHoverStyleUpdate;
@property (TB,N,V_needsConstraintRebuild) needsConstraintRebuild;
@property (TB,N,V_isEmphasized) isEmphasized;
@property (TB,N,V_hasAttributedTitle) hasAttributedTitle;
@property (T@"_UITextStyleDescriptor",C,N,V_titleStyleDescriptor) titleStyleDescriptor;
@property (TQ,N,V_controlState) controlState;
@property (T@"_UISlotView",W,N,V_securePasteButtonSlotView) securePasteButtonSlotView;
@property (Tq,N,V_overrideNumberOfTitleLines) overrideNumberOfTitleLines;
@property (Tq,N,V_overrideNumberOfSubtitleLines) overrideNumberOfSubtitleLines;
@property (T@"<_UIContextMenuCellLayout>",R,N,V_layout) layout;
@property (T@"UIStackView",R,N,V_labelStackView) labelStackView;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (T@"UILabel",R,N,V_subtitleLabel) subtitleLabel;
@property (T@"UIView",R,N) selectionIndicatorView;
@property (T@"UIView",R,N) childIndicatorView;
@property (T@"UIView",R,N) iconView;
@property (T@"UIImageView",R,N,V_iconImageView) iconImageView;
@property (T@"UIButton",R,N,V_accessoryButton) accessoryButton;
@property (T@"UIView",R,N) keyShortcutView;
@property (TB,R,N) shouldHighlightOnHover;
@property (Tq,R,N) focusStyle;
@property (T@"UIShape",R,N) contentShape;
@property (T@"UISPasteVariant",&,N,V_pasteVariant) pasteVariant;
@property (Tq,N,GtypeSelectState,V_typeSelectState) typeSelectState;
@property (TQ,N,V_options) options;
@property (Tq,N,V_selectedIconBehavior) selectedIconBehavior;
@property (TQ,N,V_numberOfTitleLines) numberOfTitleLines;
```

## Instance methods

```
-[_UIContextMenuCellContentView subtitleLabel];
-[_UIContextMenuCellContentView didMoveToWindow];
-[_UIContextMenuCellContentView accessoryButton];
-[_UIContextMenuCellContentView setDirectionalLayoutMargins:];
-[_UIContextMenuCellContentView selectionIndicatorView];
-[_UIContextMenuCellContentView setOptions:];
-[_UIContextMenuCellContentView iconView];
-[_UIContextMenuCellContentView pasteVariant];
-[_UIContextMenuCellContentView titleLabel];
-[_UIContextMenuCellContentView setNumberOfTitleLines:];
-[_UIContextMenuCellContentView setControlState:withAnimationCoordinator:];
-[_UIContextMenuCellContentView contentShape];
-[_UIContextMenuCellContentView layoutSubviews];
-[_UIContextMenuCellContentView setLayoutClass:];
-[_UIContextMenuCellContentView setSubtitle:];
-[_UIContextMenuCellContentView _setSelectionIndicatorImage:];
-[_UIContextMenuCellContentView prepareForReuse];
-[_UIContextMenuCellContentView focusStyle];
-[_UIContextMenuCellContentView updateConstraints];
-[_UIContextMenuCellContentView layout];
-[_UIContextMenuCellContentView options];
-[_UIContextMenuCellContentView labelStackView];
-[_UIContextMenuCellContentView initWithFrame:];
-[_UIContextMenuCellContentView numberOfTitleLines];
-[_UIContextMenuCellContentView iconImageView];
-[_UIContextMenuCellContentView setImage:];
-[_UIContextMenuCellContentView _selectionImage];
-[_UIContextMenuCellContentView typeSelectState];
-[_UIContextMenuCellContentView _styledTitleForText:emphasized:];
-[_UIContextMenuCellContentView _updateAppearanceForStateChange];
-[_UIContextMenuCellContentView keyShortcutView];
-[_UIContextMenuCellContentView setSelectionIndicatorImageView:];
-[_UIContextMenuCellContentView _childIndicatorColorForCurrentState];
-[_UIContextMenuCellContentView _childIndicatorImage];
-[_UIContextMenuCellContentView _childIndicatorSymbolImageConfiguration];
-[_UIContextMenuCellContentView _contentImageViewForImage:];
-[_UIContextMenuCellContentView _createLabelStackViewIfNeeded];
-[_UIContextMenuCellContentView _decorationSymbolImageConfiguration];
-[_UIContextMenuCellContentView _hasTrailingAccessory];
-[_UIContextMenuCellContentView _hideContents];
-[_UIContextMenuCellContentView _iconSymbolConfigurationForCurrentTraitsUsingBoldFont:];
-[_UIContextMenuCellContentView _inheritRelevantPropertiesFromContentView:];
-[_UIContextMenuCellContentView _installSubtitleLabelIfNeeded];
-[_UIContextMenuCellContentView _installTitleLabelIfNeeded];
-[_UIContextMenuCellContentView _maxImageSize];
-[_UIContextMenuCellContentView _mixedSelectionImage];
-[_UIContextMenuCellContentView _primaryBackgroundColorForCurrentState];
-[_UIContextMenuCellContentView _primaryCompositingFilterForCurrentTraitsAndState];
-[_UIContextMenuCellContentView _primaryContentColorForCurrentState];
-[_UIContextMenuCellContentView _primaryContentColorShouldOverrideForCurrentState];
-[_UIContextMenuCellContentView _primaryTitleLabel];
-[_UIContextMenuCellContentView _resolvedLineLimit];
-[_UIContextMenuCellContentView _secureName];
-[_UIContextMenuCellContentView _setChildIndicatorImage:];
-[_UIContextMenuCellContentView _setNeedsConstraintRebuild];
-[_UIContextMenuCellContentView _subtitleLabelFilterForCurrentTraitsAndState];
-[_UIContextMenuCellContentView _subtitleLabelRenderingMode];
-[_UIContextMenuCellContentView _subtitleTextColor];
-[_UIContextMenuCellContentView _updateAttachedConstraintsForViewHierarchyChange];
-[_UIContextMenuCellContentView _updateCompositingFiltersForCurrentState];
-[_UIContextMenuCellContentView _updateForOptionsChangeFromPreviousOptions:];
-[_UIContextMenuCellContentView _updateHoverStyleIfNeeded];
-[_UIContextMenuCellContentView _updateIconImageAppearanceForStateChange];
-[_UIContextMenuCellContentView _updateLabelsForCurrentState];
-[_UIContextMenuCellContentView _updateSecureView];
-[_UIContextMenuCellContentView _updateSubtitleLabelNumberOfLines];
-[_UIContextMenuCellContentView _updateTitleLabelNumberOfLines];
-[_UIContextMenuCellContentView childIndicatorImageView];
-[_UIContextMenuCellContentView childIndicatorView];
-[_UIContextMenuCellContentView controlState];
-[_UIContextMenuCellContentView emphasizedIconImageView];
-[_UIContextMenuCellContentView emphasizedTitleLabel];
-[_UIContextMenuCellContentView hasAttributedTitle];
-[_UIContextMenuCellContentView isEmphasized];
-[_UIContextMenuCellContentView keyShortcutInputView];
-[_UIContextMenuCellContentView measuredNumberOfSubTitleLines];
-[_UIContextMenuCellContentView measuredNumberOfTitleLines];
-[_UIContextMenuCellContentView needsConstraintRebuild];
-[_UIContextMenuCellContentView needsHoverStyleUpdate];
-[_UIContextMenuCellContentView nonSymbolImageHeight];
-[_UIContextMenuCellContentView nonSymbolImageWidth];
-[_UIContextMenuCellContentView overrideNumberOfSubtitleLines];
-[_UIContextMenuCellContentView overrideNumberOfTitleLines];
-[_UIContextMenuCellContentView securePasteButtonSlotView];
-[_UIContextMenuCellContentView selectedIconBehavior];
-[_UIContextMenuCellContentView selectionIndicatorImageView];
-[_UIContextMenuCellContentView setAccessoryAction:];
-[_UIContextMenuCellContentView setChildIndicatorImageView:];
-[_UIContextMenuCellContentView setControlState:];
-[_UIContextMenuCellContentView setEmphasizedIconImageView:];
-[_UIContextMenuCellContentView setEmphasizedTitleLabel:];
-[_UIContextMenuCellContentView setHasAttributedTitle:];
-[_UIContextMenuCellContentView setIsEmphasized:];
-[_UIContextMenuCellContentView setKeyShortcutInputView:];
-[_UIContextMenuCellContentView setKeyboardShortcut:];
-[_UIContextMenuCellContentView setKeyboardShortcutModifiersWidth:inputWidth:];
-[_UIContextMenuCellContentView setNeedsConstraintRebuild:];
-[_UIContextMenuCellContentView setNeedsHoverStyleUpdate:];
-[_UIContextMenuCellContentView setNonSymbolImageHeight:];
-[_UIContextMenuCellContentView setNonSymbolImageWidth:];
-[_UIContextMenuCellContentView setOverrideNumberOfSubtitleLines:];
-[_UIContextMenuCellContentView setOverrideNumberOfTitleLines:];
-[_UIContextMenuCellContentView setPasteVariant:];
-[_UIContextMenuCellContentView setSecurePasteButtonSlotView:];
-[_UIContextMenuCellContentView setSelectedIconBehavior:];
-[_UIContextMenuCellContentView setTitle:attributedTitle:titleStyleDescriptor:];
-[_UIContextMenuCellContentView setTitleStyleDescriptor:];
-[_UIContextMenuCellContentView setTypeSelectState:];
-[_UIContextMenuCellContentView shouldHighlightOnHover];
-[_UIContextMenuCellContentView titleStyleDescriptor];
```
