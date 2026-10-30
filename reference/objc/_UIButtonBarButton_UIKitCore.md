# `_UIButtonBarButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `_UISelectionInteractionDelegate`, `UIPointerInteractionDelegate`, `UISpringLoadedInteractionSupporting`
- 18 instance variables, 22 properties, 87 instance methods, 1 class methods

## Instance variables

```
@"_UIButtonBarButtonVisualProvider" _visualProvider;
@"NSLayoutConstraint" _widthMinimizingConstraint;
@"NSLayoutConstraint" _heightMinimizingConstraint;
B _autolayoutIsCleanForBoundsChange;
@"NSDate" _appearanceDate;
B _acceptsInauthenticTouches;
B _hasPerformedPostConfigurationLayout;
B _backButton;
B _breadcrumb;
B _verticallyCentersContents;
B _usesAdjustedTintColorWhenItemPrefersFilledAppearance;
B _shouldUseButtonPlatters;
B _isSingleItemInSectionWithPlatter;
B _hasBackgroundPlatter;
B _usesTintColorCapsuleForSelection;
@"_UIBarButtonItemData" _appearanceData;
q _preferredMenuElementOrder;
@"_UISelectionInteraction" __selectionInteraction;
```

## Properties

```
@property (T@"_UISelectionInteraction",&,N,V__selectionInteraction) _selectionInteraction;
@property (TB,N,V_usesTintColorCapsuleForSelection) usesTintColorCapsuleForSelection;
@property (T@"_UIButtonBarButtonVisualProvider",R,C,N,V_visualProvider) visualProvider;
@property (TB,R,N,GisBackButton,V_backButton) backButton;
@property (TB,R,N,GisBreadcrumb,V_breadcrumb) breadcrumb;
@property (TB,N,V_verticallyCentersContents) verticallyCentersContents;
@property (TB,N) backButtonMaskEnabled;
@property (TB,N,V_usesAdjustedTintColorWhenItemPrefersFilledAppearance) usesAdjustedTintColorWhenItemPrefersFilledAppearance;
@property (T@"_UIBarButtonItemData",&,N,V_appearanceData) appearanceData;
@property (T@"NSLayoutConstraint",R,N) widthMinimizingConstraint;
@property (T@"NSLayoutConstraint",R,N) heightMinimizingConstraint;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _buttonBarHitRect;
@property (Tq,N,V_preferredMenuElementOrder) preferredMenuElementOrder;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) accessoryViewAlignmentRect;
@property (TB,N,V_shouldUseButtonPlatters) shouldUseButtonPlatters;
@property (TB,N,V_isSingleItemInSectionWithPlatter) isSingleItemInSectionWithPlatter;
@property (TB,N,V_hasBackgroundPlatter) hasBackgroundPlatter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisSpringLoaded) springLoaded;
```

## Class methods

```
+[_UIButtonBarButton shouldUseMonochromeTreatmentWithCustomTintColor];
```

## Instance methods

