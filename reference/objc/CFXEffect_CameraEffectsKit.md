# `CFXEffect`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 4 properties, 9 instance methods, 6 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _localizedTitle;
@"JFXEffect" _jtEffect;
```

## Properties

```
@property (TB,R,N) isNone;
@property (T@"JFXEffect",&,N,V_jtEffect) jtEffect;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_localizedTitle) localizedTitle;
```

## Class methods

```
+[CFXEffect effectIdentifiersForEffectType:];
+[CFXEffect effectWithIdentifier:forEffectType:];
+[CFXEffect effectWithJTEffect:];
+[CFXEffect initEffectRegistry];
+[CFXEffect preWarmShaderCache];
+[CFXEffect setupFactoryDelegate];
```

## Instance methods

```
-[CFXEffect localizedTitle];
-[CFXEffect identifier];
-[CFXEffect hash];
-[CFXEffect copyWithZone:];
-[CFXEffect isEqual:];
-[CFXEffect isNone];
-[CFXEffect initWithJTEffect:];
-[CFXEffect jtEffect];
-[CFXEffect setJtEffect:];
```
