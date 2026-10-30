# `UIStoryboardSegue`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"UIViewController" _sourceViewController;
@"UIViewController" _destinationViewController;
@? _performHandler;
@? _prepareHandler;
@ _sender;
```

## Properties

```
@property (T@?,C,N,V_prepareHandler) prepareHandler;
@property (T@?,C,N,V_performHandler) performHandler;
@property (T@,&,N,V_sender) sender;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"UIViewController",R,N,V_sourceViewController) sourceViewController;
@property (T@"UIViewController",R,N,V_destinationViewController) destinationViewController;
```

## Class methods

```
+[UIStoryboardSegue segueWithIdentifier:source:destination:performHandler:];
```

## Instance methods

```
-[UIStoryboardSegue perform];
-[UIStoryboardSegue identifier];
-[UIStoryboardSegue init];
-[UIStoryboardSegue _prepare];
-[UIStoryboardSegue sender];
-[UIStoryboardSegue setSender:];
-[UIStoryboardSegue destinationViewController];
-[UIStoryboardSegue initWithIdentifier:source:destination:];
-[UIStoryboardSegue performHandler];
-[UIStoryboardSegue prepareHandler];
-[UIStoryboardSegue setPerformHandler:];
-[UIStoryboardSegue setPrepareHandler:];
-[UIStoryboardSegue sourceViewController];
```
