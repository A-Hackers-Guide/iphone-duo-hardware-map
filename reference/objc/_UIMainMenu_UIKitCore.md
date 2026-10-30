# `_UIMainMenu`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMainMenuElement`, `NSSecureCoding`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"_UIMainMenuIdentifier" _identifier;
@"UIMenu" _uiMenu;
@"NSArray" _children;
```

## Properties

```
@property (T@"_UIMainMenuIdentifier",R,N,V_identifier) identifier;
@property (T@"UIMenu",R,N,V_uiMenu) uiMenu;
@property (T@"NSArray",R,N,V_children) children;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMainMenu supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenu identifier];
-[_UIMainMenu children];
-[_UIMainMenu encodeWithCoder:];
-[_UIMainMenu hash];
-[_UIMainMenu description];
-[_UIMainMenu initWithCoder:];
-[_UIMainMenu isEqual:];
-[_UIMainMenu _initWithIdentifier:uiMenu:children:];
-[_UIMainMenu _initWithUIMenu:children:isPartOfBaseMenu:];
-[_UIMainMenu uiMenu];
```
