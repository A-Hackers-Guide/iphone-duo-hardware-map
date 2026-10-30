# `UIStoryboardUnwindSegueSource`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _searchChain;
@"UIViewController" _sourceViewController;
: _unwindAction;
@ _sender;
```

## Properties

```
@property (T@"UIViewController",R,V_sourceViewController) sourceViewController;
@property (T:,R,V_unwindAction) unwindAction;
@property (T@,R,V_sender) sender;
```

## Instance methods

```
-[UIStoryboardUnwindSegueSource init];
-[UIStoryboardUnwindSegueSource sender];
-[UIStoryboardUnwindSegueSource _childContainingUnwindSourceForViewController:];
-[UIStoryboardUnwindSegueSource _findDestination];
-[UIStoryboardUnwindSegueSource _initWithSourceViewController:action:sender:];
-[UIStoryboardUnwindSegueSource sourceViewController];
-[UIStoryboardUnwindSegueSource unwindAction];
```
