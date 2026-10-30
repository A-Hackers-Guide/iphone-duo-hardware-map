# `_UIMainMenuCommand`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMainMenuElement`, `NSSecureCoding`
- 4 instance variables, 8 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"UIMenuElement<_UIMenuLeaf>" _localClientMenuLeaf;
@"_UIMainMenuCommandKeyboardShortcut" _keyboardShortcut;
@"_UIMainMenuCommandIdentifier" _identifier;
@"NSArray" _alternates;
```

## Properties

```
@property (T@"UIMenuElement<_UIMenuLeaf>",&,N,V_localClientMenuLeaf) _localClientMenuLeaf;
@property (T@"_UIMainMenuCommandKeyboardShortcut",R,N,V_keyboardShortcut) _keyboardShortcut;
@property (T@"_UIMainMenuCommandIdentifier",R,N,V_identifier) identifier;
@property (T@"NSArray",R,N,V_alternates) alternates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMainMenuCommand supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuCommand identifier];
-[_UIMainMenuCommand encodeWithCoder:];
-[_UIMainMenuCommand hash];
-[_UIMainMenuCommand description];
-[_UIMainMenuCommand initWithCoder:];
-[_UIMainMenuCommand isEqual:];
-[_UIMainMenuCommand alternates];
-[_UIMainMenuCommand _initWithIdentifier:uiMenuLeaf:keyboardShortcut:alternates:];
-[_UIMainMenuCommand _initWithUIMenuLeaf:allowingKeyboardShortcuts:];
-[_UIMainMenuCommand _isHiddenForState:];
-[_UIMainMenuCommand _keyboardShortcut];
-[_UIMainMenuCommand _localClientMenuLeaf];
-[_UIMainMenuCommand _uiActionForSelfOnlyForSession:commandState:primaryActionHandler:];
-[_UIMainMenuCommand _uiActionForSelfOnlyForSession:parentState:primaryActionHandler:];
-[_UIMainMenuCommand set_localClientMenuLeaf:];
-[_UIMainMenuCommand uiMenuLeafForCommandAndAlternatesForSession:parentState:primaryActionHandler:];
```
