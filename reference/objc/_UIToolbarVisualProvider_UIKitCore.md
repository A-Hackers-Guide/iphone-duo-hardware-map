# `_UIToolbarVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 9 properties, 34 instance methods, 1 class methods

## Instance variables

```
@"UIToolbar" _toolbar;
@"UIView" _customBackgroundView;
@"UIView" _currentBackgroundView;
```

## Properties

```
@property (T@"UIToolbar",R,N,V_toolbar) toolbar;
@property (T@"UIView",&,N,V_customBackgroundView) customBackgroundView;
@property (T@"UIView",R,N,V_currentBackgroundView) currentBackgroundView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) backgroundFrame;
@property (TB,R,N) toolbarIsSmall;
@property (Tq,N) itemDistribution;
@property (Td,D,N) backgroundTransitionProgress;
@property (TB,N) useModernAppearance;
@property (T@"<_UIBarAppearanceChangeObserver>",R,N) appearanceObserver;
```

## Class methods

```
+[_UIToolbarVisualProvider shouldDecodeSubviews];
```

## Instance methods

```
-[_UIToolbarVisualProvider toolbar];
-[_UIToolbarVisualProvider setUseModernAppearance:];
-[_UIToolbarVisualProvider updateWithItems:fromOldItems:animate:];
-[_UIToolbarVisualProvider useModernAppearance];
-[_UIToolbarVisualProvider setBackgroundTransitionProgress:];
-[_UIToolbarVisualProvider setCustomBackgroundView:];
-[_UIToolbarVisualProvider backgroundTransitionProgress];
-[_UIToolbarVisualProvider setItemDistribution:];
-[_UIToolbarVisualProvider startInteractiveTransition];
-[_UIToolbarVisualProvider itemDistribution];
-[_UIToolbarVisualProvider updateBackgroundGroupName];
-[_UIToolbarVisualProvider toolbarIsSmall];
-[_UIToolbarVisualProvider layoutSubviews];
-[_UIToolbarVisualProvider updateBarForStyle:];
-[_UIToolbarVisualProvider updateInteractiveTransitionWithProgress:];
-[_UIToolbarVisualProvider traitCollectionForChild:baseTraitCollection:];
-[_UIToolbarVisualProvider backgroundFrame];
-[_UIToolbarVisualProvider finishInteractiveTransition];
-[_UIToolbarVisualProvider defaultSizeForOrientation:];
-[_UIToolbarVisualProvider customBackgroundView];
-[_UIToolbarVisualProvider currentBackgroundView];
-[_UIToolbarVisualProvider initWithToolbar:];
-[_UIToolbarVisualProvider updateBarBackground];
-[_UIToolbarVisualProvider appearanceObserver];
-[_UIToolbarVisualProvider updateAppearance];
-[_UIToolbarVisualProvider prepare];
-[_UIToolbarVisualProvider updateBarBackgroundSize];
-[_UIToolbarVisualProvider edgesPropagatingSafeAreaInsetsToSubviews];
-[_UIToolbarVisualProvider contentViewMargins];
-[_UIToolbarVisualProvider updateArchivedSubviews:];
-[_UIToolbarVisualProvider customViewChangedForButtonItem:];
-[_UIToolbarVisualProvider drawBackgroundViewInRect:];
-[_UIToolbarVisualProvider positionToolbarButtonsAndResetFontScaleAdjustment:];
-[_UIToolbarVisualProvider updateItemsForNewFrame:];
```
