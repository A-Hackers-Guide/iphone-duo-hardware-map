# `_UIButtonBarSpacerLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIButtonBarLayout`
- 7 instance variables, 1 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"UIBarButtonItem" _item;
@"UIView" _spacer;
@"NSLayoutConstraint" _requestedSize;
@"NSLayoutConstraint" _minimumSize;
@"NSLayoutConstraint" _equalSize;
B _flexible;
q _spacerType;
```

## Properties

```
@property (Tq,R,N,V_spacerType) spacerType;
```

## Class methods

```
+[_UIButtonBarSpacerLayout _updateSpacer:layoutMetrics:spacerType:];
+[_UIButtonBarSpacerLayout spacerForLayoutMetrics:betweenLayout:andLayout:];
+[_UIButtonBarSpacerLayout typeOfSpacerBetweenLayout:andLayout:];
```

## Instance methods

```
-[_UIButtonBarSpacerLayout _configure];
-[_UIButtonBarSpacerLayout barButtonItem];
-[_UIButtonBarSpacerLayout description];
-[_UIButtonBarSpacerLayout suppressSpacing];
-[_UIButtonBarSpacerLayout _addConstraintsToActivate:toDeactivate:];
-[_UIButtonBarSpacerLayout _addLayoutViews:];
-[_UIButtonBarSpacerLayout initWithLayoutMetrics:];
-[_UIButtonBarSpacerLayout initWithLayoutMetrics:barButtonItem:];
-[_UIButtonBarSpacerLayout isSpaceLayout];
-[_UIButtonBarSpacerLayout minimumLayoutWidthGivenMinimumSpaceWidth:];
-[_UIButtonBarSpacerLayout spacerType];
```
