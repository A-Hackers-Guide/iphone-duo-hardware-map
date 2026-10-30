# `_UIFloatingTabBarItemView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIFloatingTabBarContentStateProviding`
- 12 instance variables, 21 properties, 49 instance methods, 7 class methods

## Instance variables

```
B _highlighted;
B _hasSelectionHighlight;
B _editing;
B _suppressEditing;
B _suppressJiggleAnimation;
B _dragged;
@"UITab" _item;
q _preferredDisplayMode;
@"_UITabSelectionView" _backgroundView;
@"UILabel" _titleLabel;
@"UIImageView" _imageView;
@"_UIBarBadgeView" _badgeView;
```

## Properties

```
@property (T@"_UITabSelectionView",R,N,V_backgroundView) backgroundView;
@property (T@"UILabel",R,N,V_titleLabel) titleLabel;
@property (T@"UIImageView",R,N,V_imageView) imageView;
@property (T@"_UIBarBadgeView",R,N,V_badgeView) badgeView;
@property (T@"UITab",&,N,V_item) item;
@property (Tq,N,V_preferredDisplayMode) preferredDisplayMode;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TB,N,V_hasSelectionHighlight) hasSelectionHighlight;
@property (TB,N,GisEditing,V_editing) editing;
@property (TB,N,V_suppressEditing) suppressEditing;
@property (TB,N,V_suppressJiggleAnimation) suppressJiggleAnimation;
@property (Td,N) titleOpacity;
@property (Td,R,N) baselineOffsetFromTop;
@property (TB,R,N) isCustomizableItem;
@property (TB,N,GisDragged,V_dragged) dragged;
@property (TB,R,N,GisCustomizableItem) customizableItem;
@property (TB,R,N,GisDisabled) disabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIFloatingTabBarItemView _jitterRotationAnimationWithAmount:];
+[_UIFloatingTabBarItemView _jitterRotationAnimationWithStrength:];
+[_UIFloatingTabBarItemView _jitterXTranslationAnimationWithAmount:];
+[_UIFloatingTabBarItemView _jitterXTranslationAnimationWithStrength:];
+[_UIFloatingTabBarItemView _jitterYTranslationAnimationWithAmount:];
+[_UIFloatingTabBarItemView _jitterYTranslationAnimationWithStrength:];
+[_UIFloatingTabBarItemView dragPreviewForItem:userInterfaceStyle:];
```

## Instance methods

```
-[_UIFloatingTabBarItemView setTitleOpacity:];
-[_UIFloatingTabBarItemView titleOpacity];
-[_UIFloatingTabBarItemView accessibilityAttributedValue];
-[_UIFloatingTabBarItemView _currentPlatformMetrics];
-[_UIFloatingTabBarItemView accessibilityTraits];
-[_UIFloatingTabBarItemView titleLabel];
-[_UIFloatingTabBarItemView isHighlighted];
-[_UIFloatingTabBarItemView accessibilityAttributedLabel];
-[_UIFloatingTabBarItemView badgeView];
-[_UIFloatingTabBarItemView baselineOffsetFromTop];
-[_UIFloatingTabBarItemView setPreferredDisplayMode:];
-[_UIFloatingTabBarItemView setItem:];
-[_UIFloatingTabBarItemView accessibilityHint];
-[_UIFloatingTabBarItemView layoutSubviews];
-[_UIFloatingTabBarItemView _createViewHierarchy];
-[_UIFloatingTabBarItemView _updateImage];
-[_UIFloatingTabBarItemView item];
-[_UIFloatingTabBarItemView isDisabled];
-[_UIFloatingTabBarItemView sizeThatFits:];
-[_UIFloatingTabBarItemView preferredDisplayMode];
-[_UIFloatingTabBarItemView accessibilityIdentifier];
-[_UIFloatingTabBarItemView setEditing:];
-[_UIFloatingTabBarItemView setHighlighted:];
-[_UIFloatingTabBarItemView accessibilityLabel];
-[_UIFloatingTabBarItemView backgroundView];
-[_UIFloatingTabBarItemView initWithCoder:];
-[_UIFloatingTabBarItemView imageView];
-[_UIFloatingTabBarItemView isEditing];
-[_UIFloatingTabBarItemView accessibilityAttributedHint];
-[_UIFloatingTabBarItemView initWithFrame:];
-[_UIFloatingTabBarItemView setDragged:];
-[_UIFloatingTabBarItemView accessibilityValue];
-[_UIFloatingTabBarItemView _showsImageView];
-[_UIFloatingTabBarItemView suppressEditing];
-[_UIFloatingTabBarItemView _hasValidCompactRepresentation];
-[_UIFloatingTabBarItemView _imageFittingSize];
-[_UIFloatingTabBarItemView _isEffectivelyEditing];
-[_UIFloatingTabBarItemView _showsTitleLabel];
-[_UIFloatingTabBarItemView _updateFontAndColors];
-[_UIFloatingTabBarItemView _updateJigglingState];
-[_UIFloatingTabBarItemView _wantsBackground];
-[_UIFloatingTabBarItemView hasSelectionHighlight];
-[_UIFloatingTabBarItemView isCustomizableItem];
-[_UIFloatingTabBarItemView isDragged];
-[_UIFloatingTabBarItemView reloadItemView];
-[_UIFloatingTabBarItemView setHasSelectionHighlight:];
-[_UIFloatingTabBarItemView setSuppressEditing:];
-[_UIFloatingTabBarItemView setSuppressJiggleAnimation:];
-[_UIFloatingTabBarItemView suppressJiggleAnimation];
```
