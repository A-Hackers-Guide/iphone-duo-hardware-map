# `UIKeyboardTaskEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
@? __task;
@"NSArray" __creationStack;
@"NSArray" _originatingStack;
@? _breadcrumb;
```

## Properties

```
@property (T@"NSArray",R,N,V_originatingStack) originatingStack;
@property (T@?,R,N,V_breadcrumb) breadcrumb;
```

## Instance methods

```
-[UIKeyboardTaskEntry breadcrumb];
-[UIKeyboardTaskEntry initWithTask:breadcrumb:];
-[UIKeyboardTaskEntry originatingStack];
-[UIKeyboardTaskEntry copyWithZone:];
-[UIKeyboardTaskEntry execute:];
```
