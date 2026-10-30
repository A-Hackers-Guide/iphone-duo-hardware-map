# `_UIButtonBarButtonVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 10 properties, 62 instance methods, 2 class methods

## Instance variables

```
@"_UIButtonBarButton" _button;
@"UIBarButtonItem" _barButtonItem;
@"UIColor" _tintColor;
@"_UITypedStorage" __typedStorage;
```

## Properties

```
@property (T@"UIBarButtonItem",R,W) barButtonItem;
@property (T@"_UIButtonBarButton",R,N) button;
@property (T@"UIView",R,N) backIndicatorView;
@property (T@"UIView",R,N) contentView;
@property (TB,N) backButtonConstraintsActive;
@property (TB,N) backButtonMaskEnabled;
@property (T@"UIColor",C,N,V_tintColor) tintColor;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) accessoryViewAlignmentRect;
@property (T@"UIView",R,N) alignmentViewForStaticNavBarButtonLeading;
@property (T@"UIView",R,N) alignmentViewForStaticNavBarButtonTrailing;
```

## Class methods

```
+[_UIButtonBarButtonVisualProvider registerPlatformVisualProviderClass:forIdiom:];
+[_UIButtonBarButtonVisualProvider visualProviderForIdiom:];
```

## Instance methods

```
-[_UIButtonBarButtonVisualProvider backButtonConstraintsActive];
-[_UIButtonBarButtonVisualProvider buttonHeldState:forRequestedState:];
-[_UIButtonBarButtonVisualProvider buttonIntrinsicContentSize:];
-[_UIButtonBarButtonVisualProvider buttonSpringLoadedInteractionBehavior];
-[_UIButtonBarButtonVisualProvider buttonSelectionState:forRequestedState:];
-[_UIButtonBarButtonVisualProvider buttonWillMoveToSuperview:];
-[_UIButtonBarButtonVisualProvider buttonDidUpdateBoundsSize];
-[_UIButtonBarButtonVisualProvider buttonContextMenuStyleFromDefaultStyle:];
-[_UIButtonBarButtonVisualProvider accessoryViewAlignmentRect];
-[_UIButtonBarButtonVisualProvider buttonControlClass];
-[_UIButtonBarButtonVisualProvider updateButton:forSelectedState:];
-[_UIButtonBarButtonVisualProvider updateButton:forHighlightedState:];
-[_UIButtonBarButtonVisualProvider updateButton:appearance:];
-[_UIButtonBarButtonVisualProvider pointerPreviewCenter];
-[_UIButtonBarButtonVisualProvider updateButton:forEnabledState:];
-[_UIButtonBarButtonVisualProvider updateMenu];
-[_UIButtonBarButtonVisualProvider buttonImageViewSize:];
-[_UIButtonBarButtonVisualProvider shouldSuppressPointerSpecularFilter];
-[_UIButtonBarButtonVisualProvider buttonAlignmentRectInsets:];
-[_UIButtonBarButtonVisualProvider canUpdateMenuInPlace];
-[_UIButtonBarButtonVisualProvider updateButton:forHeldState:];
-[_UIButtonBarButtonVisualProvider pointerShapeInContainer:];
-[_UIButtonBarButtonVisualProvider buttonContextMenuTargetedPreview];
-[_UIButtonBarButtonVisualProvider symbolImageView];
-[_UIButtonBarButtonVisualProvider resetButtonHasHighlighted];
-[_UIButtonBarButtonVisualProvider pointerWillExit:];
-[_UIButtonBarButtonVisualProvider buttonLayoutSubviews:baseImplementation:];
-[_UIButtonBarButtonVisualProvider updateImage];
-[_UIButtonBarButtonVisualProvider matchingPointerShapeForView:rect:inContainer:];
-[_UIButtonBarButtonVisualProvider alignmentViewForStaticNavBarButtonLeading];
-[_UIButtonBarButtonVisualProvider supportsBackButtons];
-[_UIButtonBarButtonVisualProvider buttonWillMoveToWindow:];
-[_UIButtonBarButtonVisualProvider shouldLift];
-[_UIButtonBarButtonVisualProvider setBackButtonMaskEnabled:];
-[_UIButtonBarButtonVisualProvider buttonContextMenuInteractionConfiguration];
-[_UIButtonBarButtonVisualProvider buttonHighlitedState:forRequestedState:];
-[_UIButtonBarButtonVisualProvider alignmentViewForStaticNavBarButtonTrailing];
-[_UIButtonBarButtonVisualProvider menuAnchorPoint];
-[_UIButtonBarButtonVisualProvider configureButton:withAppearanceDelegate:fromBarItem:];
-[_UIButtonBarButtonVisualProvider backButtonSystemLayoutSizeFittingSize:horizontalFittingPriority:verticalFittingPriority:];
-[_UIButtonBarButtonVisualProvider focusEffect];
-[_UIButtonBarButtonVisualProvider buttonEnabledState:forRequestedState:];
-[_UIButtonBarButtonVisualProvider buttonSpringLoadedInteractionEffect];
-[_UIButtonBarButtonVisualProvider backIndicatorView];
-[_UIButtonBarButtonVisualProvider barButtonItem];
-[_UIButtonBarButtonVisualProvider traitDependenciesUpdated];
-[_UIButtonBarButtonVisualProvider updateButton:forFocusedState:];
-[_UIButtonBarButtonVisualProvider buttonBarButtonClass];
-[_UIButtonBarButtonVisualProvider backButtonMaskEnabled];
-[_UIButtonBarButtonVisualProvider pointerPreviewParameters];
-[_UIButtonBarButtonVisualProvider buttonBackgroundSize:];
-[_UIButtonBarButtonVisualProvider setBackButtonConstraintsActive:];
-[_UIButtonBarButtonVisualProvider updateButton:toUseButtonShapes:];
-[_UIButtonBarButtonVisualProvider button];
-[_UIButtonBarButtonVisualProvider reload];
-[_UIButtonBarButtonVisualProvider pointerWillEnter:];
-[_UIButtonBarButtonVisualProvider setTintColor:];
-[_UIButtonBarButtonVisualProvider contentView];
-[_UIButtonBarButtonVisualProvider hash];
-[_UIButtonBarButtonVisualProvider tintColor];
-[_UIButtonBarButtonVisualProvider copyWithZone:];
-[_UIButtonBarButtonVisualProvider isEqual:];
```
