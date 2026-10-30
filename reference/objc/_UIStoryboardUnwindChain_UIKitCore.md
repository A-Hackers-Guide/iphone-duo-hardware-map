# `_UIStoryboardUnwindChain`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _viewControllers;
Q _commonAncestorIdx;
Q _modalAncestorContainingSourceIdx;
```

## Properties

```
@property (T@"UIViewController",R,N) commonAncestorViewController;
@property (T@"UIViewController",R,N) modalAncestorContainingSourceViewController;
```

## Instance methods

```
-[_UIStoryboardUnwindChain debugDescription];
-[_UIStoryboardUnwindChain commonAncestorViewController];
-[_UIStoryboardUnwindChain enumerateViewControllersFromModalAncestorUpToButNotIncludingDestination:];
-[_UIStoryboardUnwindChain initFromSourceViewController:toDestinationViewController:];
-[_UIStoryboardUnwindChain modalAncestorContainingSourceViewController];
```
