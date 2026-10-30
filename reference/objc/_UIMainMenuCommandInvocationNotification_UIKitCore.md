# `_UIMainMenuCommandInvocationNotification`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _categoryMenuSessionMap;
@"_UIMainMenuIdentifier" _fallbackMenuIdentifier;
```

## Class methods

```
+[_UIMainMenuCommandInvocationNotification supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuCommandInvocationNotification encodeWithCoder:];
-[_UIMainMenuCommandInvocationNotification hash];
-[_UIMainMenuCommandInvocationNotification description];
-[_UIMainMenuCommandInvocationNotification initWithCoder:];
-[_UIMainMenuCommandInvocationNotification isEqual:];
-[_UIMainMenuCommandInvocationNotification _initWithCategoryMenuSessionMap:fallbackMenuIdentifier:];
-[_UIMainMenuCommandInvocationNotification invokedCommandCategoryMenuIdentifierForSession:];
```
