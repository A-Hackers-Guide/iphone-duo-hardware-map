# `_UIEventSessionAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 19 properties, 30 instance methods, 3 class methods

## Instance variables

```
q _source;
q _actionType;
@"NSNumber" _sessionID;
q _uiInterfaceOrientation;
q _magicKeyboardState;
q _hardwareKeyboardState;
q _sequenceNumber;
q _actionCountFromMergedActions;
```

## Properties

```
@property (Tq,N,V_source) source;
@property (Tq,N,V_actionType) actionType;
@property (T@"_UIEventSessionTouchAction",R,N) asTouch;
@property (T@"_UIEventSessionTapAction",R,N) asTap;
@property (T@"_UIEventSessionScrollAction",R,N) asScroll;
@property (T@"_UIEventSessionContextualAction",R,N) asContextualPress;
@property (T@"_UIEventSessionTypingAction",R,N) asTyping;
@property (T@"_UIEventSessionTextSelectionAction",R,N) asTextSelection;
@property (T@"_UIEventSessionKeyCommandAction",R,N) asKeyCommand;
@property (T@"_UIEventSessionHoverAction",R,N) asHover;
@property (T@"NSNumber",&,N,V_sessionID) sessionID;
@property (Tq,N,V_uiInterfaceOrientation) uiInterfaceOrientation;
@property (Tq,N,V_magicKeyboardState) magicKeyboardState;
@property (Tq,N,V_hardwareKeyboardState) hardwareKeyboardState;
@property (Tq,N,V_sequenceNumber) sequenceNumber;
@property (T@"NSString",R,N) typeEncoding;
@property (T@"NSString",R,N) metadata;
@property (Tq,R,N) actionCount;
@property (Tq,N,V_actionCountFromMergedActions) actionCountFromMergedActions;
```

## Class methods

```
+[_UIEventSessionAction stringValueForSource:];
+[_UIEventSessionAction getUIEventSourceForUITouchType:];
+[_UIEventSessionAction stringValueForActionType:];
```

## Instance methods

```
-[_UIEventSessionAction setActionType:];
-[_UIEventSessionAction sessionID];
-[_UIEventSessionAction setSessionID:];
-[_UIEventSessionAction setSequenceNumber:];
-[_UIEventSessionAction sequenceNumber];
-[_UIEventSessionAction metadata];
-[_UIEventSessionAction setSource:];
-[_UIEventSessionAction actionType];
-[_UIEventSessionAction description];
-[_UIEventSessionAction mergeActionIfPossible:];
-[_UIEventSessionAction copyWithZone:];
-[_UIEventSessionAction source];
-[_UIEventSessionAction asTextSelection];
-[_UIEventSessionAction asHover];
-[_UIEventSessionAction asTouch];
-[_UIEventSessionAction actionCount];
-[_UIEventSessionAction actionCountFromMergedActions];
-[_UIEventSessionAction asContextualPress];
-[_UIEventSessionAction asKeyCommand];
-[_UIEventSessionAction asScroll];
-[_UIEventSessionAction asTap];
-[_UIEventSessionAction asTyping];
-[_UIEventSessionAction hardwareKeyboardState];
-[_UIEventSessionAction magicKeyboardState];
-[_UIEventSessionAction setActionCountFromMergedActions:];
-[_UIEventSessionAction setHardwareKeyboardState:];
-[_UIEventSessionAction setMagicKeyboardState:];
-[_UIEventSessionAction setUiInterfaceOrientation:];
-[_UIEventSessionAction typeEncoding];
-[_UIEventSessionAction uiInterfaceOrientation];
```
