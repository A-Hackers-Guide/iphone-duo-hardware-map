# `JFXEffectCategory`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _isNewCategory;
B _containsNewEffects;
i _effectType;
@"NSString" _categoryID;
@"NSString" _displayName;
@"NSArray" _effectIDs;
```

## Properties

```
@property (T@"NSString",&,N,V_categoryID) categoryID;
@property (T@"NSString",&,N,V_displayName) displayName;
@property (T@"NSArray",&,N,V_effectIDs) effectIDs;
@property (Ti,N,V_effectType) effectType;
@property (TB,R,N,V_isNewCategory) isNewCategory;
@property (TB,R,N,V_containsNewEffects) containsNewEffects;
```

## Instance methods

```
-[JFXEffectCategory setCategoryID:];
-[JFXEffectCategory displayName];
-[JFXEffectCategory setDisplayName:];
-[JFXEffectCategory setEffectType:];
-[JFXEffectCategory effectType];
-[JFXEffectCategory categoryID];
-[JFXEffectCategory containsNewEffects];
-[JFXEffectCategory effectIDs];
-[JFXEffectCategory initWithCategoryID:forEffectType:displayName:effectIDs:isNewCategory:containsNewEffects:];
-[JFXEffectCategory isNewCategory];
-[JFXEffectCategory setEffectIDs:];
```
