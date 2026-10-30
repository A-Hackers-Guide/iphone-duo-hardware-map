# `_UISceneSafeAreaSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"_UISceneSafeAreaEdgeInsetResolver",&,N) safeAreaEdgeInsetResolver;
@property (T@"_UISceneSafeAreaCornerInsetResolver",&,N) safeAreaCornerInsetResolver;
@property (T{UIEdgeInsets=dddd},N) safeAreaEdgeInsets;
@property (T{_UICornerInsets={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N) safeAreaCornerInsets;
```

## Instance methods

```
-[_UISceneSafeAreaSettings safeAreaEdgeInsets];
-[_UISceneSafeAreaSettings safeAreaCornerInsets];
-[_UISceneSafeAreaSettings setSafeAreaCornerInsetResolver:];
-[_UISceneSafeAreaSettings safeAreaCornerInsetResolver];
-[_UISceneSafeAreaSettings safeAreaEdgeInsetResolver];
-[_UISceneSafeAreaSettings setSafeAreaCornerInsets:];
-[_UISceneSafeAreaSettings setSafeAreaEdgeInsetResolver:];
-[_UISceneSafeAreaSettings setSafeAreaEdgeInsets:];
```
