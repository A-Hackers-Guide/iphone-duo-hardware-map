# `UIStoryboardSegueTemplate`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 7 instance variables, 6 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _segueClassName;
@"UIViewController" _viewController;
@"NSString" _destinationViewControllerIdentifier;
: _prepareForChildViewControllerSelector;
B _performOnViewLoad;
B _animates;
```

## Properties

```
@property (TB,N,V_performOnViewLoad) performOnViewLoad;
@property (TB,N,V_animates) animates;
@property (T@"NSString",&,N) customPrepareForChildViewControllerSelectorName;
@property (T:,R,N) prepareForChildViewControllerSelector;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"UIViewController",W,N,V_viewController) viewController;
```

## Instance methods

```
-[UIStoryboardSegueTemplate setViewController:];
-[UIStoryboardSegueTemplate identifier];
-[UIStoryboardSegueTemplate init];
-[UIStoryboardSegueTemplate _perform:];
-[UIStoryboardSegueTemplate viewController];
-[UIStoryboardSegueTemplate encodeWithCoder:];
-[UIStoryboardSegueTemplate initWithCoder:];
-[UIStoryboardSegueTemplate _performWithDestinationViewController:sender:];
-[UIStoryboardSegueTemplate animates];
-[UIStoryboardSegueTemplate customPrepareForChildViewControllerSelectorName];
-[UIStoryboardSegueTemplate instantiateOrFindDestinationViewControllerWithSender:];
-[UIStoryboardSegueTemplate newDefaultPerformHandlerForSegue:];
-[UIStoryboardSegueTemplate newDefaultPrepareHandlerForSegue:];
-[UIStoryboardSegueTemplate perform:];
-[UIStoryboardSegueTemplate performOnViewLoad];
-[UIStoryboardSegueTemplate prepareForChildViewControllerSelector];
-[UIStoryboardSegueTemplate segueWithDestinationViewController:];
-[UIStoryboardSegueTemplate setAnimates:];
-[UIStoryboardSegueTemplate setCustomPrepareForChildViewControllerSelectorName:];
-[UIStoryboardSegueTemplate setPerformOnViewLoad:];
```
