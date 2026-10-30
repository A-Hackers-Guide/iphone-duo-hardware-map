# `_UIStatusBarActionable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"_UIStatusBarAction",&,N) action;
@property (T@"_UIStatusBarAction",&,N) hoverAction;
@property (T@"UIView",R,N) hoverView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) absoluteHoverFrame;
@property (TB,R,N) hoverHighlightsAsRegion;
@property (T{NSDirectionalEdgeInsets=dddd},N) extendedHoverInsets;
@property (T{UIEdgeInsets=dddd},N) actionInsets;
@property (T@"<UILayoutItem>",R,N) layoutItem;
```

## Instance methods

```
-[_UIStatusBarActionable actionInsets];
-[_UIStatusBarActionable setActionInsets:];
-[_UIStatusBarActionable hoverAction];
-[_UIStatusBarActionable setHoverAction:];
-[_UIStatusBarActionable enableWithToken:];
-[_UIStatusBarActionable disableWithToken:];
-[_UIStatusBarActionable setAction:];
-[_UIStatusBarActionable action];
-[_UIStatusBarActionable hoverView];
-[_UIStatusBarActionable extendedHoverInsets];
-[_UIStatusBarActionable hoverHighlightsAsRegion];
-[_UIStatusBarActionable setExtendedHoverInsets:];
-[_UIStatusBarActionable layoutItem];
-[_UIStatusBarActionable absoluteHoverFrame];
```
