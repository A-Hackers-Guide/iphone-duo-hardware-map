# `_UITableViewDropAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragAnimating`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _didBeginAnimation;
@"UIDragItem" _dragItem;
@"NSMutableArray" _animationsBlocks;
@"NSMutableArray" _completionBlocks;
```

## Properties

```
@property (T@"UIDragItem",&,N,V_dragItem) dragItem;
@property (T@"NSMutableArray",&,N,V_animationsBlocks) animationsBlocks;
@property (T@"NSMutableArray",&,N,V_completionBlocks) completionBlocks;
@property (TB,N,G_didBeginAnimation,S_setDidBeginAnimation:,V_didBeginAnimation) didBeginAnimation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITableViewDropAnimation addAnimations:];
-[_UITableViewDropAnimation addCompletion:];
-[_UITableViewDropAnimation completionBlocks];
-[_UITableViewDropAnimation setCompletionBlocks:];
-[_UITableViewDropAnimation _addClientBlocksToAnimator:];
-[_UITableViewDropAnimation _didBeginAnimation];
-[_UITableViewDropAnimation _executeCompletionBlocks];
-[_UITableViewDropAnimation _setDidBeginAnimation:];
-[_UITableViewDropAnimation animationsBlocks];
-[_UITableViewDropAnimation dragItem];
-[_UITableViewDropAnimation initWithDragItem:];
-[_UITableViewDropAnimation setAnimationsBlocks:];
-[_UITableViewDropAnimation setDragItem:];
```
