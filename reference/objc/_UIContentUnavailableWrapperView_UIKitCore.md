# `_UIContentUnavailableWrapperView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITouchPassthroughView`
- 7 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIView" _contentView;
@"UIView" _backgroundView;
@"UIView<_UIContentViewInternal>" _viewForConfiguration;
@"NSMutableDictionary" _parentScrollViews;
@"UIScrollView" _contentScrollView;
B _isConfiguringContentScrollView;
@"UIViewController" _viewController;
```

## Properties

```
@property (T@"UIView",R,N,V_contentView) contentView;
@property (T@"<UIContentConfiguration>",&,N) configuration;
@property (T@"UIViewController",R,W,N,V_viewController) viewController;
```

## Instance methods

```
-[_UIContentUnavailableWrapperView initWithViewController:];
-[_UIContentUnavailableWrapperView _concreteDefaultLayoutMargins];
-[_UIContentUnavailableWrapperView setConfiguration:];
-[_UIContentUnavailableWrapperView _updateBackgroundView];
-[_UIContentUnavailableWrapperView viewController];
-[_UIContentUnavailableWrapperView configuration];
-[_UIContentUnavailableWrapperView contentView];
-[_UIContentUnavailableWrapperView _canApplyConfigurationToExistingContentView:];
-[_UIContentUnavailableWrapperView _contentScrollViewForView:];
-[_UIContentUnavailableWrapperView _replaceContentViewWithViewForConfiguration:];
-[_UIContentUnavailableWrapperView _updateBackgroundViewHandlersForPreviousContentView:newContentView:];
-[_UIContentUnavailableWrapperView reconfigureContentScrollView];
```
