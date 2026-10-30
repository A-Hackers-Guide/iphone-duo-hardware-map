# `UIStoryboardDecodingContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UIStoryboardSegueTemplate" _sourceSegueTemplate;
@ _sender;
@"UIClassSwapper" _classSwapperTemplate;
@"UIViewController" _parentViewController;
q _childViewControllerIndex;
@? _creator;
```

## Properties

```
@property (T@"UIClassSwapper",&,N,V_classSwapperTemplate) classSwapperTemplate;
@property (T@"UIStoryboardSegueTemplate",&,N,V_sourceSegueTemplate) sourceSegueTemplate;
@property (T@"UIViewController",&,N,V_parentViewController) parentViewController;
@property (Tq,N,V_childViewControllerIndex) childViewControllerIndex;
@property (T@,&,N,V_sender) sender;
@property (T@?,C,N,V_creator) creator;
```

## Instance methods

```
-[UIStoryboardDecodingContext setCreator:];
-[UIStoryboardDecodingContext creator];
-[UIStoryboardDecodingContext sender];
-[UIStoryboardDecodingContext setSender:];
-[UIStoryboardDecodingContext childViewControllerIndex];
-[UIStoryboardDecodingContext classSwapperTemplate];
-[UIStoryboardDecodingContext parentViewController];
-[UIStoryboardDecodingContext setChildViewControllerIndex:];
-[UIStoryboardDecodingContext setClassSwapperTemplate:];
-[UIStoryboardDecodingContext setParentViewController:];
-[UIStoryboardDecodingContext setSourceSegueTemplate:];
-[UIStoryboardDecodingContext sourceSegueTemplate];
```
