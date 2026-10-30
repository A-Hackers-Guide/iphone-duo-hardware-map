# `_UISceneHostingGraph`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISceneHostingGraph`
- 2 instance variables, 0 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMapTable" _hostingGraph;
@"NSHashTable" _lazy_contextTrackingAssertions;
```

## Class methods

```
+[_UISceneHostingGraph sharedInstance];
```

## Instance methods

```
-[_UISceneHostingGraph _init];
-[_UISceneHostingGraph _localWindowGraphHostingContextID:];
-[_UISceneHostingGraph _noteContextID:hostedByWindow:];
-[_UISceneHostingGraph _rawWindowHostingContextID:];
-[_UISceneHostingGraph localWindowGraphHostingContextID:];
-[_UISceneHostingGraph observeLocalWindowGraphHostingContextID:withHandler:];
```
