# `_UICommandIdentifier`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
: _action;
@ _propertyList;
```

## Properties

```
@property (T:,R,N,V_action) action;
@property (T@,R,N,V_propertyList) propertyList;
```

## Class methods

```
+[_UICommandIdentifier supportsSecureCoding];
+[_UICommandIdentifier identifierWithAction:propertyList:];
```

## Instance methods

```
-[_UICommandIdentifier propertyList];
-[_UICommandIdentifier action];
-[_UICommandIdentifier encodeWithCoder:];
-[_UICommandIdentifier hash];
-[_UICommandIdentifier description];
-[_UICommandIdentifier initWithCoder:];
-[_UICommandIdentifier copyWithZone:];
-[_UICommandIdentifier initWithAction:propertyList:];
-[_UICommandIdentifier isEqual:];
```
