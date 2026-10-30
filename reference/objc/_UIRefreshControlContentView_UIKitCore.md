# `_UIRefreshControlContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 3 instance variables, 7 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIRefreshControl" _refreshControl;
@"UIColor" _tintColor;
@"UIImpactFeedbackGenerator" _impactFeedbackGenerator;
```

## Properties

```
@property (Tq,R,N) style;
@property (T@"UIRefreshControl",N,V_refreshControl) refreshControl;
@property (T@"UIColor",&,N,V_tintColor) tintColor;
@property (T@"NSAttributedString",&,N) attributedTitle;
@property (Td,R,N) minimumSnappingHeight;
@property (Td,R,N) maximumSnappingHeight;
@property (T@"UIImpactFeedbackGenerator",&,N,V_impactFeedbackGenerator) impactFeedbackGenerator;
```

## Instance methods

```
-[_UIRefreshControlContentView setAttributedTitle:];
-[_UIRefreshControlContentView style];
-[_UIRefreshControlContentView willTransitionFromState:toState:];
-[_UIRefreshControlContentView didTransitionFromState:toState:];
-[_UIRefreshControlContentView setTintColor:];
-[_UIRefreshControlContentView _heightAtWhichNoneOfTheInterfaceElementsAreVisibleEvenIfTheControlIsStillPartiallyOnScreen];
-[_UIRefreshControlContentView attributedTitle];
-[_UIRefreshControlContentView tintColor];
-[_UIRefreshControlContentView maximumSnappingHeight];
-[_UIRefreshControlContentView setRefreshControl:];
-[_UIRefreshControlContentView _removeAllAnimations];
-[_UIRefreshControlContentView impactFeedbackGenerator];
-[_UIRefreshControlContentView minimumSnappingHeight];
-[_UIRefreshControlContentView refreshControl];
-[_UIRefreshControlContentView refreshControlInvalidatedSnappingHeight];
-[_UIRefreshControlContentView setImpactFeedbackGenerator:];
```
