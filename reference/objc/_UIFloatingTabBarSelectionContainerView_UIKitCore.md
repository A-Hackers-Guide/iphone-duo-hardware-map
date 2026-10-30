# `_UIFloatingTabBarSelectionContainerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 6 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"UIView" _selectionView;
@"UIViewFloatAnimatableProperty" _targetPosition;
@"_UILiquidLensView" _liquidLensView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _selectionViewBounds;
```

## Properties

```
@property (T@"_UILiquidLensView",R,N,V_liquidLensView) liquidLensView;
@property (T{CGPoint=dd},N) selectionViewPosition;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_selectionViewBounds) selectionViewBounds;
@property (T@"UIView",R,N,V_selectionView) selectionView;
@property (T@"UIView",&,N) liftedContentView;
@property (T@"UIViewFloatAnimatableProperty",R,N,V_targetPosition) targetPosition;
```

## Instance methods

```
-[_UIFloatingTabBarSelectionContainerView setLiftedContentView:];
-[_UIFloatingTabBarSelectionContainerView selectionView];
-[_UIFloatingTabBarSelectionContainerView liftedContentView];
-[_UIFloatingTabBarSelectionContainerView initWithFrame:];
-[_UIFloatingTabBarSelectionContainerView _shouldScalePlatter];
-[_UIFloatingTabBarSelectionContainerView _updateSelectionViewBounds];
-[_UIFloatingTabBarSelectionContainerView liquidLensView];
-[_UIFloatingTabBarSelectionContainerView selectionViewBounds];
-[_UIFloatingTabBarSelectionContainerView selectionViewFrame];
-[_UIFloatingTabBarSelectionContainerView selectionViewPosition];
-[_UIFloatingTabBarSelectionContainerView setSelectionViewBounds:];
-[_UIFloatingTabBarSelectionContainerView setSelectionViewPosition:];
-[_UIFloatingTabBarSelectionContainerView targetPosition];
```
