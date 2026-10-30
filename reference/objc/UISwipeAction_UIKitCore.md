# `UISwipeAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIContextualAction`
- 4 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _canBeTriggeredBySwipe;
B _resetsSwipedRow;
@"UIVisualEffect" _backgroundEffect;
@? _completionHandler;
```

## Properties

```
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"UIColor",C,N) color;
@property (T@"UIImage",C,N) icon;
@property (T@"UIVisualEffect",C,N,V_backgroundEffect) backgroundEffect;
@property (TB,N,V_canBeTriggeredBySwipe) canBeTriggeredBySwipe;
@property (TB,N,V_resetsSwipedRow) resetsSwipedRow;
```

## Class methods

```
+[UISwipeAction swipeActionWithStyle:title:handler:];
```

## Instance methods

```
-[UISwipeAction setColor:];
-[UISwipeAction setBackgroundEffect:];
-[UISwipeAction setCompletionHandler:];
-[UISwipeAction completionHandler];
-[UISwipeAction init];
-[UISwipeAction setIcon:];
-[UISwipeAction backgroundEffect];
-[UISwipeAction color];
-[UISwipeAction icon];
-[UISwipeAction resetsSwipedRow];
-[UISwipeAction canBeTriggeredBySwipe];
-[UISwipeAction resetSwipedRow];
-[UISwipeAction setCanBeTriggeredBySwipe:];
-[UISwipeAction setResetsSwipedRow:];
```
