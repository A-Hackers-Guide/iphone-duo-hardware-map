# `UIPhysicalKeyboardEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPressesEvent`
- Protocols: `NSSecureCoding`
- 22 instance variables, 25 properties, 58 instance methods, 2 class methods

## Instance variables

```
B _canPrivatize;
@"_UIPhysicalKeyTranslationMap" _originalEscapeKeyTranslationMap;
@"_UIPhysicalKeyTranslationMap" _keyTranslationMap;
B _needToPrepareKeyTranslationMap;
B __isFromEmojiPopover;
B _keyCommandHandlingBeforePublic;
B _keyEventForwardedFromInputUIHost;
B _shiftDown;
B __externalEvent;
i _inputFlags;
I _keyCommandCode;
@"NSString" _modifiedInput;
@"NSString" _unmodifiedInput;
@"NSString" _shiftModifiedInput;
@"NSString" _commandModifiedInput;
@"NSString" _markedInput;
q _modifierFlags;
@"NSString" _privateInput;
q _privateModifierFlags;
@"NSString" _hint;
q __keyCode;
q _source;
```

## Properties

```
@property (T@"NSString",&,N,V_modifiedInput) _modifiedInput;
@property (T@"NSString",&,N,V_unmodifiedInput) _unmodifiedInput;
@property (T@"NSString",&,N,V_shiftModifiedInput) _shiftModifiedInput;
@property (T@"NSString",&,N,V_commandModifiedInput) _commandModifiedInput;
@property (T@"NSString",&,N,V_markedInput) _markedInput;
@property (T@"NSString",&,N,V_privateInput) _privateInput;
@property (T@"NSString",&,N,V_hint) _hint;
@property (Tq,N,S_setModifierFlags:,V_modifierFlags) _modifierFlags;
@property (Tq,N,V_privateModifierFlags) _privateModifierFlags;
@property (Tq,R,N) _gsModifierFlags;
@property (TB,R,N) _isKeyDown;
@property (TB,R,N) _isGlobeKey;
@property (TB,R,N) _isEjectKey;
@property (TB,R,N) _isModifierKey;
@property (TB,R,N) _isARepeat;
@property (TB,R,N) _isDeleteKey;
@property (Tq,N,V__keyCode) _keyCode;
@property (Ti,N,V_inputFlags) _inputFlags;
@property (Tq,N,V_source) source;
@property (TB,N,V__isFromEmojiPopover) _isFromEmojiPopover;
@property (TI,N,V_keyCommandCode) keyCommandCode;
@property (TB,N,V_keyCommandHandlingBeforePublic) keyCommandHandlingBeforePublic;
@property (TB,N,V_keyEventForwardedFromInputUIHost) keyEventForwardedFromInputUIHost;
@property (TB,N,V_shiftDown) shiftDown;
@property (TB,N,G_isExternalEvent,V__externalEvent) _externalEvent;
```

## Class methods

```
+[UIPhysicalKeyboardEvent supportsSecureCoding];
+[UIPhysicalKeyboardEvent _eventWithInput:inputFlags:];
```

## Instance methods

```
-[UIPhysicalKeyboardEvent _isARepeat];
-[UIPhysicalKeyboardEvent _cloneEvent];
-[UIPhysicalKeyboardEvent _hint];
-[UIPhysicalKeyboardEvent _setHIDEvent:keyboard:];
-[UIPhysicalKeyboardEvent set_markedInput:];
-[UIPhysicalKeyboardEvent _isModifierKey];
-[UIPhysicalKeyboardEvent keyCommandHandlingBeforePublic];
-[UIPhysicalKeyboardEvent set_hint:];
-[UIPhysicalKeyboardEvent _keyCode];
-[UIPhysicalKeyboardEvent setShiftDown:];
-[UIPhysicalKeyboardEvent set_keyCode:];
-[UIPhysicalKeyboardEvent _matchFidelityForKeyboardShortcutLeaf:translationMap:additionalModifiers:];
-[UIPhysicalKeyboardEvent setKeyEventForwardedFromInputUIHost:];
-[UIPhysicalKeyboardEvent keyEventForwardedFromInputUIHost];
-[UIPhysicalKeyboardEvent _isFromEmojiPopover];
-[UIPhysicalKeyboardEvent modifierFlags];
-[UIPhysicalKeyboardEvent _isDeleteKey];
-[UIPhysicalKeyboardEvent _modifierFlags];
-[UIPhysicalKeyboardEvent set_privateInput:];
-[UIPhysicalKeyboardEvent shiftDown];
-[UIPhysicalKeyboardEvent set_externalEvent:];
-[UIPhysicalKeyboardEvent set_privateModifierFlags:];
-[UIPhysicalKeyboardEvent _prepareKeyTranslationMapIfNeeded];
-[UIPhysicalKeyboardEvent _commandModifiedInput];
-[UIPhysicalKeyboardEvent setKeyCommandCode:];
-[UIPhysicalKeyboardEvent setSource:];
-[UIPhysicalKeyboardEvent _shiftModifiedInput];
-[UIPhysicalKeyboardEvent set_shiftModifiedInput:];
-[UIPhysicalKeyboardEvent set_commandModifiedInput:];
-[UIPhysicalKeyboardEvent type];
-[UIPhysicalKeyboardEvent _markedInput];
-[UIPhysicalKeyboardEvent set_inputFlags:];
-[UIPhysicalKeyboardEvent _unmodifiedInput];
-[UIPhysicalKeyboardEvent _isExternalEvent];
-[UIPhysicalKeyboardEvent encodeWithCoder:];
-[UIPhysicalKeyboardEvent _isPhysicalKeyEvent];
-[UIPhysicalKeyboardEvent keyCommandCode];
-[UIPhysicalKeyboardEvent _matchFidelityForKeyboardShortcutLeaf:translationMap:];
-[UIPhysicalKeyboardEvent _isEjectKey];
-[UIPhysicalKeyboardEvent _isKeyDown];
-[UIPhysicalKeyboardEvent initWithCoder:];
-[UIPhysicalKeyboardEvent set_modifiedInput:];
-[UIPhysicalKeyboardEvent _setModifierFlags:];
-[UIPhysicalKeyboardEvent _privateInput];
-[UIPhysicalKeyboardEvent _isGlobeKey];
-[UIPhysicalKeyboardEvent _shouldAttemptSecurePasteAuthentication];
-[UIPhysicalKeyboardEvent _privatize];
-[UIPhysicalKeyboardEvent isEqual:];
-[UIPhysicalKeyboardEvent set_isFromEmojiPopover:];
-[UIPhysicalKeyboardEvent source];
-[UIPhysicalKeyboardEvent _privateModifierFlags];
-[UIPhysicalKeyboardEvent _gsModifierFlags];
-[UIPhysicalKeyboardEvent _inputFlags];
-[UIPhysicalKeyboardEvent setKeyCommandHandlingBeforePublic:];
-[UIPhysicalKeyboardEvent _modifiedInput];
-[UIPhysicalKeyboardEvent set_unmodifiedInput:];
-[UIPhysicalKeyboardEvent _matchFidelityForKeyboardShortcutLeaf:];
-[UIPhysicalKeyboardEvent _matchFidelityFromKeyMapForKeyboardShortcutLeaf:translationMap:translator:addingModifiers:ignoringModifiers:];
```
