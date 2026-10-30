# `SBSplitViewHandleNubView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBFSystemPointerInteractionDelegate`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"CABackdropLayer" _backdropLayer;
@"SBSystemPointerInteractionManager" _systemPointerInteractionManager;
q _style;
@"UIView" _nubContainerView;
```

## Properties

```
@property (T@"UIView",R,N,V_nubContainerView) nubContainerView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSplitViewHandleNubView styleForRegion:forView:];
-[SBSplitViewHandleNubView dealloc];
-[SBSplitViewHandleNubView layoutSubviews];
-[SBSplitViewHandleNubView shouldBeginPointerInteractionRequest:atLocation:forView:];
-[SBSplitViewHandleNubView pointerInteractionHitTestInsetsForView:];
-[SBSplitViewHandleNubView initWithFrame:systemPointerInteractionManager:style:];
-[SBSplitViewHandleNubView nubContainerView];
-[SBSplitViewHandleNubView nubHitTestSize];
-[SBSplitViewHandleNubView nubViewSize];
```
