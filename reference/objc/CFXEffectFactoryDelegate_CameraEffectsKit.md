# `CFXEffectFactoryDelegate`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `JFXEffectFactoryDelegate`
- 0 instance variables, 4 properties, 9 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXEffectFactoryDelegate sharedInstance];
```

## Instance methods

```
-[CFXEffectFactoryDelegate CFX_animojiEffectsWithFactory:];
-[CFXEffectFactoryDelegate CFX_filterEffectsWithFactory:];
-[CFXEffectFactoryDelegate CFX_isExpensiveEffectID:withFactory:];
-[CFXEffectFactoryDelegate JFXEffectClassForType:];
-[CFXEffectFactoryDelegate CFX_enoughPowerForStyleTransfer];
-[CFXEffectFactoryDelegate CFX_disableExpensiveFilters];
-[CFXEffectFactoryDelegate CFX_overlayEffectsWithFactory:];
-[CFXEffectFactoryDelegate effectFactory:createEffectContentDataSourceForEffectID:ofType:];
-[CFXEffectFactoryDelegate effectFactory:effectIDsAvailableForType:completion:];
```
