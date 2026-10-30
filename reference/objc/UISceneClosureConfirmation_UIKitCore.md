# `UISceneClosureConfirmation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 8 properties, 16 instance methods, 3 class methods

## Instance variables

```
@"NSString" _title;
@"NSString" _message;
@"NSArray" _sceneClosureActions;
@"UIColor" __tintColor;
```

## Properties

```
@property (T@"NSString",C,N,V_title) _title;
@property (T@"NSString",C,N,V_message) _message;
@property (T@"NSArray",C,N,V_sceneClosureActions) _sceneClosureActions;
@property (T@"UIColor",&,N,V__tintColor) _tintColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISceneClosureConfirmation supportsBSXPCSecureCoding];
+[UISceneClosureConfirmation supportsSecureCoding];
+[UISceneClosureConfirmation confirmationWithTitle:message:actions:];
```

## Instance methods

```
-[UISceneClosureConfirmation _tintColor];
-[UISceneClosureConfirmation _message];
-[UISceneClosureConfirmation encodeWithCoder:];
-[UISceneClosureConfirmation hash];
-[UISceneClosureConfirmation initWithCoder:];
-[UISceneClosureConfirmation encodeWithBSXPCCoder:];
-[UISceneClosureConfirmation initWithBSXPCCoder:];
-[UISceneClosureConfirmation copyWithZone:];
-[UISceneClosureConfirmation isEqual:];
-[UISceneClosureConfirmation _actionWithIdentifier:];
-[UISceneClosureConfirmation _sceneClosureActions];
-[UISceneClosureConfirmation _title];
-[UISceneClosureConfirmation set_message:];
-[UISceneClosureConfirmation set_sceneClosureActions:];
-[UISceneClosureConfirmation set_tintColor:];
-[UISceneClosureConfirmation set_title:];
```
