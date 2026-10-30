# `_UIMainMenuCommandPrimaryActionContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
S _secureNamespace;
@"_UIMainMenuCommand" _command;
@"_UIMainMenuIdentifier" _categoryMenuIdentifier;
```

## Properties

```
@property (T@"_UIMainMenuIdentifier",&,N,V_categoryMenuIdentifier) categoryMenuIdentifier;
@property (T@"_UIMainMenuCommand",R,N,V_command) command;
@property (TB,R,N) needsAuthenticationMessage;
@property (TS,R,N,V_secureNamespace) secureNamespace;
```

## Instance methods

```
-[_UIMainMenuCommandPrimaryActionContext command];
-[_UIMainMenuCommandPrimaryActionContext secureNamespace];
-[_UIMainMenuCommandPrimaryActionContext _initWithCommand:secureNamespace:];
-[_UIMainMenuCommandPrimaryActionContext categoryMenuIdentifier];
-[_UIMainMenuCommandPrimaryActionContext needsAuthenticationMessage];
-[_UIMainMenuCommandPrimaryActionContext setCategoryMenuIdentifier:];
```
