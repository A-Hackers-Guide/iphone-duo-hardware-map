# `_UISceneClosureAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`, `BSXPCSecureCoding`
- 2 instance variables, 6 properties, 11 instance methods, 3 class methods

## Instance variables

```
@"NSString" _actionIdentifier;
@"UIAlertAction" _alertAction;
```

## Properties

```
@property (T@"NSString",C,N,V_actionIdentifier) actionIdentifier;
@property (T@"UIAlertAction",&,N,V_alertAction) alertAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneClosureAction supportsBSXPCSecureCoding];
+[_UISceneClosureAction supportsSecureCoding];
+[_UISceneClosureAction actionWithAlertAction:];
```

## Instance methods

```
-[_UISceneClosureAction actionIdentifier];
-[_UISceneClosureAction encodeWithCoder:];
-[_UISceneClosureAction hash];
-[_UISceneClosureAction initWithCoder:];
-[_UISceneClosureAction encodeWithBSXPCCoder:];
-[_UISceneClosureAction initWithBSXPCCoder:];
-[_UISceneClosureAction copyWithZone:];
-[_UISceneClosureAction isEqual:];
-[_UISceneClosureAction setAlertAction:];
-[_UISceneClosureAction alertAction];
-[_UISceneClosureAction setActionIdentifier:];
```