```
-[_UIButtonBarButton _controlEventsForActionTriggered];
-[_UIButtonBarButton setSpringLoaded:];
-[_UIButtonBarButton setPreferredMenuElementOrder:];
-[_UIButtonBarButton visualProvider];
-[_UIButtonBarButton isSpringLoaded];
-[_UIButtonBarButton accessoryViewAlignmentRect];
-[_UIButtonBarButton setSelected:];
-[_UIButtonBarButton contextMenuInteraction:previewForDismissingMenuWithConfiguration:];
-[_UIButtonBarButton setShouldUseButtonPlatters:];
-[_UIButtonBarButton intrinsicContentSize];
-[_UIButtonBarButton willMoveToSuperview:];
-[_UIButtonBarButton pointerInteraction:styleForRegion:];
-[_UIButtonBarButton contextMenuInteraction:configurationForMenuAtLocation:];
-[_UIButtonBarButton setBackButtonMaskEnabled:];
-[_UIButtonBarButton init];
-[_UIButtonBarButton usesTintColorCapsuleForSelection];
-[_UIButtonBarButton backButtonSystemLayoutSizeFittingSize:horizontalFittingPriority:verticalFittingPriority:];
-[_UIButtonBarButton focusEffect];
-[_UIButtonBarButton didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIButtonBarButton alignmentRectInsets];
-[_UIButtonBarButton pointerInteraction:willEnterRegion:animator:];
-[_UIButtonBarButton pointerInteraction:willExitRegion:animator:];
-[_UIButtonBarButton backgroundSize];
-[_UIButtonBarButton traitDependenciesUpdated];
-[_UIButtonBarButton backButtonMaskEnabled];
-[_UIButtonBarButton dealloc];
-[_UIButtonBarButton contextMenuInteraction:previewForHighlightingMenuWithConfiguration:];
-[_UIButtonBarButton menuAttachmentPointForConfiguration:];
-[_UIButtonBarButton layoutSubviews];
-[_UIButtonBarButton setBounds:];
-[_UIButtonBarButton _preferredSender];
-[_UIButtonBarButton gestureRecognizerShouldBegin:];
-[_UIButtonBarButton setHighlighted:];
-[_UIButtonBarButton willMoveToWindow:];
-[_UIButtonBarButton setEnabled:];
-[_UIButtonBarButton removeAllSymbolEffectsWithOptions:animated:];
-[_UIButtonBarButton encodeWithCoder:];
-[_UIButtonBarButton pointerInteraction:regionForRequest:defaultRegion:];
-[_UIButtonBarButton setFrame:];
-[_UIButtonBarButton description];
-[_UIButtonBarButton initWithCoder:];
-[_UIButtonBarButton preferredMenuElementOrder];
-[_UIButtonBarButton setUsesTintColorCapsuleForSelection:];
-[_UIButtonBarButton initWithFrame:];
-[_UIButtonBarButton _contextMenuInteraction:styleForMenuWithConfiguration:];
-[_UIButtonBarButton shouldUseButtonPlatters];
-[_UIButtonBarButton _targetedPreviewForInteraction:];
-[_UIButtonBarButton _selectionInteractionDidSelect:];
-[_UIButtonBarButton applyContentTransition:options:];
-[_UIButtonBarButton _acceptsInauthenticTouches];
-[_UIButtonBarButton _accessibilitySettingsChanged:];
-[_UIButtonBarButton _accessibilityShouldActivateOnHUDLift];
-[_UIButtonBarButton _applyDeferredSymbolEffects];
-[_UIButtonBarButton _buttonBarHitRect];
-[_UIButtonBarButton _configureFromBarItem:appearanceDelegate:isBackButton:useBreadcrumbStyle:];
-[_UIButtonBarButton _is_setNeedsLayout];
-[_UIButtonBarButton _selectionInteraction];
-[_UIButtonBarButton _selectionInteractionDidBeginHinting:];
-[_UIButtonBarButton _selectionInteractionDidCancelHinting:];
-[_UIButtonBarButton _setHasActiveMenuPresentation:];
-[_UIButtonBarButton _setTouchHasHighlighted:];
-[_UIButtonBarButton addSymbolEffect:options:animated:];
-[_UIButtonBarButton appearanceData];
-[_UIButtonBarButton configureBackButtonFromBarItem:withAppearanceDelegate:];
-[_UIButtonBarButton configureBreadcrumbBackButtonFromBarItem:withAppearanceDelegate:];
-[_UIButtonBarButton configureFromBarItem:withAppearanceDelegate:];
-[_UIButtonBarButton hasBackgroundPlatter];
-[_UIButtonBarButton heightMinimizingConstraint];
-[_UIButtonBarButton imageViewSize];
-[_UIButtonBarButton initWithVisualProvider:];
-[_UIButtonBarButton isBackButton];
-[_UIButtonBarButton isBreadcrumb];
-[_UIButtonBarButton isSingleItemInSectionWithPlatter];
-[_UIButtonBarButton pasteTouchDown];
-[_UIButtonBarButton pointMostlyInside:withEvent:];
-[_UIButtonBarButton removeSymbolEffectOfType:options:animated:];
-[_UIButtonBarButton setAppearanceData:];
-[_UIButtonBarButton setHasBackgroundPlatter:];
-[_UIButtonBarButton setIsSingleItemInSectionWithPlatter:];
-[_UIButtonBarButton setNeedsAppearanceUpdate];
-[_UIButtonBarButton setUsesAdjustedTintColorWhenItemPrefersFilledAppearance:];
-[_UIButtonBarButton setVerticallyCentersContents:];
-[_UIButtonBarButton set_selectionInteraction:];
-[_UIButtonBarButton updatePresentedMenuFrom:];
-[_UIButtonBarButton usesAdjustedTintColorWhenItemPrefersFilledAppearance];
-[_UIButtonBarButton verticallyCentersContents];
-[_UIButtonBarButton widthMinimizingConstraint];
```
