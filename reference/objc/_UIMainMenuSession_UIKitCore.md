# `_UIMainMenuSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 6 instance variables, 6 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuSessionLocalCache" _localCache;
@"NSDictionary" _visibleCommandKeyboardShortcuts;
@"NSDictionary" _hostKeyboardShortcuts;
@"NSDictionary" _performableKeyboardShortcutCommands;
@"_UIMainMenuSessionIdentifier" _identifier;
@"_UIMainMenu" _uncategorizedMenu;
```

## Properties

```
@property (T@"_UIMainMenuSessionLocalCache",R,N,V_localCache) _localCache;
@property (T@"NSDictionary",&,N,V_visibleCommandKeyboardShortcuts) _visibleCommandKeyboardShortcuts;
@property (T@"NSDictionary",&,N,V_hostKeyboardShortcuts) _hostKeyboardShortcuts;
@property (T@"NSDictionary",&,N,V_performableKeyboardShortcutCommands) _performableKeyboardShortcutCommands;
@property (T@"_UIMainMenu",&,N,V_uncategorizedMenu) uncategorizedMenu;
@property (T@"_UIMainMenuSessionIdentifier",R,N,V_identifier) identifier;
```

## Class methods

```
+[_UIMainMenuSession supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuSession identifier];
-[_UIMainMenuSession encodeWithCoder:];
-[_UIMainMenuSession hash];
-[_UIMainMenuSession description];
-[_UIMainMenuSession initWithCoder:];
-[_UIMainMenuSession isEqual:];
-[_UIMainMenuSession _initWithIdentifier:localCache:];
-[_UIMainMenuSession _hostKeyboardShortcuts];
-[_UIMainMenuSession _initWithLocalCache:];
-[_UIMainMenuSession _isKeyboardShortcutVisibleForCommand:];
-[_UIMainMenuSession _localCache];
-[_UIMainMenuSession _performableKeyboardShortcutCommands];
-[_UIMainMenuSession _visibleCommandKeyboardShortcuts];
-[_UIMainMenuSession hostSideInvokableKeyboardShortcutsWithPrimaryActionHandler:];
-[_UIMainMenuSession setUncategorizedMenu:];
-[_UIMainMenuSession set_hostKeyboardShortcuts:];
-[_UIMainMenuSession set_performableKeyboardShortcutCommands:];
-[_UIMainMenuSession set_visibleCommandKeyboardShortcuts:];
-[_UIMainMenuSession uncategorizedMenu];
```
