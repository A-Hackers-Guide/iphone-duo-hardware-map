# `SBResolvedKeyboardFocusContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"FBSSceneIdentityToken" _sceneIdentityToken;
I _windowContextID;
B _focusedOnEmbeddedRemoteAlert;
```

## Properties

```
@property (T@"FBSSceneIdentityToken",R,N,V_sceneIdentityToken) sceneIdentityToken;
@property (TI,R,N,V_windowContextID) windowContextID;
@property (TB,N,GisFocusedOnEmbeddedRemoteAlert,V_focusedOnEmbeddedRemoteAlert) focusedOnEmbeddedRemoteAlert;
```

## Instance methods

```
-[SBResolvedKeyboardFocusContext init];
-[SBResolvedKeyboardFocusContext hash];
-[SBResolvedKeyboardFocusContext description];
-[SBResolvedKeyboardFocusContext copyWithZone:];
-[SBResolvedKeyboardFocusContext isEqual:];
-[SBResolvedKeyboardFocusContext sceneIdentityToken];
-[SBResolvedKeyboardFocusContext windowContextID];
-[SBResolvedKeyboardFocusContext initWithSceneIdentityToken:windowContextID:];
-[SBResolvedKeyboardFocusContext isFocusedOnEmbeddedRemoteAlert];
-[SBResolvedKeyboardFocusContext setFocusedOnEmbeddedRemoteAlert:];
```
