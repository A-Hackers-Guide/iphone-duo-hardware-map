# `_UIScrollPocketBarInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction_Internal`, `_UIGeometryChangeObserver`
- 16 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
? view;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 collectorInteraction;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 delegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 tracksFloatingElements;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 appliesPocketTraitsToView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 shouldDriveStatusBarStyle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastForwardedEdges;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastForwardedCleanUserInterfaceStyle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 pocketReceivers;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 receiverDrivingTraits;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 lastAccumulatedMetrics;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 floatingElements;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 dirty;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 materialBackdropContext;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 luminanceAggregatorObserver;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_luminanceAggregator;
```

## Properties

```
@property (T@"UIView",N,W,Vview) view;
@property (T@"NSString",N,R) description;
```

## Class methods

```
+[_UIScrollPocketBarInteraction isEnabled];
```

## Instance methods

```
-[_UIScrollPocketBarInteraction init];
-[_UIScrollPocketBarInteraction _updateProperties];
-[_UIScrollPocketBarInteraction setView:];
-[_UIScrollPocketBarInteraction _didMoveFromWindow:toWindow:];
-[_UIScrollPocketBarInteraction _geometryChanged:forAncestor:];
-[_UIScrollPocketBarInteraction view];
-[_UIScrollPocketBarInteraction dumpBarConfigs];
-[_UIScrollPocketBarInteraction willMoveToView:];
-[_UIScrollPocketBarInteraction description];
-[_UIScrollPocketBarInteraction _viewVisibilityDidChange];
-[_UIScrollPocketBarInteraction dumpReceivers];
-[_UIScrollPocketBarInteraction _viewTraitCollectionDidChange:];
-[_UIScrollPocketBarInteraction didMoveToView:];
-[_UIScrollPocketBarInteraction dumpResolvedBarConfigs];
```
