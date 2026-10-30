# `SBMenuBarHeaderContainerView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 5 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
d _contentHeight;
@"NSMutableArray" _menuHeaderViews;
@"NSMutableArray" _trailingConstraints;
@"NSLayoutConstraint" _leadingEdgeConstraint;
d _contentOriginOffset;
```

## Properties

```
@property (T@"NSArray",R,N,V_menuHeaderViews) menuHeaderViews;
@property (Td,R,N) contentWidth;
@property (Td,N,V_contentOriginOffset) contentOriginOffset;
```

## Instance methods

```
-[SBMenuBarHeaderContainerView contentWidth];
-[SBMenuBarHeaderContainerView menuHeaderViews];
-[SBMenuBarHeaderContainerView animateToPresented:fadeAppMenu:completion:];
-[SBMenuBarHeaderContainerView appendOverflowMenuView:fittingMaximumContentWidth:];
-[SBMenuBarHeaderContainerView contentOriginOffset];
-[SBMenuBarHeaderContainerView initWithMenuHeaderViews:contentHeight:];
-[SBMenuBarHeaderContainerView prependMenuView:];
-[SBMenuBarHeaderContainerView setContentOriginOffset:];
```
