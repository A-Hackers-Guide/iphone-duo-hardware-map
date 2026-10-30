# `_UIKeyboardChangedInformation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIKeyboardUIInformation`
- 18 instance variables, 18 properties, 44 instance methods, 7 class methods

## Instance variables

```
B _avoidIntersectability;
B _multipleScenes;
B _isOneness;
B _automaticMinimizationEnabled;
B _isFloating;
B _shouldTakeSnapshot;
B _shouldRestoreKeyboard;
i _hostProcessIdentifier;
i _processIdentifier;
@"NSString" _sourceSceneIdentityString;
@"NSString" _sourceDisplayIdentifier;
@"NSString" _sourceBundleIdentifier;
@"NSString" _hostBundleIdentifier;
d _keyboardIAVHeight;
@"NSString" _keyboardPreserveKey;
{CGPoint="x"d"y"d} _persistentOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardPositionWithIAV;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _keyboardPositionWithRemoteIAV;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,V_keyboardPositionWithIAV) keyboardPositionWithIAV;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_keyboardPositionWithRemoteIAV) keyboardPositionWithRemoteIAV;
@property (Td,R,V_keyboardIAVHeight) keyboardIAVHeight;
@property (TB,V_isFloating) isFloating;
@property (T{CGPoint=dd},V_persistentOffset) persistentOffset;
@property (TB,N,V_avoidIntersectability) avoidIntersectability;
@property (TB,N,V_multipleScenes) multipleScenes;
@property (TB,N,V_isOneness) isOneness;
@property (TB,N,V_automaticMinimizationEnabled) automaticMinimizationEnabled;
@property (TB,N,V_shouldTakeSnapshot) shouldTakeSnapshot;
@property (TB,R,V_shouldRestoreKeyboard) shouldRestoreKeyboard;
@property (T@"NSString",C,N,V_sourceSceneIdentityString) sourceSceneIdentityString;
@property (T@"NSString",C,N,V_sourceBundleIdentifier) sourceBundleIdentifier;
@property (T@"NSString",C,N,V_hostBundleIdentifier) hostBundleIdentifier;
@property (Ti,N,V_hostProcessIdentifier) hostProcessIdentifier;
@property (Ti,N,V_processIdentifier) processIdentifier;
@property (T@"NSString",C,N,V_sourceDisplayIdentifier) sourceDisplayIdentifier;
@property (T@"NSString",C,N,V_keyboardPreserveKey) keyboardPreserveKey;
```

## Class methods

```
+[_UIKeyboardChangedInformation animationFence];
+[_UIKeyboardChangedInformation supportsSecureCoding];
+[_UIKeyboardChangedInformation informationForKeyboardUp:withIAV:];
+[_UIKeyboardChangedInformation informationForKeyboardPreserve:];
+[_UIKeyboardChangedInformation informationForKeyboardRestore:];
+[_UIKeyboardChangedInformation informationForKeyboardDown];
+[_UIKeyboardChangedInformation informationForKeyboardUpWithIAVHeight:];
```

## Instance methods

```
-[_UIKeyboardChangedInformation descriptionForLog];
-[_UIKeyboardChangedInformation setPersistentOffset:];
-[_UIKeyboardChangedInformation setAutomaticMinimizationEnabled:];
-[_UIKeyboardChangedInformation setSourceBundleIdentifier:];
-[_UIKeyboardChangedInformation persistentOffset];
-[_UIKeyboardChangedInformation setIsFloating:];
-[_UIKeyboardChangedInformation setMultipleScenes:];
-[_UIKeyboardChangedInformation isFloating];
-[_UIKeyboardChangedInformation automaticMinimizationEnabled];
-[_UIKeyboardChangedInformation setAvoidIntersectability:];
-[_UIKeyboardChangedInformation setHostBundleIdentifier:];
-[_UIKeyboardChangedInformation setKeyboardPreserveKey:];
-[_UIKeyboardChangedInformation sourceBundleIdentifier];
-[_UIKeyboardChangedInformation setHostProcessIdentifier:];
-[_UIKeyboardChangedInformation setProcessIdentifier:];
-[_UIKeyboardChangedInformation setShouldTakeSnapshot:];
-[_UIKeyboardChangedInformation sourceSceneIdentityString];
-[_UIKeyboardChangedInformation setSourceDisplayIdentifier:];
-[_UIKeyboardChangedInformation dealloc];
-[_UIKeyboardChangedInformation keyboardPreserveKey];
-[_UIKeyboardChangedInformation avoidIntersectability];
-[_UIKeyboardChangedInformation initWithKeyboardRect:iavPosition:onScreen:takeSnapshot:fence:];
-[_UIKeyboardChangedInformation keyboardIAVHeight];
-[_UIKeyboardChangedInformation shouldTakeSnapshot];
-[_UIKeyboardChangedInformation hostBundleIdentifier];
-[_UIKeyboardChangedInformation initWithKeyboardIAVHeight:onScreen:takeSnapshot:fence:];
-[_UIKeyboardChangedInformation copyWithIntersectability:];
-[_UIKeyboardChangedInformation shouldRestoreKeyboard];
-[_UIKeyboardChangedInformation setIsOneness:];
-[_UIKeyboardChangedInformation encodeWithCoder:];
-[_UIKeyboardChangedInformation copyWithoutFence];
-[_UIKeyboardChangedInformation setKeyboardPositionWithRemoteIAV:];
-[_UIKeyboardChangedInformation description];
-[_UIKeyboardChangedInformation keyboardPositionWithRemoteIAV];
-[_UIKeyboardChangedInformation initWithCoder:];
-[_UIKeyboardChangedInformation hostProcessIdentifier];
-[_UIKeyboardChangedInformation processIdentifier];
-[_UIKeyboardChangedInformation keyboardPositionWithIAV];
-[_UIKeyboardChangedInformation multipleScenes];
-[_UIKeyboardChangedInformation copyWithZone:];
-[_UIKeyboardChangedInformation sourceDisplayIdentifier];
-[_UIKeyboardChangedInformation setSourceSceneIdentityString:];
-[_UIKeyboardChangedInformation copyWithoutIAVKeyboardRect:];
-[_UIKeyboardChangedInformation isOneness];
```
