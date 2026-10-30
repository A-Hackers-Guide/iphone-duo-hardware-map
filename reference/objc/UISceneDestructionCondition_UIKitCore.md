# `UISceneDestructionCondition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSXPCSecureCoding`, `NSCopying`
- 1 instance variables, 4 properties, 9 instance methods, 5 class methods

## Instance variables

```
q _kind;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISceneDestructionCondition supportsBSXPCSecureCoding];
+[UISceneDestructionCondition supportsSecureCoding];
+[UISceneDestructionCondition systemDisconnection];
+[UISceneDestructionCondition systemImmersionInterruption];
+[UISceneDestructionCondition userInitiatedDismissal];
```

## Instance methods

```
-[UISceneDestructionCondition encodeWithCoder:];
-[UISceneDestructionCondition hash];
-[UISceneDestructionCondition description];
-[UISceneDestructionCondition initWithCoder:];
-[UISceneDestructionCondition encodeWithBSXPCCoder:];
-[UISceneDestructionCondition initWithBSXPCCoder:];
-[UISceneDestructionCondition copyWithZone:];
-[UISceneDestructionCondition isEqual:];
-[UISceneDestructionCondition _initWithKind:];
```
