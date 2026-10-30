# `_UITabDataProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,R,N,GisEnabled) enabled;
@property (TB,R,N,GisSelected) seleted;
@property (TB,R,N,GisSpringLoaded) springLoaded;
@property (Tq,R,N) preferredPlacement;
@property (T@"UITabBarAppearance",R,C,N) standardAppearance;
@property (T@"UITabBarAppearance",R,C,N) scrollEdgeAppearance;
```

## Instance methods

```
-[_UITabDataProvider scrollEdgeAppearance];
-[_UITabDataProvider isSpringLoaded];
-[_UITabDataProvider standardAppearance];
-[_UITabDataProvider imageForStyle:state:];
-[_UITabDataProvider badgeForStyle:state:];
-[_UITabDataProvider isEnabled];
-[_UITabDataProvider isSelected];
-[_UITabDataProvider imageInsetsForStyle:state:];
-[_UITabDataProvider titleForStyle:state:];
-[_UITabDataProvider preferredPlacement];
```
