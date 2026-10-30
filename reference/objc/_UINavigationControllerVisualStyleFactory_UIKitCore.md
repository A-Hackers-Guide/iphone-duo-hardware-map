# `_UINavigationControllerVisualStyleFactory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UINavigationControllerVisualStyleProviding`
- 1 instance variables, 5 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"<_UINavigationControllerVisualStyleProviding>" _visualStyleProvider;
```

## Properties

```
@property (T@"<_UINavigationControllerVisualStyleProviding>",&,N,V_visualStyleProvider) visualStyleProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UINavigationControllerVisualStyleFactory sharedInstance];
```

## Instance methods

```
-[_UINavigationControllerVisualStyleFactory init];
-[_UINavigationControllerVisualStyleFactory visualStyleProvider];
-[_UINavigationControllerVisualStyleFactory registerVisualStyleProvider:];
-[_UINavigationControllerVisualStyleFactory setVisualStyleProvider:];
-[_UINavigationControllerVisualStyleFactory styleForNavigationController:];
```
