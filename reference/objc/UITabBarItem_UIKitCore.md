# `UITabBarItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIBarItem`
- Protocols: `_UIPopoverPresentationControllerSourceItem_Internal`, `_UIBarAppearanceChangeObserver`, `_UITabDataProvider`
- 28 instance variables, 29 properties, 107 instance methods, 1 class methods

## Instance variables

```
@"NSString" _title;
: _action;
@ _target;
@"UIImage" _templateImage;
@"UIImage" _selectedTemplateImage;
@"UIImage" _selectedImage;
@"UIImage" _unselectedImage;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _imageInsets;
@"UIImage" _landscapeTemplateImage;
@"UIImage" _landscapeSelectedTemplateImage;
@"UIImage" _landscapeSelectedImage;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _landscapeImageInsets;
@"NSString" _badgeValue;
{UIOffset="horizontal"d"vertical"d} _badgeOffset;
@"UIControl<_UITabBarButton>" _view;
@"_UITabBarItemAppearanceStorage" _appearanceStorage;
{?="enabled"b1"springLoaded"b1"style"b3"isSystemItem"b1"systemItem"b4"selected"b1"customSelectedImage"b1"customUnselectedImage"b1} _tabBarItemFlags;
@? _alternateUpdateHandler;
B __prominentItem;
B __usesModernAppearance;
B __pinned;
@"UITabBarAppearance" _scrollEdgeAppearance;
@"<_UITabChangeObserver>" _changeObserver;
@"UITabBarAppearance" _standardAppearance;
q __barMetrics;
q __imageStyle;
@"UIColor" __tintColor;
@"<_UIPopoverPresentationControllerSourceItem_Internal>" __fallbackSourceItem;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UITabBarItemAppearanceStorage",R,N) _appearanceStorage;
@property (Tq,N,S_setBarMetrics:,V__barMetrics) _barMetrics;
@property (Tq,N,S_setImageStyle:,V__imageStyle) _imageStyle;
@property (T@"UIColor",&,N,S_setTintColor:,V__tintColor) _tintColor;
@property (TB,N,G_isSelected,S_setSelected:) _selected;
@property (T@"UIImage",R,N) _internalLandscapeSelectedImagePhone;
@property (TB,N,S_setUsesModernAppearance:,V__usesModernAppearance) _usesModernAppearance;
@property (TB,N,G_isPinned,S_setPinned:,V__pinned) _pinned;
@property (T@"UIImage",&,N) landscapeSelectedImagePhone;
@property (T{UIOffset=dd},N) badgeOffset;
@property (T{UIOffset=dd},N) landscapePhoneBadgeOffset;
@property (T@"UIImage",&,N) selectedImage;
@property (T@"NSString",C,N,V_badgeValue) badgeValue;
@property (T{UIOffset=dd},N) titlePositionAdjustment;
@property (T@"UIColor",C,N) badgeColor;
@property (T@"UITabBarAppearance",C,N,V_standardAppearance) standardAppearance;
@property (T@"UITabBarAppearance",C,N,V_scrollEdgeAppearance) scrollEdgeAppearance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisEnabled) enabled;
@property (TB,R,N,GisSelected) seleted;
@property (TB,R,N,GisSpringLoaded) springLoaded;
@property (Tq,R,N) preferredPlacement;
```

## Class methods

```
+[UITabBarItem _appearanceBlindViewClasses];
```

## Instance methods

