# `_UIButtonBarButtonVisualProviderCarPlay`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarButtonVisualProvider`
- 10 instance variables, 10 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"<_UIButtonBarAppearanceDelegate>" _appearanceDelegate;
@"UIView" _focusedView;
@"UIImageView" _backView;
@"UIImageView" _imageView;
@"UILabel" _titleView;
@"NSArray" _titleAlternatives;
@"NSMutableDictionary" _titleAlterntativeLookup;
@"NSArray" _buttonConstraints;
@"NSLayoutConstraint" _maxTitleViewWidthConstraint;
@"NSLayoutConstraint" _backViewToContentConstraint;
```

## Properties

```
@property (T@"<_UIButtonBarAppearanceDelegate>",W,N,V_appearanceDelegate) appearanceDelegate;
@property (T@"UIView",&,N,V_focusedView) focusedView;
@property (T@"UIImageView",&,N,V_backView) backView;
@property (T@"UIImageView",&,N,V_imageView) imageView;
@property (T@"UILabel",&,N,V_titleView) titleView;
@property (T@"NSArray",&,N,V_titleAlternatives) titleAlternatives;
@property (T@"NSMutableDictionary",&,N,V_titleAlterntativeLookup) titleAlterntativeLookup;
@property (T@"NSArray",&,N,V_buttonConstraints) buttonConstraints;
@property (T@"NSLayoutConstraint",&,N,V_maxTitleViewWidthConstraint) maxTitleViewWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_backViewToContentConstraint) backViewToContentConstraint;
```

## Instance methods

```
-[_UIButtonBarButtonVisualProviderCarPlay setTitleView:];
-[_UIButtonBarButtonVisualProviderCarPlay updateButton:forHighlightedState:];
-[_UIButtonBarButtonVisualProviderCarPlay updateButton:forEnabledState:];
-[_UIButtonBarButtonVisualProviderCarPlay _setupAlternateTitlesFromBarButtonItem:];
-[_UIButtonBarButtonVisualProviderCarPlay buttonLayoutSubviews:baseImplementation:];
-[_UIButtonBarButtonVisualProviderCarPlay supportsBackButtons];
-[_UIButtonBarButtonVisualProviderCarPlay configureButton:fromBarButtonItem:];
-[_UIButtonBarButtonVisualProviderCarPlay focusedView];
-[_UIButtonBarButtonVisualProviderCarPlay configureButton:withAppearanceDelegate:fromBarItem:];
-[_UIButtonBarButtonVisualProviderCarPlay setImageView:];
-[_UIButtonBarButtonVisualProviderCarPlay setMaxTitleViewWidthConstraint:];
-[_UIButtonBarButtonVisualProviderCarPlay backIndicatorView];
-[_UIButtonBarButtonVisualProviderCarPlay _effectiveEdgeSpacing];
-[_UIButtonBarButtonVisualProviderCarPlay updateButton:forFocusedState:];
-[_UIButtonBarButtonVisualProviderCarPlay _updateLabelColorsForStateEnabled:focused:pressed:];
-[_UIButtonBarButtonVisualProviderCarPlay setButtonConstraints:];
-[_UIButtonBarButtonVisualProviderCarPlay titleAlternatives];
-[_UIButtonBarButtonVisualProviderCarPlay backView];
-[_UIButtonBarButtonVisualProviderCarPlay setTitleAlterntativeLookup:];
-[_UIButtonBarButtonVisualProviderCarPlay titleAlterntativeLookup];
-[_UIButtonBarButtonVisualProviderCarPlay _titleAlternativeForTitle:];
-[_UIButtonBarButtonVisualProviderCarPlay contentView];
-[_UIButtonBarButtonVisualProviderCarPlay backViewToContentConstraint];
-[_UIButtonBarButtonVisualProviderCarPlay setAppearanceDelegate:];
-[_UIButtonBarButtonVisualProviderCarPlay setTitleAlternatives:];
-[_UIButtonBarButtonVisualProviderCarPlay maxTitleViewWidthConstraint];
-[_UIButtonBarButtonVisualProviderCarPlay titleView];
-[_UIButtonBarButtonVisualProviderCarPlay buttonConstraints];
-[_UIButtonBarButtonVisualProviderCarPlay imageView];
-[_UIButtonBarButtonVisualProviderCarPlay appearanceDelegate];
-[_UIButtonBarButtonVisualProviderCarPlay setBackView:];
-[_UIButtonBarButtonVisualProviderCarPlay setBackViewToContentConstraint:];
-[_UIButtonBarButtonVisualProviderCarPlay setFocusedView:];
```
