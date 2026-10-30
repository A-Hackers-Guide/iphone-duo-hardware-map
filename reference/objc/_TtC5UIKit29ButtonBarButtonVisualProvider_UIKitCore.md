# `_TtC5UIKit29ButtonBarButtonVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarButtonVisualProvider`
- 21 instance variables, 7 properties, 41 instance methods, 0 class methods

## Instance variables

```
_$sSDySSSo18NSLayoutConstraintCG currentConstraints;
_$sSDySSSo18NSLayoutConstraintCG oldConstraints;
UIKit.ButtonBarButtonVisualProvider.Button ? backIndicatorButton;
UIKit.ButtonBarButtonVisualProvider.BackButtonMaskView ? backButtonMask;
UIKit.ButtonBarButtonVisualProvider.Button ? titleButton;
UIKit.ButtonBarButtonVisualProvider.Button ? imageButton;
_$sSo11UIImageViewCSg backgroundView;
UIKit.ButtonBarButtonVisualProvider.TitleAttributes ? barButtonTitleAttributes;
UIKit.ButtonBarButtonVisualProvider.TitleAttributes ? finalTitleAttributes;
UIKit.ButtonBarButtonVisualProvider.BackgroundImages backgroundImages;
_$sSa -> UIKit.ButtonBarButtonVisualProvider.TitleContent titleContent;
_$sSDySS UIKit.ButtonBarButtonVisualProvider.TitleContent titleLookup;
_$sSo18NSLayoutConstraintCSg backButtonTitleMaxWidthConstraint;
_$sSo6UIMenuCSgSaySo0A7ElementCGcSg menuProvider;
__C.SystemItem systemItem;
(objc_protocol 0x186445840) ? appearanceDelegate;
Swift.Bool imageHasBaseline;
Swift.Bool _backButtonMaskEnabled;
__C.Style style;
Swift.Bool isSystemItem;
_$sSd backButtonContentTrailingPadding;
```

## Properties

```
@property (T@"UIColor",N,&) tintColor;
@property (TB,N) backButtonMaskEnabled;
@property (T@"UIView",N,R) backIndicatorView;
@property (T@"UIView",N,R) contentView;
@property (T@"UIView",N,R) alignmentViewForStaticNavBarButtonLeading;
@property (T@"UIView",N,R) alignmentViewForStaticNavBarButtonTrailing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,R) accessoryViewAlignmentRect;
```

## Instance methods

```
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonSelectionState:forRequestedState:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonDidUpdateBoundsSize];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonContextMenuStyleFromDefaultStyle:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider accessoryViewAlignmentRect];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonControlClass];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:forSelectedState:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:forHighlightedState:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:appearance:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:forEnabledState:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateMenu];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonImageViewSize:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider canUpdateMenuInPlace];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:forHeldState:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider pointerShapeInContainer:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonContextMenuTargetedPreview];
-[_TtC5UIKit29ButtonBarButtonVisualProvider symbolImageView];
-[_TtC5UIKit29ButtonBarButtonVisualProvider resetButtonHasHighlighted];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonLayoutSubviews:baseImplementation:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateImage];
-[_TtC5UIKit29ButtonBarButtonVisualProvider matchingPointerShapeForView:rect:inContainer:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider alignmentViewForStaticNavBarButtonLeading];
-[_TtC5UIKit29ButtonBarButtonVisualProvider supportsBackButtons];
-[_TtC5UIKit29ButtonBarButtonVisualProvider shouldLift];
-[_TtC5UIKit29ButtonBarButtonVisualProvider setBackButtonMaskEnabled:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider init];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonContextMenuInteractionConfiguration];
-[_TtC5UIKit29ButtonBarButtonVisualProvider alignmentViewForStaticNavBarButtonTrailing];
-[_TtC5UIKit29ButtonBarButtonVisualProvider menuAnchorPoint];
-[_TtC5UIKit29ButtonBarButtonVisualProvider configureButton:withAppearanceDelegate:fromBarItem:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider backButtonSystemLayoutSizeFittingSize:horizontalFittingPriority:verticalFittingPriority:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider buttonSpringLoadedInteractionEffect];
-[_TtC5UIKit29ButtonBarButtonVisualProvider backIndicatorView];
-[_TtC5UIKit29ButtonBarButtonVisualProvider traitDependenciesUpdated];
-[_TtC5UIKit29ButtonBarButtonVisualProvider backButtonMaskEnabled];
-[_TtC5UIKit29ButtonBarButtonVisualProvider pointerPreviewParameters];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateButton:toUseButtonShapes:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider reload];
-[_TtC5UIKit29ButtonBarButtonVisualProvider setTintColor:];
-[_TtC5UIKit29ButtonBarButtonVisualProvider contentView];
-[_TtC5UIKit29ButtonBarButtonVisualProvider tintColor];
-[_TtC5UIKit29ButtonBarButtonVisualProvider updateTextContent];
```
