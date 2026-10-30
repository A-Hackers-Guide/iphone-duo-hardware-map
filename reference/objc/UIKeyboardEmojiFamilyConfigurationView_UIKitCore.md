# `UIKeyboardEmojiFamilyConfigurationView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIKBKeyViewContentView`
- 15 instance variables, 18 properties, 49 instance methods, 2 class methods

## Instance variables

```
d _metachronalRhythmAnimationStartTime;
B _usesDarkStyle;
B _hasSplitFontSupport;
@"UIView" _touchForwardingView;
@"NSMutableArray" _familyMemberStackViews;
@"UIView" _separatorView;
@"UIStackView" _previewWellStackView;
@"UIKeyboardEmojiWellView" _neutralWellView;
@"UIKeyboardEmojiWellView" _configuredWellView;
@"NSIndexPath" _lastSelectedIndexPath;
@"NSString" _baseEmojiString;
@"NSMutableArray" _selectedVariantIndices;
@"NSArray" _skinToneVariantRows;
@"NSArray" _variantDisplayRows;
@"UIKBTree" _representedKey;
```

## Properties

```
@property (TB,N,V_usesDarkStyle) usesDarkStyle;
@property (T@"NSMutableArray",&,N,V_familyMemberStackViews) familyMemberStackViews;
@property (T@"UIView",&,N,V_separatorView) separatorView;
@property (T@"UIStackView",&,N,V_previewWellStackView) previewWellStackView;
@property (T@"UIKeyboardEmojiWellView",&,N,V_neutralWellView) neutralWellView;
@property (T@"UIKeyboardEmojiWellView",&,N,V_configuredWellView) configuredWellView;
@property (T@"NSIndexPath",&,N,V_lastSelectedIndexPath) lastSelectedIndexPath;
@property (T@"NSString",&,N,V_baseEmojiString) baseEmojiString;
@property (T@"NSMutableArray",&,N,V_selectedVariantIndices) selectedVariantIndices;
@property (T@"NSArray",&,N,V_skinToneVariantRows) skinToneVariantRows;
@property (T@"NSArray",&,N,V_variantDisplayRows) variantDisplayRows;
@property (T@"UIKBTree",&,N,V_representedKey) representedKey;
@property (TB,N,V_hasSplitFontSupport) hasSplitFontSupport;
@property (T@"UIView",&,N,V_touchForwardingView) touchForwardingView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKeyboardEmojiFamilyConfigurationView _selectionAndSeparatorColorForDarkMode:];
+[UIKeyboardEmojiFamilyConfigurationView preferredContentViewSizeForKey:withTraits:];
```

## Instance methods

```
-[UIKeyboardEmojiFamilyConfigurationView retestSelectedVariantIndexForKey:atPoint:phase:];
-[UIKeyboardEmojiFamilyConfigurationView updateForKeyplane:key:];
-[UIKeyboardEmojiFamilyConfigurationView representedKey];
-[UIKeyboardEmojiFamilyConfigurationView layoutSubviews];
-[UIKeyboardEmojiFamilyConfigurationView selectedVariantIndices];
-[UIKeyboardEmojiFamilyConfigurationView setRepresentedKey:];
-[UIKeyboardEmojiFamilyConfigurationView setSeparatorView:];
-[UIKeyboardEmojiFamilyConfigurationView separatorView];
-[UIKeyboardEmojiFamilyConfigurationView nextResponder];
-[UIKeyboardEmojiFamilyConfigurationView setSelectedVariantIndices:];
-[UIKeyboardEmojiFamilyConfigurationView initWithFrame:];
-[UIKeyboardEmojiFamilyConfigurationView baseEmojiString];
-[UIKeyboardEmojiFamilyConfigurationView neutralWellView];
-[UIKeyboardEmojiFamilyConfigurationView _backgroundColorForSelection];
-[UIKeyboardEmojiFamilyConfigurationView _beginFamilyMetachronalRhythmAnimation];
-[UIKeyboardEmojiFamilyConfigurationView _colorConfigurationDidChange];
-[UIKeyboardEmojiFamilyConfigurationView _configureFamilyMemberWellStackViews];
-[UIKeyboardEmojiFamilyConfigurationView _configureSkinToneVariantSpecifiersForBaseString:];
-[UIKeyboardEmojiFamilyConfigurationView _currentlySelectedSkinToneConfiguration];
-[UIKeyboardEmojiFamilyConfigurationView _hasCompletelyConfiguredSkinToneConfiguration];
-[UIKeyboardEmojiFamilyConfigurationView _setCurrentlySelectedSkinToneConfiguration:];
-[UIKeyboardEmojiFamilyConfigurationView _silhouetteFromCurrentSelections];
-[UIKeyboardEmojiFamilyConfigurationView _updateBottomRowForSelections:];
-[UIKeyboardEmojiFamilyConfigurationView _updatePreviewWellForCurrentSelection];
-[UIKeyboardEmojiFamilyConfigurationView _updateReferencedKeySelectedVariantIndexBasedOnCurrentConfiguration];
-[UIKeyboardEmojiFamilyConfigurationView _wellViewForSection:item:];
-[UIKeyboardEmojiFamilyConfigurationView configuredWellView];
-[UIKeyboardEmojiFamilyConfigurationView familyMemberStackViews];
-[UIKeyboardEmojiFamilyConfigurationView hasSplitFontSupport];
-[UIKeyboardEmojiFamilyConfigurationView lastSelectedIndexPath];
-[UIKeyboardEmojiFamilyConfigurationView previewWellStackView];
-[UIKeyboardEmojiFamilyConfigurationView retestForTouchUpSelectedVariantIndexForKey:atPoint:];
-[UIKeyboardEmojiFamilyConfigurationView retestSelectedVariantIndexForKey:atPoint:];
-[UIKeyboardEmojiFamilyConfigurationView setBaseEmojiString:];
-[UIKeyboardEmojiFamilyConfigurationView setConfiguredWellView:];
-[UIKeyboardEmojiFamilyConfigurationView setFamilyMemberStackViews:];
-[UIKeyboardEmojiFamilyConfigurationView setHasSplitFontSupport:];
-[UIKeyboardEmojiFamilyConfigurationView setLastSelectedIndexPath:];
-[UIKeyboardEmojiFamilyConfigurationView setNeutralWellView:];
-[UIKeyboardEmojiFamilyConfigurationView setPreviewWellStackView:];
-[UIKeyboardEmojiFamilyConfigurationView setSkinToneVariantRows:];
-[UIKeyboardEmojiFamilyConfigurationView setTouchForwardingView:];
-[UIKeyboardEmojiFamilyConfigurationView setUsesDarkStyle:];
-[UIKeyboardEmojiFamilyConfigurationView setVariantDisplayRows:];
-[UIKeyboardEmojiFamilyConfigurationView skinToneVariantRows];
-[UIKeyboardEmojiFamilyConfigurationView touchForwardingView];
-[UIKeyboardEmojiFamilyConfigurationView updateRenderConfig:];
-[UIKeyboardEmojiFamilyConfigurationView usesDarkStyle];
-[UIKeyboardEmojiFamilyConfigurationView variantDisplayRows];
```
