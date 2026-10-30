# `_UISplitViewControllerAdaptiveColumnSeparatorView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIPointerInteractionDelegate`
- 6 instance variables, 8 properties, 14 instance methods, 2 class methods

## Instance variables

```
B _dimmingBackgroundEnabled;
Q _permittedResizeDirections;
d _dimmingLevel;
q _splitViewControllerColumn;
@"_UISplitViewControllerAdaptiveColumnSeparatorDimmingView" _dimmingView;
@"UIPointerInteraction" _pointerInteraction;
```

## Properties

```
@property (TQ,N,V_permittedResizeDirections) permittedResizeDirections;
@property (Td,N,V_dimmingLevel) dimmingLevel;
@property (TB,N,V_dimmingBackgroundEnabled) dimmingBackgroundEnabled;
@property (Tq,R,N,V_splitViewControllerColumn) splitViewControllerColumn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISplitViewControllerAdaptiveColumnSeparatorView touchHitTargetDimension];
+[_UISplitViewControllerAdaptiveColumnSeparatorView pointerHitTargetDimension];
```

## Instance methods

```
-[_UISplitViewControllerAdaptiveColumnSeparatorView pointerInteraction:styleForRegion:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView dimmingBackgroundEnabled];
-[_UISplitViewControllerAdaptiveColumnSeparatorView setBounds:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView setDimmingLevel:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView permittedResizeDirections];
-[_UISplitViewControllerAdaptiveColumnSeparatorView dimmingLevel];
-[_UISplitViewControllerAdaptiveColumnSeparatorView splitViewControllerColumn];
-[_UISplitViewControllerAdaptiveColumnSeparatorView pointerInteraction:regionForRequest:defaultRegion:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView setDimmingBackgroundEnabled:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView setFrame:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView updateDimmingBackground];
-[_UISplitViewControllerAdaptiveColumnSeparatorView _updateTouchInsetsForPointer];
-[_UISplitViewControllerAdaptiveColumnSeparatorView initWithSplitViewControllerColumn:];
-[_UISplitViewControllerAdaptiveColumnSeparatorView setPermittedResizeDirections:];
```
