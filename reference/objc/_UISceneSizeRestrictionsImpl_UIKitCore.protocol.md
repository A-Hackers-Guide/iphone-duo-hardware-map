# `_UISceneSizeRestrictionsImpl` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 6 instance methods, 2 class methods

## Properties

```
@property (T{CGSize=dd},N) minimumSize;
@property (T{CGSize=dd},N) maximumSize;
@property (TB,N) allowsFullScreen;
```

## Class methods

```
+[_UISceneSizeRestrictionsImpl implementationForScene:];
+[_UISceneSizeRestrictionsImpl scenePredicate];
```

## Instance methods

```
-[_UISceneSizeRestrictionsImpl setMaximumSize:];
-[_UISceneSizeRestrictionsImpl maximumSize];
-[_UISceneSizeRestrictionsImpl setMinimumSize:];
-[_UISceneSizeRestrictionsImpl minimumSize];
-[_UISceneSizeRestrictionsImpl allowsFullScreen];
-[_UISceneSizeRestrictionsImpl setAllowsFullScreen:];
```
