# `_UISupplementalItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@ _internal;
@"UIImage" _icon;
@"NSDictionary" _userInfo;
```

## Properties

```
@property (TQ,R,N,G_identifier) identifier;
@property (T@"UIImage",C,N,V_icon) icon;
@property (T@"NSDictionary",C,N,V_userInfo) userInfo;
```

## Class methods

```
+[_UISupplementalItem supportsSecureCoding];
+[_UISupplementalItem _uiSupplementalItemWithTISupplementalItem:icon:];
```

## Instance methods

```
-[_UISupplementalItem userInfo];
-[_UISupplementalItem setIcon:];
-[_UISupplementalItem setUserInfo:];
-[_UISupplementalItem _init];
-[_UISupplementalItem encodeWithCoder:];
-[_UISupplementalItem initWithCoder:];
-[_UISupplementalItem copyWithZone:];
-[_UISupplementalItem _identifier];
-[_UISupplementalItem icon];
```
