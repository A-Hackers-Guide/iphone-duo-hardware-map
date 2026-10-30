# `UISplitViewControllerImplFactory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISplitViewControllerImplProviding`
- 1 instance variables, 5 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"<UISplitViewControllerImplProviding>" _implProvider;
```

## Properties

```
@property (T@"<UISplitViewControllerImplProviding>",&,N,V_implProvider) implProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISplitViewControllerImplFactory sharedInstance];
```

## Instance methods

```
-[UISplitViewControllerImplFactory init];
-[UISplitViewControllerImplFactory implClassForSplitViewController:];
-[UISplitViewControllerImplFactory implProvider];
-[UISplitViewControllerImplFactory registerImplProvider:];
-[UISplitViewControllerImplFactory setImplProvider:];
```
