# `_UISearchControllerView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 7 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSLayoutConstraint" _inlineSearchFieldOnscreenConstraint;
@"NSLayoutConstraint" _inlineSearchFieldOffscreenConstraint;
@"_UIInlineSearchFieldAccessoryContainer" _inlineSearchFieldAccessoryContainer;
B _receivedKeyboardWillShow;
B __ensureSystemInputViewAboveSearchBarContainerView;
B _inlineSearchFieldAccessoryIsOffscreenForPresentationAnimation;
@"_UISearchControllerInlineSearchFieldAccessoryView" _inlineSearchFieldAccessoryView;
```

## Properties

```
@property (T@"_UISearchControllerInlineSearchFieldAccessoryView",&,N,V_inlineSearchFieldAccessoryView) inlineSearchFieldAccessoryView;
@property (TB,N,V__ensureSystemInputViewAboveSearchBarContainerView) _ensureSystemInputViewAboveSearchBarContainerView;
@property (TB,N,V_inlineSearchFieldAccessoryIsOffscreenForPresentationAnimation) inlineSearchFieldAccessoryIsOffscreenForPresentationAnimation;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _occludedFrame;
```

## Instance methods

```
-[_UISearchControllerView didMoveToWindow];
-[_UISearchControllerView hitTest:withEvent:];
-[_UISearchControllerView _addSubview:positioned:relativeTo:];
-[_UISearchControllerView updateConstraints];
-[_UISearchControllerView initWithFrame:];
-[_UISearchControllerView sendSubviewToBack:];
-[_UISearchControllerView bringSubviewToFront:];
-[_UISearchControllerView _ensureCarPlayLimitedUIIsOnTop];
-[_UISearchControllerView _ensureContainerIsOnTop];
-[_UISearchControllerView _ensureInlineSearchAccessoryViewIsOnTop];
-[_UISearchControllerView _ensurePortalViewIsOnTop];
-[_UISearchControllerView _ensureSubviewOrdering];
-[_UISearchControllerView _ensureSystemInputViewAboveSearchBarContainerView];
-[_UISearchControllerView _ensureViewOfClassIsOnTop:];
-[_UISearchControllerView _keyboardWillHideOrShow:];
-[_UISearchControllerView _occludedFrame];
-[_UISearchControllerView _reevaluateInlineSearchFieldAccessoryHiddenState];
-[_UISearchControllerView _updateInlineSearchAccessoryFrame];
-[_UISearchControllerView borrowSearchFieldFromControllerForInlinePresentation:];
-[_UISearchControllerView inlineSearchFieldAccessoryIsOffscreenForPresentationAnimation];
-[_UISearchControllerView inlineSearchFieldAccessoryView];
-[_UISearchControllerView returnBorrowedSearchTextField];
-[_UISearchControllerView setInlineSearchFieldAccessoryIsOffscreenForPresentationAnimation:];
-[_UISearchControllerView setInlineSearchFieldAccessoryView:];
-[_UISearchControllerView set_ensureSystemInputViewAboveSearchBarContainerView:];
```
