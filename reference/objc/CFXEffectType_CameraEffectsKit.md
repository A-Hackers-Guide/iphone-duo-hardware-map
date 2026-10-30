# `CFXEffectType`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 10 instance methods, 3 class methods

## Instance variables

```
i _jtEffectType;
@"NSOrderedSet" _effects;
@"NSString" _identifier;
@"NSString" _localizedTitle;
```

## Properties

```
@property (T@"NSOrderedSet",&,N,V_effects) effects;
@property (Ti,N,V_jtEffectType) jtEffectType;
@property (T@"NSString",C,N,V_localizedTitle) localizedTitle;
@property (T@"NSString",R,N,V_identifier) identifier;
```

## Class methods

```
+[CFXEffectType initialize];
+[CFXEffectType effectTypeWithIdentifier:];
+[CFXEffectType effectTypeIdentifiers];
```

## Instance methods

```
-[CFXEffectType localizedTitle];
-[CFXEffectType effects];
-[CFXEffectType identifier];
-[CFXEffectType setEffects:];
-[CFXEffectType hash];
-[CFXEffectType setLocalizedTitle:];
-[CFXEffectType isEqual:];
-[CFXEffectType initWithIdentifier:];
-[CFXEffectType jtEffectType];
-[CFXEffectType setJtEffectType:];
```
