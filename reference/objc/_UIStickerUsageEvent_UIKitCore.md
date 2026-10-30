# `_UIStickerUsageEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 11 instance methods, 3 class methods

## Instance variables

```
q _sourceType;
q _usageType;
q _stickerType;
q _effectType;
```

## Properties

```
@property (Tq,N,V_sourceType) sourceType;
@property (Tq,N,V_usageType) usageType;
@property (Tq,N,V_stickerType) stickerType;
@property (Tq,N,V_effectType) effectType;
```

## Class methods

```
+[_UIStickerUsageEvent effectTypeForSticker:];
+[_UIStickerUsageEvent effectTypeFromVKCStickerEffectType:];
+[_UIStickerUsageEvent isPreferredRepresentationAnimated:];
```

## Instance methods

```
-[_UIStickerUsageEvent send];
-[_UIStickerUsageEvent sourceType];
-[_UIStickerUsageEvent setSourceType:];
-[_UIStickerUsageEvent setEffectType:];
-[_UIStickerUsageEvent effectType];
-[_UIStickerUsageEvent setStickerType:];
-[_UIStickerUsageEvent initForEmojiKeyboardUsage];
-[_UIStickerUsageEvent initWithSuggestedSticker:];
-[_UIStickerUsageEvent setUsageType:];
-[_UIStickerUsageEvent stickerType];
-[_UIStickerUsageEvent usageType];
```
