# `_UIMainMenuPerformableKeyboardShortcutCommand`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuCommand" _command;
@"_UIMainMenuCommandState" _state;
@"_UIMainMenuIdentifier" _categoryMenuIdentifier;
```

## Properties

```
@property (T@"_UIMainMenuCommand",R,N,V_command) command;
@property (T@"_UIMainMenuCommandState",R,N,V_state) state;
@property (T@"_UIMainMenuIdentifier",R,N,V_categoryMenuIdentifier) categoryMenuIdentifier;
```

## Class methods

```
+[_UIMainMenuPerformableKeyboardShortcutCommand supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuPerformableKeyboardShortcutCommand command];
-[_UIMainMenuPerformableKeyboardShortcutCommand encodeWithCoder:];
-[_UIMainMenuPerformableKeyboardShortcutCommand hash];
-[_UIMainMenuPerformableKeyboardShortcutCommand description];
-[_UIMainMenuPerformableKeyboardShortcutCommand initWithCoder:];
-[_UIMainMenuPerformableKeyboardShortcutCommand isEqual:];
-[_UIMainMenuPerformableKeyboardShortcutCommand state];
-[_UIMainMenuPerformableKeyboardShortcutCommand _initWithCommand:state:categoryMenuIdentifier:];
-[_UIMainMenuPerformableKeyboardShortcutCommand categoryMenuIdentifier];
```
