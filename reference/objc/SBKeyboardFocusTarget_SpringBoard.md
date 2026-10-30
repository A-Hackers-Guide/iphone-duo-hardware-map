# `SBKeyboardFocusTarget`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 2 properties, 7 instance methods, 4 class methods

## Instance variables

```
@"FBSSceneIdentityToken" _sceneIdentityToken;
@"UIWindow" _window;
i _pid;
```

## Properties

```
@property (T@"FBSSceneIdentityToken",R,N,V_sceneIdentityToken) sceneIdentityToken;
@property (Ti,R,N,V_pid) pid;
```

## Class methods

```
+[SBKeyboardFocusTarget targetForUIWindow:];
+[SBKeyboardFocusTarget targetForFBScene:];
+[SBKeyboardFocusTarget targetForSBWindowScene:];
+[SBKeyboardFocusTarget targetForSceneIdentityToken:pid:];
```

## Instance methods

```
-[SBKeyboardFocusTarget pid];
-[SBKeyboardFocusTarget hash];
-[SBKeyboardFocusTarget description];
-[SBKeyboardFocusTarget copyWithZone:];
-[SBKeyboardFocusTarget isEqual:];
-[SBKeyboardFocusTarget sceneIdentityToken];
-[SBKeyboardFocusTarget focusChange];
```
