# `UIWebElementAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 7 instance methods, 3 class methods

## Instance variables

```
@"NSString" _title;
@? _actionHandler;
@? _dismissalHandler;
i _type;
```

## Properties

```
@property (Ti,R,N,V_type) type;
@property (T@?,C,N,V_dismissalHandler) dismissalHandler;
```

## Class methods

```
+[UIWebElementAction customElementActionWithTitle:actionHandler:];
+[UIWebElementAction standardElementActionWithType:];
+[UIWebElementAction standardElementActionWithType:customTitle:context:];
```

## Instance methods

```
-[UIWebElementAction dealloc];
-[UIWebElementAction type];
-[UIWebElementAction _runActionWithElement:targetURL:documentView:interactionLocation:];
-[UIWebElementAction _title];
-[UIWebElementAction dismissalHandler];
-[UIWebElementAction initWithTitle:actionHandler:type:];
-[UIWebElementAction setDismissalHandler:];
```
