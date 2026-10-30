# `SBSwitcherAppSuggestionBannerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLPlatterView`
- 9 instance variables, 4 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"SBBestAppSuggestion" _suggestion;
@"UIView" _iconView;
@"UIView" _iconContainerView;
@"UILabel" _appLabel;
@"UILabel" _descriptionLabel;
Q _style;
B _highlighted;
@"UIView" _highlightDarkeningView;
@"NSArray" _customConstraints;
```

## Properties

```
@property (T@"NSArray",C,N,V_customConstraints) customConstraints;
@property (TB,D,N,GisHighlighted) highlighted;
@property (T@"SBBestAppSuggestion",R,N) representedAppSuggestion;
@property (TQ,R,N,V_style) style;
```

## Instance methods

```
-[SBSwitcherAppSuggestionBannerView initWithRecipe:];
-[SBSwitcherAppSuggestionBannerView didMoveToWindow];
-[SBSwitcherAppSuggestionBannerView isHighlighted];
-[SBSwitcherAppSuggestionBannerView _titleFont];
-[SBSwitcherAppSuggestionBannerView style];
-[SBSwitcherAppSuggestionBannerView setHighlighted:];
-[SBSwitcherAppSuggestionBannerView traitCollectionDidChange:];
-[SBSwitcherAppSuggestionBannerView _descriptionFont];
-[SBSwitcherAppSuggestionBannerView _textStyle];
-[SBSwitcherAppSuggestionBannerView _borderView];
-[SBSwitcherAppSuggestionBannerView _configureConstraints];
-[SBSwitcherAppSuggestionBannerView _iconImageCache];
-[SBSwitcherAppSuggestionBannerView _appTitleForSuggestion:];
-[SBSwitcherAppSuggestionBannerView _createAppLabelForSuggestion:];
-[SBSwitcherAppSuggestionBannerView _createDarkeningView];
-[SBSwitcherAppSuggestionBannerView _createDescriptionLabelForSuggestion:];
-[SBSwitcherAppSuggestionBannerView _createIconViewForSuggestion:];
-[SBSwitcherAppSuggestionBannerView _descriptionStringForSuggestion:];
-[SBSwitcherAppSuggestionBannerView _firstWakeGreetingString];
-[SBSwitcherAppSuggestionBannerView _iconImageFromAppWithBundleIdentifier:withIconImageCache:];
-[SBSwitcherAppSuggestionBannerView _iconImageViewFromAppWithBundleIdentifier:withIconImageCache:];
-[SBSwitcherAppSuggestionBannerView _isSingleLine];
-[SBSwitcherAppSuggestionBannerView _meCardShortName];
-[SBSwitcherAppSuggestionBannerView _updateAppearanceForCurrentUserInterfaceStyle];
-[SBSwitcherAppSuggestionBannerView _updateIconViewCornerRadius];
-[SBSwitcherAppSuggestionBannerView _updateIconViewImage];
-[SBSwitcherAppSuggestionBannerView _updateIconViewImageForSuggestion:];
-[SBSwitcherAppSuggestionBannerView customConstraints];
-[SBSwitcherAppSuggestionBannerView initWithFrame:appSuggestion:style:];
-[SBSwitcherAppSuggestionBannerView representedAppSuggestion];
-[SBSwitcherAppSuggestionBannerView setCustomConstraints:];
```
