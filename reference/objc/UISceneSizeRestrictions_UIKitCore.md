# `UISceneSizeRestrictions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"<_UISceneSizeRestrictionsImpl>" _activeImpl;
```

## Properties

```
@property (T{CGSize=dd},N) minimumSize;
@property (T{CGSize=dd},N) maximumSize;
@property (TB,N) allowsFullScreen;
```

## Class methods

```
+[UISceneSizeRestrictions _registerImplClass:];
```

## Instance methods

```
-[UISceneSizeRestrictions setMaximumSize:];
-[UISceneSizeRestrictions _initWithScene:];
-[UISceneSizeRestrictions maximumSize];
-[UISceneSizeRestrictions setMinimumSize:];
-[UISceneSizeRestrictions minimumSize];
-[UISceneSizeRestrictions _initWithImplementation:];
-[UISceneSizeRestrictions _implOfClass:];
-[UISceneSizeRestrictions allowsFullScreen];
-[UISceneSizeRestrictions setAllowsFullScreen:];
```
