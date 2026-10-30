# `_UISceneSizeRestrictionsInertImpl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISceneSizeRestrictionsImpl`
- 3 instance variables, 7 properties, 6 instance methods, 2 class methods

## Instance variables

```
B allowsFullScreen;
{CGSize="width"d"height"d} minimumSize;
{CGSize="width"d"height"d} maximumSize;
```

## Properties

```
@property (T{CGSize=dd},N,VminimumSize) minimumSize;
@property (T{CGSize=dd},N,VmaximumSize) maximumSize;
@property (TB,N,VallowsFullScreen) allowsFullScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneSizeRestrictionsInertImpl implementationForScene:];
+[_UISceneSizeRestrictionsInertImpl scenePredicate];
```

## Instance methods

```
-[_UISceneSizeRestrictionsInertImpl setMaximumSize:];
-[_UISceneSizeRestrictionsInertImpl maximumSize];
-[_UISceneSizeRestrictionsInertImpl setMinimumSize:];
-[_UISceneSizeRestrictionsInertImpl minimumSize];
-[_UISceneSizeRestrictionsInertImpl allowsFullScreen];
-[_UISceneSizeRestrictionsInertImpl setAllowsFullScreen:];
```
