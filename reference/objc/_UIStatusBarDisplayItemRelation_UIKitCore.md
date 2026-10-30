# `_UIStatusBarDisplayItemRelation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 2 properties, 5 instance methods, 4 class methods

## Properties

```
@property (TB,R,N,GisFulfilled) fulfilled;
@property (T@"NSArray",R,N) itemStates;
```

## Class methods

```
+[_UIStatusBarDisplayItemRelation allRelationWithRelations:];
+[_UIStatusBarDisplayItemRelation anyRelationWithRelations:];
+[_UIStatusBarDisplayItemRelation exclusionWithDisplayItemState:placement:];
+[_UIStatusBarDisplayItemRelation requirementWithDisplayItemState:placement:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemRelation _ui_descriptionBuilder];
-[_UIStatusBarDisplayItemRelation type];
-[_UIStatusBarDisplayItemRelation description];
-[_UIStatusBarDisplayItemRelation isFulfilled];
-[_UIStatusBarDisplayItemRelation itemStates];
```
