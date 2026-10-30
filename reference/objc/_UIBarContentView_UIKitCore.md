# `_UIBarContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIButtonBarAppearanceDelegate`
- 4 instance variables, 19 properties, 39 instance methods, 0 class methods

## Instance variables

```
B _centerTextButtons;
# _appearanceGuideClass;
@"_UIBarButtonItemAppearanceStorage" _appearanceStorage;
@"UIImage" _backIndicatorMaskImage;
```

## Properties

```
@property (T@"_UIBarButtonItemAppearanceStorage",R,N,V_appearanceStorage) appearanceStorage;
@property (Tq,R,N) barType;
@property (TB,R,N) compactMetrics;
@property (TB,N,V_centerTextButtons) centerTextButtons;
@property (T@"UIImage",&,N) backIndicatorImage;
@property (T@"UIImage",&,N,V_backIndicatorMaskImage) backIndicatorMaskImage;
@property (T#,&,N,S_setAppearanceGuideClass:,V_appearanceGuideClass) _appearanceGuideClass;
@property (T@"UIColor",R,D,N) tintColor;
@property (Td,R,N) defaultEdgeSpacing;
@property (Td,R,N) defaultTextPadding;
@property (Td,R,N) backButtonMargin;
@property (Td,R,N) backButtonMaximumWidth;
@property (T@"UIImageSymbolConfiguration",?,R,N) imageSymbolConfiguration;
@property (TB,?,R,N) _useLeadingAlignedTitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Instance methods

```
-[_UIBarContentView _UIAppearance_setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIBarContentView setBackIndicatorImage:];
-[_UIBarContentView edgesPaddingBarButtonItem:];
-[_UIBarContentView _setAppearanceGuideClass:];
-[_UIBarContentView _UIAppearance_setBackButtonBackgroundImage:forState:barMetrics:];
-[_UIBarContentView _titleTextAttributesForState:];
-[_UIBarContentView _UIAppearance_setTitleTextAttributes:forState:];
-[_UIBarContentView _setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIBarContentView _setTintColor:];
-[_UIBarContentView _appearanceGuideClass];
-[_UIBarContentView backIndicatorMaskImage];
-[_UIBarContentView _setTitleTextAttributes:forState:];
-[_UIBarContentView _edgesPropagatingSafeAreaInsetsToSubviews];
-[_UIBarContentView setBackIndicatorMaskImage:];
-[_UIBarContentView _setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UIBarContentView _UIAppearance_setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIBarContentView appearanceStorage];
-[_UIBarContentView _UIAppearance_setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UIBarContentView _UIAppearance_setTintColor:];
-[_UIBarContentView setCenterTextButtons:];
-[_UIBarContentView _UIAppearance_setBackgroundImage:forState:style:barMetrics:];
-[_UIBarContentView _UIAppearance_setTitlePositionAdjustment:forBarMetrics:];
-[_UIBarContentView absorptionForItem:];
-[_UIBarContentView _appearanceChanged];
-[_UIBarContentView _setBackgroundImage:forState:barMetrics:];
-[_UIBarContentView _UIAppearance_setBackgroundImage:forState:barMetrics:];
-[_UIBarContentView _setBackButtonBackgroundImage:forState:barMetrics:];
-[_UIBarContentView backButtonMargin];
-[_UIBarContentView _setBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIBarContentView _setTitlePositionAdjustment:forBarMetrics:];
-[_UIBarContentView _setBackgroundImage:forState:style:barMetrics:];
-[_UIBarContentView centerTextButtons];
-[_UIBarContentView defaultEdgeSpacing];
-[_UIBarContentView defaultTextPadding];
-[_UIBarContentView backIndicatorImage];
-[_UIBarContentView initWithFrame:];
-[_UIBarContentView barType];
-[_UIBarContentView compactMetrics];
-[_UIBarContentView backButtonMaximumWidth];
```
