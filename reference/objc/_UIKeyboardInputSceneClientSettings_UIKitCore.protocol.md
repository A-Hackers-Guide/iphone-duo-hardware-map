# `_UIKeyboardInputSceneClientSettings` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 11 properties, 22 instance methods, 0 class methods

## Properties

```
@property (T@"NSArray",&,N) visibleKeyboardFrames;
@property (TB,N) keyboardInTrackpadMode;
@property (TB,N) pairedSceneIsForeground;
@property (Tq,N) pairedSceneInterfaceOrientation;
@property (T@"FBSDisplayConfiguration",&,N) pairedSceneDisplayConfiguration;
@property (T@"NSString",&,N) pairedScenePreferredKeyboardNamespaceIdentifier;
@property (T@"_UISceneSafeAreaEdgeInsetResolver",&,N) pairedSceneSafeAreaEdgeInsetResolver;
@property (T@"_UISceneSafeAreaCornerInsetResolver",&,N) pairedSceneSafeAreaCornerInsetResolver;
@property (T@"BSCornerRadiusConfiguration",&,N) pairedSceneCornerRadiusConfiguration;
@property (TQ,N) pairedSceneDeactivationReasons;
@property (Tq,N) pairedSceneUserInterfaceStyle;
```

## Instance methods

```
-[_UIKeyboardInputSceneClientSettings visibleKeyboardFrames];
-[_UIKeyboardInputSceneClientSettings keyboardInTrackpadMode];
-[_UIKeyboardInputSceneClientSettings pairedSceneInterfaceOrientation];
-[_UIKeyboardInputSceneClientSettings pairedSceneDisplayConfiguration];
-[_UIKeyboardInputSceneClientSettings pairedSceneCornerRadiusConfiguration];
-[_UIKeyboardInputSceneClientSettings pairedSceneDeactivationReasons];
-[_UIKeyboardInputSceneClientSettings pairedSceneIsForeground];
-[_UIKeyboardInputSceneClientSettings pairedScenePreferredKeyboardNamespaceIdentifier];
-[_UIKeyboardInputSceneClientSettings pairedSceneSafeAreaCornerInsetResolver];
-[_UIKeyboardInputSceneClientSettings pairedSceneSafeAreaEdgeInsetResolver];
-[_UIKeyboardInputSceneClientSettings pairedSceneUserInterfaceStyle];
-[_UIKeyboardInputSceneClientSettings setKeyboardInTrackpadMode:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneCornerRadiusConfiguration:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneDeactivationReasons:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneDisplayConfiguration:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneInterfaceOrientation:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneIsForeground:];
-[_UIKeyboardInputSceneClientSettings setPairedScenePreferredKeyboardNamespaceIdentifier:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneSafeAreaCornerInsetResolver:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneSafeAreaEdgeInsetResolver:];
-[_UIKeyboardInputSceneClientSettings setPairedSceneUserInterfaceStyle:];
-[_UIKeyboardInputSceneClientSettings setVisibleKeyboardFrames:];
```