```
-[UITabBarItem setSpringLoaded:];
-[UITabBarItem _setImageStyle:];
-[UITabBarItem _tintColor];
-[UITabBarItem _imageStyle];
-[UITabBarItem setScrollEdgeAppearance:];
-[UITabBarItem _setBarMetrics:];
-[UITabBarItem _appearanceStorage];
-[UITabBarItem scrollEdgeAppearance];
-[UITabBarItem badgeValue];
-[UITabBarItem _updateView];
-[UITabBarItem _internalTemplateImagesForTabBarDisplayStyle:];
-[UITabBarItem setStandardAppearance:];
-[UITabBarItem setBadgeValue:];
-[UITabBarItem isSpringLoaded];
-[UITabBarItem setLargeContentSizeImage:];
-[UITabBarItem isSystemItem];
-[UITabBarItem standardAppearance];
-[UITabBarItem badgeTextAttributesForState:];
-[UITabBarItem _barMetrics];
-[UITabBarItem appearance:categoriesChanged:];
-[UITabBarItem _setSelected:];
-[UITabBarItem landscapeImagePhone];
-[UITabBarItem landscapePhoneBadgeOffset];
-[UITabBarItem initWithTabBarSystemItem:tag:];
-[UITabBarItem systemItem];
-[UITabBarItem setBadgeTextAttributes:forState:];
-[UITabBarItem resolvedTitle];
-[UITabBarItem _setTintColor:];
-[UITabBarItem _isPinned];
-[UITabBarItem setTitlePositionAdjustment:];
-[UITabBarItem init];
-[UITabBarItem badgeColor];
-[UITabBarItem _internalTitleForTabBarDisplayStyle:];
-[UITabBarItem animatedBadge];
-[UITabBarItem unselectedImage];
-[UITabBarItem imageForStyle:state:];
-[UITabBarItem setUnselectedImage:];
-[UITabBarItem _nearestViewController];
-[UITabBarItem _updateViewAndPositionItems:];
-[UITabBarItem _frameInCoordinateSpace:window:];
-[UITabBarItem setView:];
-[UITabBarItem setAction:];
-[UITabBarItem action];
-[UITabBarItem largeContentSizeImageInsets];
-[UITabBarItem _setInternalTitle:];
-[UITabBarItem setFinishedSelectedImage:withFinishedUnselectedImage:];
-[UITabBarItem _prefersZoomTransitionsForPopoverPresentationController:];
-[UITabBarItem setTitleTextAttributes:forState:];
-[UITabBarItem badgeForStyle:state:];
-[UITabBarItem _sourceRectForPresentationInWindow:];
-[UITabBarItem _sourceViewForPresentationInWindow:];
-[UITabBarItem setAnimatedBadge:];
-[UITabBarItem isEnabled];
-[UITabBarItem _internalLargeContentSizeImage];
-[UITabBarItem view];
-[UITabBarItem finishedSelectedImage];
-[UITabBarItem initWithTitle:image:tag:];
-[UITabBarItem initWithTitle:image:selectedImage:];
-[UITabBarItem _internalTemplateImage];
-[UITabBarItem _internalTemplateImages];
-[UITabBarItem _usesModernAppearance];
-[UITabBarItem title];
-[UITabBarItem setEnabled:];
-[UITabBarItem setTarget:];
-[UITabBarItem landscapeSelectedImagePhone];
-[UITabBarItem titleTextAttributesForState:];
-[UITabBarItem _internalLandscapeTemplateImage];
-[UITabBarItem selectedImage];
-[UITabBarItem encodeWithCoder:];
-[UITabBarItem isSelected];
-[UITabBarItem _updateViewBadge];
-[UITabBarItem setImageInsets:];
-[UITabBarItem _setPinned:];
-[UITabBarItem _internalTitle];
-[UITabBarItem setLandscapeImagePhone:];
-[UITabBarItem largeContentSizeImage];
-[UITabBarItem _setUsesModernAppearance:];
-[UITabBarItem imageInsetsForStyle:state:];
-[UITabBarItem description];
-[UITabBarItem landscapeImagePhoneInsets];
-[UITabBarItem setBadgeOffset:];
-[UITabBarItem _createViewForTabBar:asProxyView:];
-[UITabBarItem _internalLandscapeSelectedImagePhone];
-[UITabBarItem setLandscapeImagePhoneInsets:];
-[UITabBarItem initWithCoder:];
-[UITabBarItem setTitle:];
-[UITabBarItem imageInsets];
-[UITabBarItem setSelectedImage:];
-[UITabBarItem image];
-[UITabBarItem target];
-[UITabBarItem _setInternalTemplateImage:];
-[UITabBarItem titleForStyle:state:];
-[UITabBarItem setBadgeColor:];
-[UITabBarItem setLandscapePhoneBadgeOffset:];
-[UITabBarItem _setInternalLandscapeTemplateImage:];
-[UITabBarItem preferredPlacement];
-[UITabBarItem setLandscapeSelectedImagePhone:];
-[UITabBarItem _internalLandscapeTemplateImages];
-[UITabBarItem hasTitle];
-[UITabBarItem titlePositionAdjustment];
-[UITabBarItem frameInView:];
-[UITabBarItem badgeOffset];
-[UITabBarItem _setTitleTextAttributeValue:forAttributeKey:state:];
-[UITabBarItem finishedUnselectedImage];
-[UITabBarItem setLargeContentSizeImageInsets:];
-[UITabBarItem _isSelected];
-[UITabBarItem setImage:];
```
