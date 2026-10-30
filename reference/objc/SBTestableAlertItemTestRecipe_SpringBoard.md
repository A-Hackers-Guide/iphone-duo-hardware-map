# `SBTestableAlertItemTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTestRecipe`
- 3 instance variables, 5 properties, 15 instance methods, 3 class methods

## Instance variables

```
@"SBAlertItem" _item;
@"SBWindowScene" _windowScene;
@"NSArray" _recipesToTest;
```

## Properties

```
@property (T@"NSArray",&,N,V_recipesToTest) recipesToTest;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBTestableAlertItemTestRecipe nameForCase:];
+[SBTestableAlertItemTestRecipe testCases];
+[SBTestableAlertItemTestRecipe testCasesGrouped];
```

## Instance methods

```
-[SBTestableAlertItemTestRecipe iconController];
-[SBTestableAlertItemTestRecipe title];
-[SBTestableAlertItemTestRecipe _anyAppIcon];
-[SBTestableAlertItemTestRecipe _anySUDescriptor];
-[SBTestableAlertItemTestRecipe _anyUserInstalledAppIcon];
-[SBTestableAlertItemTestRecipe _dismissCurrentItem];
-[SBTestableAlertItemTestRecipe _mapsApp];
-[SBTestableAlertItemTestRecipe _nextAlertItemToTest];
-[SBTestableAlertItemTestRecipe alertForIndex:];
-[SBTestableAlertItemTestRecipe dataPlanAlertItemForCase:];
-[SBTestableAlertItemTestRecipe handleVolumeDecrease];
-[SBTestableAlertItemTestRecipe handleVolumeIncrease];
-[SBTestableAlertItemTestRecipe recipesToTest];
-[SBTestableAlertItemTestRecipe setRecipesToTest:];
-[SBTestableAlertItemTestRecipe windowSceneDidUpdate:];
```
