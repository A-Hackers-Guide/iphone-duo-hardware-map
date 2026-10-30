# `UISceneActivationConditions`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 15 instance methods, 2 class methods

## Instance variables

```
@"NSPredicate" _canActivatePredicate;
@"NSPredicate" _prefersPredicate;
@"UIScene" _uiScene;
```

## Properties

```
@property (T@"UIScene",W,N,S_setUIScene:,V_uiScene) _UIScene;
@property (T@"NSPredicate",C,N) canActivateForTargetContentIdentifierPredicate;
@property (T@"NSPredicate",C,N) prefersToActivateForTargetContentIdentifierPredicate;
```

## Class methods

```
+[UISceneActivationConditions supportsSecureCoding];
+[UISceneActivationConditions accessInstanceVariablesDirectly];
```

## Instance methods

```
-[UISceneActivationConditions _UIScene];
-[UISceneActivationConditions init];
-[UISceneActivationConditions _suitabilityForTargetContentIdentifier:errorString:];
-[UISceneActivationConditions prefersToActivateForTargetContentIdentifierPredicate];
-[UISceneActivationConditions setPrefersToActivateForTargetContentIdentifierPredicate:];
-[UISceneActivationConditions encodeWithCoder:];
-[UISceneActivationConditions setCanActivateForTargetContentIdentifierPredicate:];
-[UISceneActivationConditions hash];
-[UISceneActivationConditions _setUIScene:];
-[UISceneActivationConditions description];
-[UISceneActivationConditions initWithCoder:];
-[UISceneActivationConditions copyWithZone:];
-[UISceneActivationConditions isEqual:];
-[UISceneActivationConditions _validateCompileTimeIssues:runTimeIssues:];
-[UISceneActivationConditions canActivateForTargetContentIdentifierPredicate];
```
