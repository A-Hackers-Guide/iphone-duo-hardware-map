# `SBFluidSwitcherContentView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIFocusItemScrollableContainer`, `SBSwitcherLayoutElementProviding`
- 2 instance variables, 10 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _passesTouchesThrough;
@"<SBFluidSwitcherContentViewDelegate>" _delegate;
```

## Properties

```
@property (TB,N,V_passesTouchesThrough) passesTouchesThrough;
@property (T@"<SBFluidSwitcherContentViewDelegate>",W,N,V_delegate) delegate;
@property (T{CGPoint=dd},N) contentOffset;
@property (T{CGSize=dd},R,N) contentSize;
@property (T{CGSize=dd},R,N) visibleSize;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherContentView contentOffset];
-[SBFluidSwitcherContentView isAppLayout];
-[SBFluidSwitcherContentView appLayout];
-[SBFluidSwitcherContentView setContentOffset:];
-[SBFluidSwitcherContentView switcherLayoutElementType];
-[SBFluidSwitcherContentView visibleSize];
-[SBFluidSwitcherContentView hitTest:withEvent:];
-[SBFluidSwitcherContentView contentSize];
-[SBFluidSwitcherContentView canBecomeFocused];
-[SBFluidSwitcherContentView setPassesTouchesThrough:];
-[SBFluidSwitcherContentView setDelegate:];
-[SBFluidSwitcherContentView passesTouchesThrough];
-[SBFluidSwitcherContentView delegate];
-[SBFluidSwitcherContentView preferredFocusEnvironments];
-[SBFluidSwitcherContentView copyWithZone:];
```
