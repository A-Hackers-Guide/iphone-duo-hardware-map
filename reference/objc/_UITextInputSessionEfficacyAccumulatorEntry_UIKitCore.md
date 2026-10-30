# `_UITextInputSessionEfficacyAccumulatorEntry`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _netCharacters;
q _userRemovedCharacters;
q _netEmojiCharacters;
q _userRemovedEmojiCharacters;
q _inputActions;
```

## Properties

```
@property (Tq,V_netCharacters) netCharacters;
@property (Tq,V_userRemovedCharacters) userRemovedCharacters;
@property (Tq,V_netEmojiCharacters) netEmojiCharacters;
@property (Tq,V_userRemovedEmojiCharacters) userRemovedEmojiCharacters;
@property (Tq,V_inputActions) inputActions;
```

## Class methods

```
+[_UITextInputSessionEfficacyAccumulatorEntry generateAccumulatorEntryFromAction:];
```

## Instance methods

```
-[_UITextInputSessionEfficacyAccumulatorEntry increaseWithEntry:];
-[_UITextInputSessionEfficacyAccumulatorEntry inputActions];
-[_UITextInputSessionEfficacyAccumulatorEntry isAllZeroes];
-[_UITextInputSessionEfficacyAccumulatorEntry netCharacters];
-[_UITextInputSessionEfficacyAccumulatorEntry netEmojiCharacters];
-[_UITextInputSessionEfficacyAccumulatorEntry setInputActions:];
-[_UITextInputSessionEfficacyAccumulatorEntry setNetCharacters:];
-[_UITextInputSessionEfficacyAccumulatorEntry setNetEmojiCharacters:];
-[_UITextInputSessionEfficacyAccumulatorEntry setUserRemovedCharacters:];
-[_UITextInputSessionEfficacyAccumulatorEntry setUserRemovedEmojiCharacters:];
-[_UITextInputSessionEfficacyAccumulatorEntry userRemovedCharacters];
-[_UITextInputSessionEfficacyAccumulatorEntry userRemovedEmojiCharacters];
```
