# `_UIPresentationControllerDefaultVisualStyleProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPresentationControllerVisualStyleProviding`
- 2 instance variables, 7 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _providerByIdiom;
@"_UIPresentationControllerNullVisualStyleProvider" _fallbackProvider;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_providerByIdiom) providerByIdiom;
@property (T@"_UIPresentationControllerNullVisualStyleProvider",&,N,V_fallbackProvider) fallbackProvider;
@property (T@"_UISheetPresentationMetrics",?,R,N) defaultSheetMetrics;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIPresentationControllerDefaultVisualStyleProvider sharedInstance];
```

## Instance methods

```
-[_UIPresentationControllerDefaultVisualStyleProvider presentationControllerClassForModalPresentationStyle:inIdiom:];
-[_UIPresentationControllerDefaultVisualStyleProvider styleForRootPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider _providerForPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider presentationControllerForPresentedViewController:inIdiom:];
-[_UIPresentationControllerDefaultVisualStyleProvider fallbackProvider];
-[_UIPresentationControllerDefaultVisualStyleProvider providerByIdiom];
-[_UIPresentationControllerDefaultVisualStyleProvider defaultStyleForPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider _init];
-[_UIPresentationControllerDefaultVisualStyleProvider _providerForViewController:];
-[_UIPresentationControllerDefaultVisualStyleProvider presentationControllerForPresentedViewController:];
-[_UIPresentationControllerDefaultVisualStyleProvider styleForPopoverPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider styleForSheetPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider defaultConcreteTransitionStyleForViewController:];
-[_UIPresentationControllerDefaultVisualStyleProvider defaultSheetMetrics];
-[_UIPresentationControllerDefaultVisualStyleProvider defaultConcretePresentationStyleForViewController:];
-[_UIPresentationControllerDefaultVisualStyleProvider styleForAlertPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider styleForSearchPresentationController:];
-[_UIPresentationControllerDefaultVisualStyleProvider registerVisualStyleProvider:forIdiom:];
-[_UIPresentationControllerDefaultVisualStyleProvider setProviderByIdiom:];
-[_UIPresentationControllerDefaultVisualStyleProvider _providerForIdiom:];
-[_UIPresentationControllerDefaultVisualStyleProvider setFallbackProvider:];
```
