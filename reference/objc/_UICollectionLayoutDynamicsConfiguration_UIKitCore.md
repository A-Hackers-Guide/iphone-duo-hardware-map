# `_UICollectionLayoutDynamicsConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _dirtyItems;
@"NSArray" _items;
@"NSMutableDictionary" _behaviorDict;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previousVisibleBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentVisibleBounds;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_behaviorDict) behaviorDict;
@property (T@"NSArray",&,N) dynamicItems;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_previousVisibleBounds) previousVisibleBounds;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_currentVisibleBounds) currentVisibleBounds;
```

## Instance methods

```
-[_UICollectionLayoutDynamicsConfiguration _reset];
-[_UICollectionLayoutDynamicsConfiguration init];
-[_UICollectionLayoutDynamicsConfiguration _dirtyItems];
-[_UICollectionLayoutDynamicsConfiguration _setBehaviors:forItem:];
-[_UICollectionLayoutDynamicsConfiguration behaviorDict];
-[_UICollectionLayoutDynamicsConfiguration behaviorsForItem:];
-[_UICollectionLayoutDynamicsConfiguration currentVisibleBounds];
-[_UICollectionLayoutDynamicsConfiguration dynamicItems];
-[_UICollectionLayoutDynamicsConfiguration previousVisibleBounds];
-[_UICollectionLayoutDynamicsConfiguration setBehaviorDict:];
-[_UICollectionLayoutDynamicsConfiguration setBehaviors:forItem:];
-[_UICollectionLayoutDynamicsConfiguration setCurrentVisibleBounds:];
-[_UICollectionLayoutDynamicsConfiguration setDynamicItems:];
-[_UICollectionLayoutDynamicsConfiguration setPreviousVisibleBounds:];
```
