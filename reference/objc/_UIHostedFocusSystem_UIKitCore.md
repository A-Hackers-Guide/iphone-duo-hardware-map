# `_UIHostedFocusSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFocusSystem`
- 3 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<UIFocusEnvironment>" _hostEnvironment;
@"_UIHostedFocusSystemItemContainer" _itemContainerProxy;
@"_UIHostedFocusSystemDelegateProxy" _delegateProxy;
```

## Properties

```
@property (T@"_UIHostedFocusSystemItemContainer",R,N,V_itemContainerProxy) itemContainerProxy;
@property (T@"_UIHostedFocusSystemDelegateProxy",&,N,V_delegateProxy) delegateProxy;
@property (T@"<UIFocusEnvironment>",R,W,N,V_hostEnvironment) hostEnvironment;
@property (T@"<_UIHostedFocusSystemDelegate>",W,N) delegate;
```

## Instance methods

```
-[_UIHostedFocusSystem _isEligibleForFocusInteraction];
-[_UIHostedFocusSystem setDelegateProxy:];
-[_UIHostedFocusSystem delegateProxy];
-[_UIHostedFocusSystem focusItemContainer];
-[_UIHostedFocusSystem setDelegate:];
-[_UIHostedFocusSystem behavior];
-[_UIHostedFocusSystem delegate];
-[_UIHostedFocusSystem _isEligibleForFocusOcclusion];
-[_UIHostedFocusSystem containsChildOfHostEnvironment:];
-[_UIHostedFocusSystem hostEnvironment];
-[_UIHostedFocusSystem _focusSystemIsValid];
-[_UIHostedFocusSystem _hostFocusSystem];
-[_UIHostedFocusSystem _initWithHostEnvironment:];
-[_UIHostedFocusSystem _postsFocusUpdateNotifications];
-[_UIHostedFocusSystem _prefersDeferralForFocusUpdateInContext:];
-[_UIHostedFocusSystem itemContainerProxy];
```
