# `_UIBanner`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIBanner`
- 9 instance variables, 13 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"_UIBannerView" _view;
@"_UIBannerContent" _content;
@"_UIBannerManager" _manager;
@"NSLayoutConstraint" _visibleConstraint;
@"NSLayoutConstraint" _hiddenConstraint;
q _state;
@"NSMutableArray" _dismissalAnimations;
@"NSMutableArray" _dismissalCompletionHandlers;
@"NSMutableArray" _tapHandlers;
```

## Properties

```
@property (T@"_UIBannerView",&,N,V_view) view;
@property (Tq,N,V_state) state;
@property (T@"NSMutableArray",&,N,V_dismissalAnimations) dismissalAnimations;
@property (T@"NSMutableArray",&,N,V_dismissalCompletionHandlers) dismissalCompletionHandlers;
@property (T@"NSMutableArray",&,N,V_tapHandlers) tapHandlers;
@property (T@"_UIBannerContent",&,N,V_content) content;
@property (T@"_UIBannerManager",W,N,V_manager) manager;
@property (T@"NSLayoutConstraint",&,N,V_visibleConstraint) visibleConstraint;
@property (T@"NSLayoutConstraint",&,N,V_hiddenConstraint) hiddenConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIBanner present];
-[_UIBanner setContent:];
-[_UIBanner setState:];
-[_UIBanner dismiss];
-[_UIBanner content];
-[_UIBanner setManager:];
-[_UIBanner setView:];
-[_UIBanner manager];
-[_UIBanner view];
-[_UIBanner state];
-[_UIBanner setDismissalCompletionHandlers:];
-[_UIBanner setTapHandlers:];
-[_UIBanner addDismissalAnimations:];
-[_UIBanner addDismissalCompletionHandler:];
-[_UIBanner addTapHandler:];
-[_UIBanner dismissalAnimations];
-[_UIBanner dismissalCompletionHandlers];
-[_UIBanner handleLongPressGesture:];
-[_UIBanner hiddenConstraint];
-[_UIBanner setDismissalAnimations:];
-[_UIBanner setHiddenConstraint:];
-[_UIBanner setVisibleConstraint:];
-[_UIBanner tapHandlers];
-[_UIBanner visibleConstraint];
```
