# `_UISplitViewControllerPanelPrimaryViewControllerPromiseItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFocusItem`, `UIFocusItemContainer`
- 3 instance variables, 18 properties, 17 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
@"UIView" _parentView;
@"UISplitViewControllerPanelImpl" _impl;
```

## Properties

```
@property (T@"UIView",W,N,V_parentView) parentView;
@property (T@"UISplitViewControllerPanelImpl",W,N,V_impl) impl;
@property (TB,R,N) canBecomeFocused;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
```

## Instance methods

```
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem impl];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem updateFocusIfNeeded];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem parentView];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem setImpl:];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem setParentView:];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem coordinateSpace];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem focusItemsInRect:];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem didUpdateFocusInContext:withAnimationCoordinator:];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem setNeedsFocusUpdate];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem parentFocusEnvironment];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem focusItemContainer];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem canBecomeFocused];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem preferredFocusEnvironments];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem shouldUpdateFocusInContext:];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem frame];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem _isLazyFocusItemContainer];
-[_UISplitViewControllerPanelPrimaryViewControllerPromiseItem initWithParentView:impl:];
```
